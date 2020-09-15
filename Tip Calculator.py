#Cameron Garrett Burns

#creates a variable to represent a specific number (the tip percentage)
percent_tip = .25


#creates the 'meal' variable with input for the user to put how much he/she spent
meal = float(input ("Please enter the cost of the meal: "))

#calculates how much the tip will be by multiplying the meal input with the given percent_tip of .25
tip = (meal * percent_tip)


#creates an execution to print "Sub-total: $" along with the meal cost
print ("Sub-total: $", (meal))

#creates an execution to print "Tip: $" along with the calculated tip
#"%.2f" creates a rule that rounds the calculation of the tip to 2 decimal places
print ("Tip: $", "%.2f" % (tip))

#creates an execution to print "Total: $" along with the total of the meal and tip cost, rounded two decimal places
print ("Total: $", "%.2f" % (meal + tip))


#allows the user to press enter to kill the  program
input ("Press 'Enter' to Exit")

#round(number, number_of_digits you want to round)
