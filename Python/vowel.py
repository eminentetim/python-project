string = input("enter string:")

vowels = 'aeiouAEIOU'
count = 0
for char in string:
	if char in vowels:
		count += 1
print(count)
