import pandas
data_dic = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_word = {row.letter:row.code for (index,row) in data_dic.iterrows()}
def generate_phonetic():
  word = input("Enter a word: ").upper()
  try:
    output = [phonetic_word[letter] for letter in word]
  except:
    print("Sorry, only letters in the alphabet please")
    genarate_phonetic()
  else:
    print(output)
genarate_phonetic()

