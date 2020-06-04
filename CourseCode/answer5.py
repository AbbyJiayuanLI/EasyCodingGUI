(i<101):\
    i = i+1\
    Sum = Sum + i@(i<=100):\
    i = i+1\
    Sum = Sum + i@(i<100):\
    i = i+1\
    Sum = Sum + i
@range(100):\
    Sum = Sum + i@range(101):\
    i=i+1\
    Sum = Sum + i@range(101):\
    Sum = Sum + i
@    Sum = Sum + i\
    if(i>=100):\
        break@    i = i+1\
    Sum = Sum + i\
    if(i>100):\
        break@    i = i+1\
    Sum = Sum + i\
    if(i>=100):\
        break
@y = 2 * x + 3\
print(y)\
y = function_y(2)\
y = function_y(3)@    y = 2 * x + 3\
    print(y)\
y = function_y(2)\
y = function_y(3)@    y = 2 * x + 3\
    print(y)\
    y = function_y(2)\
    y = function_y(3)
    