var1 = int(input("enter number: "))
var2 = int(input("enter number: "))
print("calkulator result")

def total(a,b):
    print("log----------------------")
    print(a)
    print(b)
    print("log----------------------")
    summa = ( a + b )/ 2
    return summa

print("Avarace: " + str(total(var1,var2)))