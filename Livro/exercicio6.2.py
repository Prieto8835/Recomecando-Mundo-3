a = []
b = []
c = []
a.append(input('Digite seu nome: '))
b.append(int(input('Digite sua idade: ')))
c.append(a[:])
c.append(b[:])
a.clear()
b.clear()
print(c)
