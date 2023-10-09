num1, num2 = input('Enter two number: ').split()

num1 = int(num1)
num2 = int(num2)

sum = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2
quot = num1 % num2

print('{} + {} = {}'.format( num1, num2, sum))
print('{} - {} = {}'.format( num1, num2, sub))
print('{} * {} = {}'.format( num1, num2, mul))
print('{} / {} = {}'.format( num1, num2, div))
print('{} % {} = {}'.format( num1, num2, quot))
