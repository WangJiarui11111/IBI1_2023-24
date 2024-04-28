def number_of_chocolate_bars(total_money, price):  
    # Calculate the number of bars that user is able to afford
    number_of_bars = total_money // price  
    # Calculate the change left over  
    change = total_money % price  
    return number_of_bars, change  
# For Example: 
total_money = 100
price = 7   
bars, change = number_of_chocolate_bars(total_money, price)  
# Print the result  
print(f"The user can afford {bars} chocolate bars and will have {change} left over.")  