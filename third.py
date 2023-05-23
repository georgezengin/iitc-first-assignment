# כתוב תוכנית הקולטת מילים מהמשתמש, עד אשר המשתמש יקליד את אותה המילים פעמיים )לא
# בהכרח ברצף(
# לדוגמא:
# Please type a word: I
# Please type a word: Learn
# Please type a word: Python
# Please type a word: Learn
# You entered the work Learn twice. Good bye…

def wordcount(wrds, wd):
    n = sum(1 for w in words if w.lower() == wd.lower())
    return n

words = []
while True:
    w = input('Please type a word: ')
    words.append(w)
    n = wordcount(words,w)
    if n>2:
        print(f'"{w}" is repeated {n} time(s)')
        break

print('\nhasta la vista, baby!')

