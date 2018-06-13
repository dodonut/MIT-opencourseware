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
m = high


while able_to_pay:
    portion_saved = round(m/(annual_salary/12.0), 2)
    if portion_saved > 1 : portion_saved = 1
    while current_savings < down_payment and n_months < three_years:
        current_savings += (current_savings * r + portion_saved * annual_salary) / 12.0
        n_months += 1
        if n_months % 6 == 0:
            annual_salary += annual_salary * semi_annual_raise

    m = (low + high) / 2.0
    if current_savings < down_payment:
        able_to_pay = False
    elif n_months <

print("Number of months: ", n_months)
