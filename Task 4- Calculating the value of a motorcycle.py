#program will work out how many years it will take for a motorcycle to depreciate in value to less than Â£1000.
currentyear = 0
currentvalue = 2000 #this variable tells you the price when it is purchased.

print("If I buy a motorcycle for £", currentvalue, "(Wow! That's a proper bargain!)")

while currentvalue > 1000: #the value of the motorcycle will be less than 1000
    
    currentvalue = currentvalue*0.9 #the motorcycle loses value by 10 percent
    currentyear = currentyear +1 #this shows that it loses value every year
    
if currentyear ==1:
    print ("After", currentyear, "year")
    print ("The motorcycle is worth £", currentvalue)
else:
    print("After", currentyear,"years")#calculates how many years it takes to drop below Â£1000
    print("The motorcycle is worth £", round(currentvalue,2)) 
#use round function to round up the answer to 2 d.p. to give the actual value in money.