import pandas


def NATO_alph():
    try:
        user_word = input("What's the word? ").upper()
        words_list = [NATO[n] for n in user_word]
    except KeyError:
        print("Only letters")
        NATO_alph()
    else:
        print(words_list)
    finally:
        NATO_alph()


data = pandas.read_csv("nato_phonetic_alphabet.csv")
NATO = {row.letter: row.code for (index, row) in data.iterrows()}

NATO_alph()