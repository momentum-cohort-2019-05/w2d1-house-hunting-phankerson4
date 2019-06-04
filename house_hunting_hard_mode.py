annual_salary = int(input("What is your annual salary? "))
portion_saved = float(input("What percent of salary will you save? "))
r = float(input("What is the rate of return?"))
total_cost = int(input("What is the total cost of your dream home? "))
portion_down_payment = float(input("What is down payment percent?"))
down_payment_amount_needed=portion_down_payment*total_cost
current_savings = 0

monthly_savings = annual_salary/12
number_of_months = 0







while current_savings < down_payment_amount_needed:
  current_savings += current_savings * r/12
  current_savings += portion_saved*monthly_savings
  number_of_months += 1
print('Number of months:', number_of_months)

    

    
    
    

  
