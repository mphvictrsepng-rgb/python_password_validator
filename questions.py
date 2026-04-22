# --- QUESTION 1: THE BASIC GATEKEEPER ---
# 1. Ask for a password input.
# 2. If it's shorter than 6 characters, print "Too Short".
# 3. If it's "123456" OR "password", print "Too Simple".
# 4. Otherwise, print "Validating...".

password = input("Question 1 - Set a password: ")
# Write logic here:

# --- QUESTION 2: THE MULTI-FACTOR SIMULATION ---
# Ask for two inputs: a password (pwd) AND a "PIN" (as an integer).
# 1. If the password is "Admin" AND the PIN is 9999, print "Superuser Access".
# 2. If the password is "Admin" but the PIN is wrong, print "Invalid PIN".
# 3. If the password is wrong, print "Access Denied".

pwd = input("Question 2 - Enter Password: ")
pin = int(input("Question 2 - Enter 4-digit PIN: "))
# Write logic here:

# --- QUESTION 3: THE COMPLEXITY BOSS ---
# Rules for a "Master Password":
# 1. It must be between 10 and 20 characters long.
# 2. It must NOT contain the word "login" (in any case).
# 3. It must start with the character "!" or "@".
#
# If all 3 rules are met, print "Password Robust!".
# If any rule is failed, print "Weakness Detected".

master_pwd = input("Question 3 - Create Master Password: ")
# Write logic