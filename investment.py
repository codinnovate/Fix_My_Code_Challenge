investment_amount = input('Enter Investment Amount');
expected_interest = input('Enter Interest Amount')
investment_amount.float()
expected_interest.float()
for i in range(0, 10):
    investment_amount = investment_amount + investment_amount * expected_interest
    print(investment_amount)