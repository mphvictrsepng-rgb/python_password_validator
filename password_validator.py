# --- QUESTION 1: THE BASIC GATEKEEPER ---
"""
password = input('Question 1 - Set your password here: ')
if len(password) < 6:
    print('Too Short')
elif password == '123456' or password == 'password':
    print('Too Simple')
else:
    print('Validating...')
"""

# Logic
"""
The first thing I did was to ask the user for a password input using the input() function. The value off the password is stored in the variable named password.
Then I used an if statement to check if the length of the password is less than the 6 characters as required. If it is, I print "Too Short".
Next, I used an elif statement to check if the password is either "123456" or "password". If it is, I print "Too Simple".
Finally, if neither of those conditional tests are met or fail, I print "Validating...".
"""
# --- QUESTION 2: THE MULTI-FACTOR SIMULATION ---

pwd = input("Question 2 - Enter Password: ")
pin = int(input("Question 2 - Enter 4-digit PIN: "))
if pwd == 'Admin' and pin == 9999:
    print('Superuser Access')
elif pwd == 'Admin' and pin != 9999:
    print('Invalid PIN')
else:
    print('Access Denied')

# Logic
"""
Here the first thing I did was to prompt the user to insert their passward (the value ( a string) is stored in the pwd variable) and then I asked them to insert their
PIN (the value (as an interger) is stored in the pin variable). Then I used the if statement to test if the password (pwd) matches 'Admin' as well as to check if
pin is equal to or matches '9999' using the and operator, as well as the == comparison operator to compare values against variables. 
If both of the conditions pass the test, then I print 'Supperuser Access'. 

Additionally, I used the elif statement to test if pwd is equal to 'Admin' but the pin is not equal to '9999' using the != comparison operator.
If the conditions pass the test, then I print 'Invalid PIN'. 
Lastly, I used the else statement to catch all other situations where the passwprd is wrong(not 'Admin') and pin is wrong (not '9999') and print out 'Access denied'.
"""
