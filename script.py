from pprint import pprint
import string
import pandas as pd 
import matplotlib.pyplot as plt

class TextBase:
    def __init__(self):
        self.list_of_lines = []

    def load_text(self, filename: str):
        self.list_of_lines = open(filename).readlines()
        self.list_of_lines = [word.strip() for word in self.list_of_lines]
        self.list_of_lines = [word.replace('.', '').replace(',', '').split(' ') for word in self.list_of_lines]   
        self.list_of_lines = [word for sublist in self.list_of_lines for word in sublist]
        
class TextCypher(TextBase):
    def __init__(self):
        super().__init__()
    
    def encrypt(self, number_of_keys, *keys):
        keyIndex = 0
        lettersLen = len(string.ascii_uppercase)
        for index, word in enumerate(self.list_of_lines):
            newWord = ""
            for char in word:
                if(char not in string.ascii_letters):
                    newWord += char
                    continue
                charIndex = string.ascii_uppercase.index(char) if char.isupper() else string.ascii_lowercase.index(char)
                step = (charIndex + keys[keyIndex])

                if char.isupper():
                    newChar = string.ascii_uppercase[step % lettersLen]
                elif char.islower():
                    newChar = string.ascii_lowercase[step % lettersLen]
                newWord += newChar

            self.list_of_lines[index] = newWord
            if keyIndex < number_of_keys - 1:
                keyIndex += 1
            else:
                keyIndex = 0
            
    
tc = TextCypher()
tc.load_text('zen.txt')
tc.encrypt(3, *[8, 2, 5])
print(tc.list_of_lines)


class TextAnalyzer(TextBase):
    def __init__(self):
        self.list_of_lines = []
        self.word_count_dict = {}

    def generate_report(self):
        for line in self.list_of_lines:
                for word in line.split(' '):
                    if word.lower() in self.word_count_dict:
                        self.word_count_dict[word.lower()] += 1
                    else:
                        self.word_count_dict[word.lower()] = 1
        # print(self.word_count_dict)
        self.list_of_lines = (sorted(self.word_count_dict.items(), key=lambda kv: kv[1], reverse=True))
        print(self.list_of_lines)

    def generate_chart(self):
        pass
        # df = pd.DataFrame({'Words': [word[0] for word in self.list_of_lines], 
        #            'Count': [word[1] for word in self.list_of_lines]})
        # ws = [w[0] for w in self.list_of_lines]
        # nu = [w[1] for w in self.list_of_lines]
        # # print(self.list_of_lines)

        plt.barh(range(len(ws)),nu)
        plt.yticks(range(len(ws)),ws)

        plt.show()  
        # df = pd.DataFrame(list(zip(ws, nu))).set_index(1)
        # df.plot.barh()

        # plt.show()
text_analyzer = TextAnalyzer()
text_analyzer.load_text('zen.txt')
text_analyzer.generate_report()
text_analyzer.generate_chart()