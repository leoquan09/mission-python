#Formula is F = P * (1 + i)**t

def get_user_info():
    current_money = int(input('Enter current money in savings account: '))
    interest = int(input('Enter monthly interest rate: '))
    num_months = int(input('Enter number of months the money will be in the account: '))
    return current_money, interest, num_months

def calc_future_val(current, interest, num_months):
    return current * (1 + interest/100)**num_months

current, interest, num_months = get_user_info()
print(calc_future_val(current, interest, num_months))
