#Let the user input his/her current age and the age he/she wants to retire. Then calculate the number of years left until retirement
current_age= eval(input("Enter your current age: "))
retire_age= eval(input("Enter the age you want to retire: "))
years_left = retire_age - current_age
print("Number of years left until retirement: ", years_left)

#Let the user input how much money he/she wants to spend each year during the retirement. Then calculate the total amount of money needed for retirement
annual_spending = eval(input("Enter the amount of money you want to spend each year during retirement: "))
total_amount_needed = annual_spending /(0.04) 
#print the total amounte needed for retirement in the format of dollar sign and thousands comma
print(f"The total amount needed for retirement is: ${total_amount_needed:,.2f}")




