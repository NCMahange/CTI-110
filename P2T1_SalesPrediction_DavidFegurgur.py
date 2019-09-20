#Trying to get profit from projected sales
#18 Sep 2019
# CTI-110 P2T1 - Sales Prediction
#David Fegurgur





#Entering Projected Sales

TotalSales=float(input("Enter the projected sales:"))
print ("Projected Sales",TotalSales)

#Get Total Sales times profit

profit=TotalSales*0.23

#Show the total profit

print ("The Profit is $", format(profit,",.2f"))
