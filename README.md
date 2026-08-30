**PASSWORD TOOLKIT**
**Video Demo: https://youtu.be/Fq2y6VFcUtQ**
**Description:**

**Password Toolkit is a command-line program that combines two tools in one: a password strength checker and a random password generator. Both are designed to help users understand and improve their password security. The program runs as a simple menu-driven loop in the terminal. Users type Checker, Generator, or Quit to choose an action, and the program repeats until they quit.**

**Features**
**Password Strength Checker**

This tool uses 3 main functions that carry out different roles to deliver 3 separate messages to the user. These functions:-

- Analyze a password's length and character variety (uppercase, lowercase, digits, symbols) to assign a strength rating: Weak, Fair, Strong, or Very Strong.

- Cross-reference the password against a list of commonly used/breached passwords loaded from common\_passwords.txt. Any match is automatically rated "Weak," regardless of length or character variety, since these are the first passwords attackers try.

- Calculate the password's entropy (in bits), a measure of how many possible guesses an attacker would need in a brute-force search. This is translated into more user-friendly language (e.g. "Very Predictable," "Highly Unpredictable") so users don't need to interpret the raw number themselves. If the password is a known common password, its predictability label is forced to "Very Predictable," since entropy math alone doesn't account for password-list-based attacks.

**Password Generator**
This tool uses 3 main functions that carry out different roles to deliver  separate messages to the user. These functions:-

- Generate a random password of a user-specified length using Python's secrets module, which is designed for cryptographically secure random values (unlike the random module).

- Lets the user choose whether to include symbols in the generated password.

**Files**
project.py — contains all program logic, including main() and all supporting functions.
test_project.py — pytest unit tests for the core logic functions (check_strength, calculate_entropy, is_common_password).
common_passwords.txt — a list of commonly used passwords, used by the strength checker.

**Functions used**
check_strength(password) — returns a strength rating based on length, character variety, and common-password status.

calculate_entropy(password) — calculates the password's entropy in bits based on its character pool size and length.

describe_entropy(entropy, is_common) — converts a raw entropy value into a human-readable predictability label.

is_common_password(password) — checks whether a password appears in the loaded common password list.

load_common_passwords(filename) — reads common_passwords.txt into a set at program startup.

generate_password(length, use_symbols) — generates a random password using secrets.choice().

get_length() — prompts the user for a password length, validating that it's a usable integer.

ask_include_symbols() — prompts the user (y/n) on whether to include symbols in a generated password.

**A few choices worth explaining:**
I used ‘set’ instead of ‘list’ for the common passwords because membership checks are much faster on a set than a list, and the order of common passwords doesn't matter here, so a set is a better data structure to use.

Entropy calculations assume an attacker is guessing randomly across the full character pool. In reality, attackers try known/leaked passwords first. A password like “Password123” can have high theoretical entropy while still being one of the first guesses in a real attack, so the common-password check takes priority over the numeric score.

The random module is not cryptographically secure and shouldn't be used to generate anything security-sensitive, like passwords. secrets is part of the standard library and is designed specifically for this purpose.
