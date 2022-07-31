import random
import string
import pickle
class Encoding:
    def __init__(self, dct='non'):
        if dct == 'non':
            self.__dct = {}
            for char in string.ascii_letters:
                dct_code = ''
                dct_code += chr(random.randint(65,90))
                dct_code += chr(random.randint(97,122))
                dct_code += chr(random.randint(48,57))
                dct_code += chr(random.randint(33,46))
                self.__dct[char] = dct_code
            self.__dct[' '] = 'H#2a'
        elif type(dct) == type(dict):
            self.__dct = dct
        else:
            with open(f'{dct}.pkl', 'rb') as inp:
                self.__dct = pickle.load(inp)

    def saveobj(self):
        tmp = random.randint(1,100000)
        with open(f'dct{tmp}.pkl', 'wb') as outp:
            saved = self.__dct
            pickle.dump(saved, outp, pickle.HIGHEST_PROTOCOL)
        print(f'Your file was saved as: dct{tmp}')

    def encode(self, word):
        encoded = ''
        for char in word:
            encoded += self.__dct[char]

        return encoded

    def decode(self, word):
        decoded = ''
        count = 0
        for chars in range(len(word)//4):
            tmp = word[count:count+4]
            for key, value in self.__dct.items():
                if value == tmp:
                    decoded += key
            count += 4

        return decoded

    def get_dct(self):
        return self.__dct

        

    def pass_generator(self):

        lst = []

        for x in range(4):
            upp = chr(random.randint(65,90))
            low = chr(random.randint(97,122))
            dig = chr(random.randint(48,57))
            pun = chr(random.randint(33,46))
            lst.append(upp)
            lst.append(low)
            lst.append(dig)
            lst.append(pun)

        random.shuffle(lst)
        return "".join(lst)

# try:
#     test = Encoding('dct38875')
# except:
#     print('No file was found')


#encode a text:
#test.ecode('hello world')


#save the dictionary file
#test.saveobj()

#reuse later by creating new instance of the class using your pickle file
#test = Encoding('dct#')
# print(test.decode("""Rp0*Ho1$Tx5)Tx5)Mq9#H#2aEg1,Mq9#H#2aHp9!Mq9#Cn9+H#2aBl4%Io9-Ua3!Ua3!Io9-H#2aGt0'Tx5)Io9-Hp9!H#2aEg1,Mq9#Ss8&Io9-H#2aUf9)Hp9!H#2aIo9-Ua3!Hp9!H#2aCf5"Bi9*Io9-Ua3!Cf5"Ho1$"""))

