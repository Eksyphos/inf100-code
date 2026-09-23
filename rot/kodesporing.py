balance = 1000
org_balance = balance

# første år: 5% rente
interest_rate = 0.05
interest_amount =balance*interest_rate
balance += interest_amount

#Andre år: 10% rente
interest_rate = 0.10
interest_amount = balance*interest_rate
balance += interest_amount

difference = balance-org_balance
print(f"Etter to år har du tjent {difference} kr i renter")