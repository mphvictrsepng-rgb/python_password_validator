# --- QUESTION 1: THE BASIC GATEKEEPER ---

password = input('Question 1 - Set your password here: ')
if len(password) < 6:
    print('Too Short')
elif password == '123456' or password == 'password':
    print('Too Simple')
else:
    print('Validating...')

# Write logic here.
"""
The first thing I did was to ask the user for a password input.
Then I used an if statement to check if the length of the password is less than the 6 characters as required. If it is, I print "Too Short".
Next, I used an elif statement to check if the password is either "123456" or "password". If it is, I print "Too Simple".
Finally, if neither of those conditional tests are met or fail, I print "Validating...".
"""
