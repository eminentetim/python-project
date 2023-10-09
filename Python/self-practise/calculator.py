num1 , operator, num2 = input('enter calculation: ').split()

# convert num to integer

num1 = int(num1)
num2 = int(num2)

if operator == "+":
	print('{} + {} = {}'.format( num1, num2, num1+num2))
elif operator == "-":
	print('{} - {} = {}'.format( num1, num2, num1-num2))
elif operator == "*":
	print('{} * {} = {}'.format( num1, num2, num1*num2))
elif operator == "/":
	print('{} / {} = {}'.format( num1, num2, num1/num2))
elif operator == "%":
	print('{} % {} = {}'.format( num1, num2, num1%num2))
else:
	print('use +, -, *, / or % next time')

