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