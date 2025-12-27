a = 10
b = 5
print(a&b)
print(a|b)
print(a^b)
print(~a)
print(~b)
print(a<<b)
print(b<<a)
print(a>>b)
print(b>>a)
num1 = int(input('Enter number: '))
c=1
if num1&c==0:
    print('Number is even.')
else:
    print('Number is odd.')
a=a^b
b=a^b
a=a^b
print(a)
print(b)