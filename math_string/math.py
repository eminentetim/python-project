while True:
	try:
		number = int(input("please enter a number : "))
		break
	except ValueError:
		print("You did not enter a number")
	except:
		print("An unknown error occurred")
print("Thank you for entering a number")

