money = input("Enter investment amount: ")
interest = input("Enter your interest rate: ")

money = float(money)
interest = float(interest) * .01

for i in range(10):
	money = money + (money * interest)
	print("Investment after 10 years : {:.2f}".format(money))
