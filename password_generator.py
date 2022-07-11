
SYMBOLS = {'~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/'}
is_strong = False


def password_symbol_counter (password):
    symbol_number = 0
    for ch in password:
        if ch in SYMBOLS:
            symbol_number += 1
    return symbol_number


def password_upper_case_counter (password):
    upper_case_number = 0
    for ch in password:
        if ch.isupper():
            upper_case_number += 1
    return upper_case_number

#TEST TEST
def password_strenght(symbol, upper_case):
    if symbol > 2 and upper_case > 1:
        print("Your Password is very strong!")
    elif symbol > 1 and upper_case > 1:
        print("Your password is medium strong")
        global is_strong
        is_strong = True
        return is_strong
    else:
        print("Your password is not strong enought...")

#TEST TEST
while is_strong == False:
    password = input("Type your new password: \n")
    if len(password) < 9:
        print("Password should be at least 8 characters long")
    else:
        symbol_number = password_symbol_counter(password)
        upper_case_number = password_upper_case_counter(password)
        password_strenght(symbol_number, upper_case_number)
