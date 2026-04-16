# ---------------------------------------------------------
# PYTHON CHALLENGE: THE NET SALARY CALCULATOR (SARS 2026/27)
# ---------------------------------------------------------

# QUESTION 1: 
# Create three variables to get user input (floats):
# - monthly_gross_salary
monthly_gross_salary = float(input("Enter your monthly gross salary: "))
# - medical_aid_premium
medical_aid_premium = float(input("Enter your monthly medical aid premium: "))
# - num_dependents (for medical credits)
num_dependents = int(input("Enter the number of dependents for medical credits: "))
print("\nCalculating your net salary...\n")
print(f"Monthly Gross Salary: R{monthly_gross_salary:.2f}")
print(f"Medical Aid Premium: R{medical_aid_premium:.2f}")
print(f"Number of Dependents: {num_dependents}")

# QUESTION 2:
# Calculate the monthly UIF contribution. 
# Remember: It is 1% of gross salary, but it is capped at R177.12.
# Hint: Use an 'if' statement or the min() function.
uif_contribution = min(monthly_gross_salary * 0.01, 177.12)
print(f"Monthly UIF Contribution: R{uif_contribution:.2f}")


# QUESTION 3:
# To calculate tax (PAYE), we need the annual salary.
# Create a variable 'annual_gross' by multiplying monthly salary by 12.
paye = 0  # Initialize PAYE variable
annual_gross = monthly_gross_salary * 12
print(f"Annual Gross Salary: R{annual_gross:.2f}")


# QUESTION 4:
# Using the 2026/27 Tax Brackets, create an if/elif/else structure
# to calculate the 'base_tax' on the 'annual_gross'.
# Example: 
# If income <= 245100, tax is 18%.
# If income > 245100 and <= 383100, tax is 44118 + 26% of amount above 245100.
if annual_gross <= 245100:
    base_tax = annual_gross * 0.18
elif annual_gross <= 383100:
    base_tax = 44118 + (annual_gross - 245100) * 0.26
else:
    base_tax = 75585 + (annual_gross - 383100) * 0.31
print(f"Base Tax before rebates: R{base_tax:.2f}")



# QUESTION 5:
# Everyone gets a Primary Rebate of R17,820 per year.
# Subtract this rebate from your 'base_tax'. 
# Note: Tax cannot be less than zero!
primary_rebate = 17820
tax_after_rebate = max(base_tax - primary_rebate, 0)
print(f"Tax after Primary Rebate: R{tax_after_rebate:.2f}")


# QUESTION 6:
# Medical Tax Credits (MTC) reduce your tax.
# For 2026, the main member gets R376 off per month.
# Calculate the 'monthly_tax' by dividing annual tax by 12, 
# then subtract the R376 credit.
monthly_tax_before_credit = tax_after_rebate / 12
medical_tax_credit = 376
monthly_tax = max(monthly_tax_before_credit - medical_tax_credit, 0)
print(f"Monthly Tax before Medical Credit: R{monthly_tax_before_credit:.2f}")
print(f"Monthly Tax after Medical Credit: R{monthly_tax:.2f}")



# QUESTION 7:
# Final Step! Calculate the 'net_salary'.
# Formula: Gross - Monthly Tax - UIF - Medical Aid Premium.
net_salary = monthly_gross_salary - monthly_tax - uif_contribution - medical_aid_premium
print(f"Net Salary: R{net_salary:.2f}")



# QUESTION 8:
# Print a professional payslip showing:
# Gross Salary, UIF Deduction, Tax Paid, and the final Net Salary.
print("\n--- PAYSLIP ---")
print(f"Gross Salary: R{monthly_gross_salary:.2f}")
print(f"UIF Deduction: R{uif_contribution:.2f}")
print(f"Tax Paid: R{monthly_tax:.2f}")
print(f"Net Salary: R{net_salary:.2f}")
