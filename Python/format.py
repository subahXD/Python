# String formatting
num1 = 50
num2 = 70
print(f"{num1+num2}")


username = "Subah"
roll = '23'
print(f"My name is {username} & my class roll is {roll}")

# binary type data (immutable)
subahlist =[1,45,88,99,100,111,150,178,200,210,230,255]
b= bytes(subahlist)
print(type(b))
 
# Binary type data byteArray (mutable)
subahlist =[1,45,88,99,100,111,150,178,200,210,230,255]
b1=bytearray(subahlist)
b1[1]=10
print(b1[1])

# none type data
X= None
print(type(X))
