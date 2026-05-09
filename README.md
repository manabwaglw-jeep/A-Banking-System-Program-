Sure:

---

# Python Banking Program

A beginner-friendly command-line banking application built in Python. It simulates basic banking operations through an interactive menu with no external libraries required.

## Features

View your current account balance, deposit and withdraw funds with input validation, and overdraft protection. Simple and easy to read code, great for beginners.

## Getting Started

Make sure you have Python 3.x installed, then run:

```bash
python banking.py
```

## Project Structure

```
banking.py            # Main program (menu loop & logic)
banking_head.py       # Functions (show_balance, deposit, withdraw)
README.md             # Project documentation
```

banking.py imports all functions from banking_head.py using:

```python
from banking_head import *
```

## Example

```
____ BANKING PROGRAM ____
Enter 1 to show balance
Enter 2 to withdraw
Enter 3 to deposit
Enter 4 to exit

Enter your choice (1-4): 3
Enter the amount to deposit: $500.00
$500.00 has been deposited successfully.

Enter your choice (1-4): 1
Your current balance is: $500.00

Enter your choice (1-4): 4
Thank you! Have a nice day!
```
