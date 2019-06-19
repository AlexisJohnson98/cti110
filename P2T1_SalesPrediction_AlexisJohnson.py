# This program will allow the user to enter project total sales and profit.
#6-18-2019
#CTI-110 P2T1 - Sales Prediction
#Alexis Johnson
#

# Find the projected total tales.
total_sales = float(input('Enter the projected sales: '))

# Calculate the profit as 23 percent of total sales.
profit = total_sales * 0.23

# Display the profit.
print('The profit is $', format(profit, ',.2f'))
