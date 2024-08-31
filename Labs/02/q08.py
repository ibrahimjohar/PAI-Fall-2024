#name: ibrahim johar farooqi
#date: 28 august 2024
#lab: 02
#task: 08

print("welcome to currency conversion programme!")
choice_currency = str(input("which currency would you like to convert? (USD, EUR, PKR, INR, YEN): "))   
amount = float(input("enter amount you want to convert: "))
convert_currency = str(input("which curreny would you like to convert this to? (USD, EUR, PKR, INR, YEN): "))

exchanges_rates_usd = {'EUR': 0.9, 'PKR':278.89, 'YEN': 146.21, 'INR': 83.89, 'USD': 1.0}

#convert to a base currency, like usd
usd_amount = amount / exchanges_rates_usd[choice_currency.upper()]
#convert to our required currency then
converted_amount = usd_amount * exchanges_rates_usd[convert_currency.upper()]

print(choice_currency.upper(), amount, " is ", convert_currency.upper(), converted_amount)
