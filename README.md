# Banking Management System

## About the Project

The Banking Management System is a Python and MySQL based application designed to manage basic banking operations. It allows users to create and manage accounts, check balances, deposit money, withdraw money, and view transaction history.

## Features

* Create and manage bank accounts
* Check account balance
* Deposit money
* Withdraw money
* Store banking transactions
* View transaction history
* Input validation and error handling
* MySQL database connectivity

## Technologies Used

* Python
* MySQL
* MySQL Connector/Python

## Project Structure

```text
banking-system/
│
├── __init__.py
├── account.py
├── balance.py
├── config.py
├── db_setup.py
├── deposit.py
├── display.py
├── exceptions.py
├── history.py
├── main.py
├── requirements.txt
├── validators.py
└── withdraw.py
```

## How to Run

1. Install Python.
2. Install MySQL Server.
3. Install the required Python package:

```bash
pip install -r requirements.txt
```

4. Configure the MySQL database details in `config.py`.
5. Run the main program:

```bash
python main.py
```

## Main Operations

The system provides the following operations:

1. Create Account
2. Check Balance
3. Deposit Money
4. Withdraw Money
5. Transaction History
6. Exit

## Database

The project uses MySQL to store account information and transaction details.

## Author

NALLANIDIVYA
