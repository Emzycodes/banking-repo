# Simple Banking System

## Overview
The "Simple Banking System" is a Python class that simulates basic banking operations. It allows users to create bank accounts, make deposits, and check their account balances. This simple system serves as a foundation for understanding fundamental concepts in banking and account management.

## Features
**- Account Creation**: Users can create bank accounts with a specified account name and number.

**- Deposit Funds**: Account holders can deposit funds into their accounts.

**- Account Balance**: Check the account balance at any time.

## Usage

To use the Simple Banking System, follow these steps:

1. Create a bank account using the `BankAccount` class, providing an account name and number.
2. Deposit funds into the account using the `deposit` method.
3. Check the account balance using the `getbalance` method.

## Example

```python
# Create a bank account
my_account = BankAccount("John Doe", "1234567890")

# Deposit funds
my_account.deposit(1000)

# Check account balance
balance = my_account.getbalance()
print(f"Account Balance: ${balance}")

## License

This project is licensed under the [MIT License](LICENSE.md).

