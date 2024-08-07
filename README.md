# Account-Management-System
### Introduction to the Account Management System Project

In this project, we will be developing a Command-Line Interface (CLI) based account management system using Python. The system is designed to manage user accounts and provide a variety of financial operations. It will support two types of users: **Admin** and **Standard Users**.

#### Features for Standard Users:
1. **Deposit Amount**: Users can deposit money into their accounts.
2. **Check Balance**: Users can view their current account balance.
3. **Print Statement**: Users can generate and view a statement of their transactions.
4. **Transfer Amount**: Users can transfer money to other users within a set limit.
5. **Withdraw Amount**: Users can withdraw money from their accounts.
6. **Set/Change PIN Code**: Users can set or change their account PIN code, which will be securely encrypted.
7. **View Transaction History**: Users can view their past transactions.

#### Features for Admins:
1. **Create Account**: Admins can create new user accounts, ensuring that each account is unique.
2. **Show Details**: Admins can view the details of user accounts without seeing the encrypted PIN code.
3. **Show Transactions**: Admins can view the transaction history for all users or individual users.
4. **Delete Account**: Admins can delete a user's account from the system.
5. **Freeze Account**: Admins can freeze a user's account to prevent any further transactions.
6. **Set Transaction Limit**: Admins can set a transaction limit for users to control how much money can be transferred at once.
7. **Generate Reports**: Admins can generate reports showing the total cash-in and cash-out activities on a monthly, weekly, or yearly basis.

#### Security:
- **Encryption of PIN Code**: The system will ensure that the PIN codes used by users are securely encrypted using a hashing algorithm, preventing unauthorized access to sensitive information.

#### Objective:
This project aims to simulate a basic banking system that manages user accounts and transactions with a focus on security, ease of use, and administrative control. The CLI will provide a straightforward interface for performing these operations, making it a practical tool for learning Python and understanding the fundamentals of financial software systems.

This project will involve various Python concepts such as file handling, data structures (like dictionaries and lists), string manipulation, and encryption, making it a comprehensive learning experience.
