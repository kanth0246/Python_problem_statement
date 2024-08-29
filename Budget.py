# Inputting the budget

Total_Budget = int(input('Enter the total budget of the month: '))
a=Total_Budget 

print("Total Budget is", a)

# Inputting the Food, Transportation, Entertainment, Other expenses
Food_Expense = int(input('Enter the food expense of the month: '))
b=Food_Expense
Running_Total_Expenses= b
print("Total Expenses till now: ", Running_Total_Expenses)
Transportation_Expense=int(input('Enter the Transportation of the month: '))
c=Transportation_Expense
Running_Total_Expenses= b+c
print("Total Expenses till now: ", Running_Total_Expenses)
Entertainment_Expense= int(input('Enter the Entertainment expense of the month: '))
d=Entertainment_Expense
Running_Total_Expenses= b+c+d
print("Total Expenses till now: ", Running_Total_Expenses)
Other_Expenses = int(input('Enter the Other expenses of the month: '))
e=Other_Expenses
Running_Total_Expenses= b+c+d+e
print("Total Expenses till now: ", Running_Total_Expenses)

#Calculating Remaining Expenses

Remaining_Budget= a-(b+c+d+e)


#Breakdown of Category
print("Food Expense: ",b)    
print("Transportation: ",c)
print("Entertainment: ",d)
print("Other Expense: ",e)

print("Total Budget for the month is: ", a)

print("Total Amount Spent so far: ", Running_Total_Expenses)

print("Remaining_Budget of the month is:",Remaining_Budget)



# Resetting the budget
    
Modified_Budget = int(input('Modify your budget of the month: '))

Remaining_Budget= Modified_Budget-(b+c+d+e)


print("Modified Budget for the month is: ", Modified_Budget)

print("Total Amount Spent so far: ", Running_Total_Expenses)

print("Remaining_Budget of the month is:",Remaining_Budget)

if (Running_Total_Expenses>Total_Budget or Running_Total_Expenses>Modified_Budget):
    print("Warning: Your Expenses are more than your Budget")
