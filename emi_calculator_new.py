def calculate_emi(principal, rate, tenure_months):
    r = rate / (12 * 100) 
    emi = (principal * r * (1 + r)**tenure_months) / ((1 + r)**tenure_months - 1)
    return round(emi, 2)

if __name__ == "__main__":
    principal = float(input("Enter loan amount (principal): "))
    rate = float(input("Enter annual interest rate (in %): "))
    tenure_months = int(input("Enter tenure (in months): "))

    emi = calculate_emi(principal, rate, tenure_months)
    print(f"Monthly EMI is: ₹{emi}")
