#pi.py

def gregoryLeibnizSeries():
	pi = 0
	currentOdd = 1

	for x in range(500000):
		pi = pi + 4/currentOdd
		currentOdd+=2
		pi = pi - 4/currentOdd
		currentOdd+=2

	return pi

def baileyBorweinPlouffe(n):
	pi=0
	for k in range(10000):
		pi = pi + ((1/16**k)*((4/(8*k+1)) - (2/(8*k+4)) - (1/(8*k+5)) - (1/(8*k+6))))
	return pi

def shell():
	print('Which method do you want to use to calculate pi:')
	print('1. Gregory Leibniz Series')
	choice = input("")

	if choice == "1":
		pi = gregoryLeibnizSeries()
		print(pi)
	elif choice == "2":
		pi=baileyBorweinPlouffe(10)
		print(pi)
	else:
		print("Not a valid choice.")


if __name__ =='__main__':
	shell()