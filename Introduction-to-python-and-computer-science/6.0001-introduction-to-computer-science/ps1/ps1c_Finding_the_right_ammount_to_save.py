portion_down_payment = 0.25
r = 0.04
total_cost = 1000000
semi_annual_raise = .07
current_savings = 0
three_years = 36
down_payment = total_cost * portion_down_payment

starter_salary = float(input("Enter your starting salary: "))
annual_salary = starter_salary

n_months = 0
n_steps = 0
able_to_pay = True
low = 0
high = 10000
epsilon = 100

while abs(down_payment - current_savings) > epsilon:
    current_savings = 0
    n_months = 0
    annual_salary = starter_salary
    m = (low + high) / 2.0
    portion_saved = round(m/(annual_salary/12.0), 4)
    while current_savings < down_payment and n_months < three_years:
        current_savings += (current_savings * r + portion_saved * annual_salary) / 12.0
        n_months += 1
        if n_months % 6 == 0:
            annual_salary += annual_salary * semi_annual_raise

    if current_savings < down_payment:
        low = m
    else:
        high = m
    n_steps += 1

if portion_saved > 1:
    print("It is not possible to pay the down payment in three years.")
else:
    print("Best savings rate: " , portion_saved)
    print("Steps in bisection search: ", n_steps)
