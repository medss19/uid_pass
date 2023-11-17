# Secure User ID and Password Storage

Securely store user IDs and passwords with this simple Python script. The program ensures password strength and prevents the use of duplicate user IDs.

## How to Use

1. Run the script, and it will prompt you to enter a user ID.
2. If the entered user ID is unique, the script will prompt you to create a strong password.
3. The password must be at least 8 characters long and include a combination of alphabets, digits, and special characters.
4. Once a strong password is entered, the user ID and password combination will be stored securely.

## Password Strength Check

- The script checks for password strength by verifying the presence of alphabets, digits, and special characters.
- If the password is weak, the script prompts you to create a stronger password.

## Preventing Duplicate User IDs

- The script reads existing user IDs from a file ("sec.txt") and checks for duplicates.
- If the entered user ID is already in use, the script prompts you to choose another one.

## How to Run

1. Execute the script in a Python environment.
2. Follow the prompts to enter a user ID and create a strong password.

## Important Note

- Ensure that the "sec.txt" file is in the same directory as the script for proper functionality.

**Secure your user IDs and passwords with this straightforward Python script.**
