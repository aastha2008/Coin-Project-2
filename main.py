#Ask the user how many cents
cents=int(input("How many cents do you want: "))

#Find how many quarters needed
if(cents >= 25):
 quarters=cents // 25
 #print("The number of quarters are: " + str(quarters))
else:
 quarters=0
 #print("The number of quarters are: " + str(quarters))
#print("The number of quarters are: " + str(quarters))

#Find how many dimes needed
cents=cents-(25*quarters)
if(cents >= 10):
  dimes=cents // 10
else:
 dimes=0
#print("The number of dimes are: " + str(dimes))

#Find how many nickels needed
cents=cents-(10*dimes)
if(cents >= 5):
  nickels=cents // 5
else:
  nickels=0
#print("The number of nickels are: " + str(nickels))

#Find how many pennies needed
pennies=cents-(5*nickels)
#print("The number of pennies are: " + str(pennies))

print("The number of quarters are: " + str(quarters))
print("The number of dimes are: " + str(dimes))
print("The number of nickels are: " + str(nickels))
print("The number of pennies are: " + str(pennies))
