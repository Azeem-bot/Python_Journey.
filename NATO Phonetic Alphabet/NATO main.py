import pandas
data_dic = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_word = {row.letter:row.code for (index,row) in data_dic.iterrows()}

word = input("Enter a word: ").upper()
output = [phonetic_word[letter] for letter in word]
print(output)
