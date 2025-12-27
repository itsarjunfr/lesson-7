x = 5
if type(x) is int:
    print('True')
else:
    print('False')
    
x = 20
y = 20
if x is y:
    print ('x and y same identity')

y=30
if x is not y:
    print('x and y different identity')