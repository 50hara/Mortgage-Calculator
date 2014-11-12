def manualcalc():
	loanamt = input("How much will your home loan be for? ")
	interestyear = input("Enter your interest rate: ")/100.00
	interestmonth = interestyear/12
	years = input("How many years woudld you like to screwed for?")
	months = years*12
	topinterest = interestmonth*pow((1+interestmonth), months)
	bottominterest = pow((1+interestmonth), months) -1
	monthypmt = loanamt*(topinterest/bottominterest)
	print "Your monthly payments on your mortgage will be $%.2f for %s years " %(monthypmt,years)
	main() 

def autocalc():
	loanamt = input("How much will your home loan be for? ")
	interestyear = input("Enter your interest rate: ")/100.00
	interestmonth = interestyear/12
	for years in [10,20,30]:
		months = years * 12
		topinterest = interestmonth*pow((1+interestmonth), (months))
		bottominterest = pow((1+interestmonth), months) -1
		monthypmt = loanamt*(topinterest/bottominterest) 
		print "Years of Mortgage\t Monthly Payments\t"
		print "%s \t  %s \t\t\t\n " %(years,monthypmt)
	main()     

def main():
	print " Hello %s, welcome to your Mortgage monthly payment Calculator 1.0a " %(name)
	print " Here are your options: "
	print "\ta) Compare monthly payments on a 10, 20, and 30 year mortgage. " 
	print "\tb) See what your monthly payments will be for a specific year. "
	loan_options = raw_input("\n What would you like to do? (to quit type 'fuck this program') ")
	loan_options = loan_options.lower()
	if loan_options == "a":
		autocalc()
	elif loan_options == "fuck this program":
		exit()
	elif loan_options == "b":
		manualcalc()
	else: 
		print "That entry is incorrect. Try again. "
		main()


name = raw_input('Enter Your Name: ')
main()

# This function calculates the montly payment mortgage for a specific year. (based on user input)
