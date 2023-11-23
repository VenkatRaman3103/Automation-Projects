# Password Checker

## Overview

This Python script checks the security of a password by querying the [Have I Been Pwned](https://haveibeenpwned.com/) API. It calculates the SHA-1 hash of the password and checks if it has been compromised in previous data breaches.

## Usage

### Prerequisites

- Python 3.x
- `requests` library (install using `pip install requests`)

### Running the Script

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/password-checker.git
    cd password-checker
    ```

2. **Run the script:**

    ```bash
    python password_checker.py <password1> <password2> ...
    ```

    Replace `<password1>`, `<password2>`, etc., with the passwords you want to check.

## Functionality

The script performs the following steps:

1. Converts the password into a SHA-1 hash.
2. Queries the Have I Been Pwned API with the first five characters of the hash.
3. Checks if the remaining hash exists in the response, indicating if the password has been previously compromised.

## Example

    ```bash
    python password_checker.py mypassword secretp@ss 123456
    ```

## Output:

    ```bash
        5BAA61E4C9B93F3F0682250B6CF8331B7EE68FD8 was found 3355754 times.... do change the password
        secretp@ss was not found
        your password is strong
        25F9E794323B453885F5181F1B624D0B was not found
        your password is strong
    ```

# Dependencies

- requests