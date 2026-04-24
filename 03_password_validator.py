# -- QUESTION 1: THE BASIC GATEKEEPER --

password = input('Question 1 - Set your password here: ')
if len(password) < 6:
    print('Too Short')
elif password == '123456' or password == 'password':
    print('Too Simple')
else:
    print('Validating...')

# My logic
"""
The first thing I did was to ask the user for a password input using the input() function. The value off the password is stored
 in the variable named password. Then I used an if statement to check if the length of the password is less than the 6 characters 
 as required. If it is, I print "Too Short". Next, I used an elif statement to check if the password is either "123456" or "password".
 If it is, I print "Too Simple".
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

# My logic
"""
Here the first thing I did was to prompt the user to insert their passward (the value ( a string) is stored in the pwd variable)
and then I asked them to insert their PIN (the value (as an interger) is stored in the pin variable). Then I used the if statement
 to test if the password (pwd) matches 'Admin' as well as to check if pin is equal to or matches '9999' using the and operator, as well 
 as the == comparison operator to compare values against variables. If both of the conditions pass the test, then I print 'Supperuser Access'. 

Additionally, I used the elif statement to test if pwd is equal to 'Admin' but the pin is not equal to '9999' using the != comparison operator.
If the conditions pass the test, then I print 'Invalid PIN'. Lastly, I used the else statement to catch all other situations where the
 passwprd is wrong(not 'Admin') and pin is wrong (not '9999') and print out 'Access denied'.
"""

# --- QUESTION 3: THE COMPLEXITY BOSS ---

master_pwd = input("Question 3 - Create Master Password: ")
#if len(master_pwd) >= 10 and len(master_pwd) <= 20:
requirements = [len(master_pwd) >= 10 and len(master_pwd) <= 20, 'login' not in master_pwd, master_pwd.startswith('!') or master_pwd.startswith('@')]
if all(requirements):
    print('Password Robust!')
else:
    print('Weakness Detected')

# My logic
"""
This one took me a while to figure it out. 
The first thing I did was to ask the user to create a master password using the input() function and store the value in the master_pwd 
variable. Then I tried to write an if statement for each of the 3 rules but I couldn't figure out how to do that for all the 3 rules
separately. Hence I decided to create a list called requirements and store all the 3 rules in that list. The firt thing I did in the
list was to check if the length of the master password is between 10 and 20 using len() function (>= 10 and <=20). The 2nd item in the
list is to check if the word 'login' is not in the master passowrd using the not in operator (if not in, condition is true and vice versa
if its in the master password, which would be false). The 3rd item in the list is to check if master password starts with "!" or "@" using
the startwith() methd; I used the or operator to check if neither of the condition is true. 

Finally, I used if staetemt to check if all the items in the requirements list are true using the all() function and if they are, I print
(Password robust!). I used the else statement to catch all other situations where the entered master password fails any of the 3 rules
 in the list, then the all() fucntion will return false and I print('Weakness Detected').
"""
