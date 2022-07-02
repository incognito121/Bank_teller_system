checking_balance = 0
savings_balance = 0

def check_balance(account_type, checking_balance, savings_balance):
    if account_type == 'checking':
        balance = checking_balance
    elif account_type == 'savings':
        balance = savings_balance
    else: 
        return 'ERROR, please select checking or savings'
    
    balance_statement = 'Your ' + account_type + ' balance is ' + str(balance) + '.'
    return balance_statement

def make_deposit(account_type, amount, checking_balance, savings_balance):
    deposit_status = ''
    if amount > 0:
        if account_type == 'savings':
            savings_balance += amount
            deposit_status = 'successful'
        elif account_type == 'checking':
            checking_balance += amount
            deposit_status = 'successful'
        else:
            return 'error, please selct checking or savings for deposit'
    else:
        deposit_status = 'unsuccessful, please enter an amount greater than 0'
    deposit_statement = "Deposit of "+ str(amount) + " dollars to your " + account_type + " account was " + deposit_status + "."
    return savings_balance, checking_balance

def make_withdrawl(account_type, amount, checking_balance, savings_balance):
    withdrawl_status = ''
    fail = 'unsuccessful, please enter amount less than the balance'

    if account_type == "savings":
        if amount <= savings_balance:
            savings_balance -= amount
            withdrawal_status = "successful"
        else:
            withdrawal_status = fail
    elif account_type == "checking":
        if amount <= checking_balance:
            checking_balance -= amount
            withdrawal_status = "successful"
        else:
            withdrawal_status = fail
    else:
        return 'error, please try again'
    withdrawal_statement = "Withdrawal of "+ str(amount) + " from your " + account_type + " account was " + withdrawal_status + "."

    print(withdrawal_statement)
    return savings_balance, checking_balance

def acc_transfer(acc_from, acc_to, amount, checking_balance, savings_balance):
    transaction_staus = ''
    trans_error = 'unsuccessful transaction, please try again'
    if acc_from == "savings" and acc_to == "checking":
        if amount <= savings_balance:
            savings_balance -= amount
            checking_balance += amount
            transaction_status = "successful"
        else:
            transaction_status = trans_error + str(savings_balance)
    elif acc_from == "checking" and acc_to == "savings":
        if amount <= checking_balance:
            checking_balance -= amount
            savings_balance += amount
            transaction_status = "successful"
        else:
            transaction_status = trans_error + str(checking_balance)
    else:
        transaction_status = 'error'
    transaction_statement = "Transfer of "+ str(amount) + " from your " + acc_from + " to your "+ acc_to +" account was " + transaction_status + "."
    print(transaction_statement)
    return savings_balance, checking_balance