from interestrate import app , InterestRate

with app.app_context():
    rates = InterestRate.query.all()
    
    if rates:
        print("Country | Interest Rate")
        print("-------------------------")
        for rate in rates:
            print(f"{rate.country} | {rate.interest_rate}")
    else:
        print("No interest rates found in the database.")