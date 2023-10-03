"""
Name - Efe Udolu-Joshua
"""

from datetime import datetime
month = datetime.now().month
day = datetime.now().day
year = datetime.now().year

# Step 2 completed, code copied from assignment document

citizenship = input("Are you a Canadian citizen?: ")
residency = input("Are you a resident of Alberta?: ")
month_of_birth = int(input("Enter your birth month as a number: "))
day_of_birth = int(input("Enter your day of birth date: "))
year_of_birth = int(input("Enter your year of birth: "))

# Step 3 completed, assigned variables to user input
# For citizenship and residency, I did not convert the input type
# For birth month, birth day, and birth year, I converted the user's input into an integer


if citizenship != "yes" and citizenship != "no":
    print("Invalid response to citizenship.")
    exit()
elif residency != "yes" and residency != "no":
    print("Invalid response to residency.")
    exit()

# Step 4a completed
"""
Conditionals for citizenship and residency
If the input is not a yes or no answer
It is an invalid response
"""

if month_of_birth < 1 or month_of_birth > 12:
    print("Invalid month.")
    exit()
elif day_of_birth < 1 or day_of_birth > 31:
    print("Invalid day.")
    exit()
elif year_of_birth < 1900 or year_of_birth > 2023:
    print("Invalid year.")
    exit()
# Step 4b completed
"""
Conditionals for month of birth, day of birth and year of birth
If month of birth is not between 1 and 12, it is an invalid month
If day of birth is not between 1 and 31, it is an invalid day
If year of birth is not between 1900 and 2023, it is an invalid year
"""

if month_of_birth == 4 and day_of_birth == 31:
    print("Invalid birth date.")
    exit()
elif month_of_birth == 6 and day_of_birth == 31:
    print("Invalid birth date.")
    exit()
elif month_of_birth == 9 and day_of_birth == 31:
    print("Invalid birth date.")
    exit()
elif month_of_birth == 11 and day_of_birth == 31:
    print("Invalid birth date.")
    exit()
elif month_of_birth >= month and year_of_birth >= year and day_of_birth > day:
    print("Invalid birth date.")
    exit()
elif month_of_birth == 2 and day_of_birth == 29 and year_of_birth %4 != 0 or year_of_birth == 1900:
    print("Invalid birth date.")
    exit()
elif year_of_birth >= year-18 and month_of_birth >= month and day_of_birth > day:
    print("You are not eligible to vote.")
    exit()
elif citizenship == "no" or residency == "no":
    print("You are not eligible to vote.")
    exit()
elif citizenship == "yes" and residency == "yes" and year_of_birth <= year-18 and month_of_birth <= month and day_of_birth <= day:
    print("You are eligible to vote.")
    exit()
else:
    print("You are eligible to vote.")
    exit()
# Step 5 completed
# First four conditions are to prevent people from putting April, June, Spetember or November 31
# The next condition is to prevent people from putting birth dates in the future
# The next condition is to prevent people from putting Feb 29 on a non-leap year

# Step 6 completed
# The next condition checks if user is under 18, and if they are, they cannot vote
# I check if they are 18 by ensuring that their birthday at least 18 years from the current date
# I check if they are both a citizen and a resident, and if not, they are not eligible to vote
# If they are both a citizen and a resident, and they are at least 18 years old, they are eligible to vote
