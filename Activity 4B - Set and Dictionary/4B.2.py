import csv

# Function to load currency rates from CSV file
def load_currency_rates(filename):
    currency_rates = {}

    with open(filename, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            currency_code = row['code']
            rate = float(row['rate'])
            currency_rates[currency_code] = rate

    return currency_rates

# Function to convert USD to the target currency
def convert_currency(usd_amount, target_currency, currency_rates):
    if target_currency in currency_rates:
        conversion_rate = currency_rates[target_currency]
        return usd_amount * conversion_rate
    else:
        print(f"Currency {target_currency} not found!")
        return None

# Main function to handle user input and currency conversion
def main():
    # Load the exchange rates from the CSV file
    filename = 'currency.csv'  # Make sure to set the correct path to your CSV file
    currency_rates = load_currency_rates(filename)

    # Get input from the user
    usd_amount = float(input("How much dollar do you have? "))
    target_currency = input("What currency you want to have? ").strip().upper()

    # Convert the currency
    converted_amount = convert_currency(usd_amount, target_currency, currency_rates)
    
    if converted_amount is not None:
        print(f"Dollar: {usd_amount} USD")
        print(f"{target_currency}: {converted_amount:.2f}")

if __name__ == "__main__":
    main()
