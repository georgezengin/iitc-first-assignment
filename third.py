# כתוב תוכנית הקולטת מילים מהמשתמש, עד אשר המשתמש יקליד את אותה המילים פעמיים )לא
# בהכרח ברצף(
# לדוגמא:
# Please type a word: I
# Please type a word: Learn
# Please type a word: Python
# Please type a word: Learn
# You entered the work Learn twice. Good bye…

words = []
while True:
    try:
        maxtimes = int(input('Enter max number of times: '))
        if maxtimes > 0:
            break
        if maxtimes < 0:
            exit(0)
    except ValueError:
        print('*** Error *** Invalid number of times, try again ***')


while True:
    w = input('Please type a word: ')
    words.append(w.lower())
    n = words.count(w.lower())
    if n >= maxtimes:
        print(f'You entered the word "{w}" {n} time'+('s' if n > 1 else ''))
        break

print('\nhasta la vista, baby!')

