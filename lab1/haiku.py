a = input("Første raden:")
b = input("Andre raden:")
c = input("Tredje raden:")

La = len(a)
Lb = len(b)
Lc = len(c)
maximum = max(La, Lb, Lc)

da = maximum-La
db = maximum-Lb
dc = maximum-Lc

print("")
tb = "@"*(maximum+4)
print(tb)
print ("@"," "*da+a,"@")
print ("@"," "*db+b,"@")
print ("@"," "*dc+c,"@")
print(tb)
