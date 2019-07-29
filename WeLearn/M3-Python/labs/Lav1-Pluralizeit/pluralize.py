def pluralize(word):
    if word[-3:] == "ife":
        return word[:-3] + "ives"
    elif word [-2:] == "ch":
        return word[:-1] + "hes"
    elif word [-2:] == "us":
        return word[:-2] + "i"
    elif word[-1:] == "y":
        return word[:-1] + "ies"
    else:
        return word+'s'

number = int(raw_input("#: "))
the_word = raw_input("word:")

if number == 1:
    print ((str(number))+(" ")+(the_word))
else:
    print ((str(number))+(" ")+pluralize(the_word))
