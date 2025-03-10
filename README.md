Description

This Password Validator is a command-line application that guides users through creating a secure password. It enforces various password requirements to ensure passwords are robust against common attacks while being usable.
Features

Username-based validation (prevents using initials in password)
Length validation (8-12 characters)
Complexity requirements:

At least one uppercase letter
At least one lowercase letter
At least one number
At least one special character from: ! @ # $ % ^


Prohibits passwords that start with "pass" (case-insensitive)
Checks for character uniqueness (no repeated characters)
Interactive feedback with specific error messages for each failed check

How to Use

Run the script: python password_validator.py
Enter your first and last name when prompted
Enter your desired password
The program will check your password against all criteria
If your password fails any checks, you'll see specific error messages
Continue entering passwords until all criteria are met

Security Features

This validator enhances password security by:

Preventing dictionary attacks with complexity requirements
Stopping personal information usage (initials check)
Requiring varied character types
Enforcing minimum and maximum length rules
Preventing character repetition that could weaken passwords

Example
CopyEnter your first and last name: John Doe
Enter your desired password: password
Password must be between 8 and 12 characters
Password can't start with Pass
Password must contain at least 1 uppercase letter
Password must contain at least 1 special character: ! @ # $ % ^
These characters appear more than once:
a: 2 times
s: 2 times

Enter your desired password: Secure$1
Password must be between 8 and 12 characters

Enter your desired password: Secure$123
Password is valid and OK to use.
Requirements

Python 3.x
No external dependencies
