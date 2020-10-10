print("Enter 1st number:")
num1 = int(input())
print("Enter the operator: (+,-,*,/,**,%)")
operator = input()
print("Enter 2nd number:")
num2 = int(input())

if operator == '+':
    plus = num1+num2
    print('The ans is =',plus)
elif operator == '-':
    minus = num1-num2
    print('The ans is =',minus)
elif operator == '*':
    multi = num1*num2
    print('The ans is =',multi)
elif operator == '/':
    devide = num1/num2
    print('The ans is =',devide)
elif operator == '**':
    power = num1**num2
    print('The ans is =',power)
elif operator == '%':
    modulas = num1%num2
    print('The ans is =', modulas)
else:
    print("Error! Please check your input")
