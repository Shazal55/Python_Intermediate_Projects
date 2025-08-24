import pandas
data = pandas.read_csv("Book 3(Sheet1).csv")
phonetics = {row.Symbol : row.Code for (index, row) in data.iterrows()}

def generate_phonetics():
    word = input("Enter a word: ").upper()
    try:
        word_list = [phonetics[n] for n in word]
    except KeyError:
        print("Sorry!, Only letters are allowed.")
        generate_phonetics()
    else:
        print(word_list)
generate_phonetics()