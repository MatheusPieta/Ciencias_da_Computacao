data=int(input('Digite a data!'))

D = data//10000
X = data%10000
M= X//100
A= X% 100

resultado= A*10000 + M*100 + D
print("A data fornecida no formato fica: ", "{foo:06d}".format(foo=resultado))
