var1 = int(input("enter number: "))
var2 = int(input("enter number: "))
print("calkulator result")

def total(a,b):
    print("Log-----------------")
    print(a)
    print(b)
    print("Log-----------------")
    summa = ( a + b )/ 2
    return summa

print("Total: " + str(total(var1,var2)))