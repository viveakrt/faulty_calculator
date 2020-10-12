  
print("Enter 1st number:")
num1 = int(input())
print("Enter the operator: (+,-,*,/,**,%)")
operator = input()
print("Enter 2nd number:")
num2 = int(input())

if num1==45 and num2 ==3 and operator =='*':
    print("555")
elif num1==56 and num2 ==9 and operator=='+':
    print('77')
elif num1==56 and num2==6 and operator=='/':
    print('4')
elif operator == '+':
    plus = num1+num2
    print('The ans is =',plus)
elif operator == '-':
    minus = num1-num2
    print('The ans is =',minus)
elif operator == '*':
    multi = num1*num2
    print('The ans is =',multi)
elif operator == '/':
    divide = num1/num2
    print('The ans is =',divide)
elif operator == '**':
    power = num1**num2
    print('The ans is =',power)
elif operator == '%':
    modulas = num1%num2
    print('The ans is =', modulas)
else:
    print("Error! Please check your input")
