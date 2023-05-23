#  כתוב תוכנית פייטון הקולטת מספר ומדפיסה את כל מחלקיו השלמים.
# לדוגמא עבור 20 יודפ ס-
# 10 ,5 ,4 ,2 ,1

n = []

try:
    m = int(input('enter number:'))
    for z in range(m-1,0,-1):
        if m%z==0:
            n.append(z)
    print(', '.join(str(i)  for i in n))
except ValueError:
    print('invalid number')
    exit(1)