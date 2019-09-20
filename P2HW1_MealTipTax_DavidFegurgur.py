#Enter the amount of tip you want to give the tax information and the cost of 
#the food. Show the total from all three
#18 Sep 2019
# CTI-110 P2HW1 - Meal Tip Tax Calculator
#David Fegurgur

print (" What is the cost for the amount of food you PIGGED out on:")
totalCostofFood= float(input())
    
#ENter the amount of tip

print ("How Much tip you going to give?,%")
tipPercentage= float( input())

tipAmount=(tipPercentage  / 100)*totalCostofFood
    
#Enter the tax

print ("What is the Sales Tax?,%")
taxPercentage = float (input())

taxAmount= (taxPercentage / 100) *totalCostofFood

#Calculate the total

total=totalCostofFood+tipAmount+taxAmount
print ("This is what you owe the Waiter $",total)






       







    
    
    
    
    
    
    
    
    
    
    
