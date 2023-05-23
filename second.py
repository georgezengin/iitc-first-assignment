#  כתוב תוכנית הקולטת מספרים חי וביים מהמשתמש עד אשר המשתמש יקליד מספר שלילי
# עבור כל מספר יוצג המספר הסידורי הנקלט. סכום המספרים והממוצע הנוכחי.
# לדוגמא:
# Please enter number #1 : 5
# Please enter number #2 (avg=5. Sum=5): 15
# Please enter number #3 (avg=10. Sum=20): -1
# Thank you. Goodbye.

i = 1
t = 0
while True:
    try:
        n = int(input(f'Please enter number #{i} '+(f'(avg={t//(i-1)}, sum={t})' if t>0 else '')+': '))
        if n < 0:
            break
        t += n
        i += 1
    except ValueError:
        print('invalid number, try again')
        continue

print('\nhasta la vista, baby!')

