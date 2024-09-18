# Jill the Heckler

Jill the Heckler is a password cracker that uses a dictionary attack to crack passwords. Your task is to implement the entire program in Python, following the patterns and tools we have covered in class.

## Files

The following files are provided in this repository:

- `jill.py`: The main program file. This is where you will implement the password cracker.
- `passwords.txt`: A file containing usernames and hashed passwords.
- `dictionary.txt`: A file containing passwords to try.
- `test_jill.py`: A test file containing automated tests for the password cracker.

## Requirements

Your solution must adhere to the following requirements:

- Jill **must** accept two parameters: a file containing usernames and hashed passwords (in the format `username:hashed_password`), and a dictionary file containing passwords to try.
- Jill **must** run by executing `python3 jill.py <password_file> <dictionary_file>`.
- Jill **must** output the cracked passwords in the format `username:password` as they are cracked.
- Jill **must** use the `argparse` module to parse command line arguments.
- Jill **must** use the `hashlib` module to hash passwords in SHA-256 format.
- Jull **must not** output passwords that could not be cracked.
- Jill **should** iterate over every line in the dictionary file and compare the hashed password with the hashed passwords in the file.
- Jill **should** be tested using the `pytest` command.
- Jill **should** be properly documented using appropriate code comments.
- Jill **should** be tested using your own password and word lists.

## Hints

The following modules and functions **may** be helpful in your attempt to complete this project:

- `argparse.ArgumentParser`
- `hashlib.sha256()`
- `hashlib.hexdigest()`
- `file.open()`
- `file.readline()`
- `string.strip()`
- `string.split()`
- `string.encode()`