
# Farmers Management System

This project is a web-based Farmers Management System developed using Flask, a Python web framework, and MySQL as the database. It allows for managing farmer details, agricultural products, and tracking changes through database triggers.

## Features

* **User Authentication:** Secure signup and login for users.
* **Farmer Management:**
    * Add new farmer details (name, Aadhar number, age, gender, phone, address, farming type).
    * View all registered farmers.
    * Edit existing farmer details.
    * Delete farmer records.
* **Agricultural Product Management:**
    * Add new agro products with details like product name, description, and price.
    * View available agro products.
* **Farming Type Management:** Add and manage different types of farming.
* **Database Triggers:** Automatically log insertions, updates, and deletions of farmer records.

## Technologies Used

* **Backend:** Flask (Python Web Framework)
* **Database:** MySQL
* **Database ORM:** Flask-SQLAlchemy
* **User Authentication:** Flask-Login
* **Password Hashing:** Werkzeug (Though the current implementation in `main.py` directly stores passwords, it's highly recommended to use `generate_password_hash` and `check_password_hash` for production.)
* **Database Management Tool:** phpMyAdmin (for initial database setup and management)

## Setup and Installation

Follow these steps to set up and run the project on your local machine.

### 1. Prerequisites

* **Python 3.x:** Make sure you have Python installed. You can download it from [python.org](https://www.python.org/).
* **MySQL Server:** Install MySQL. You can download it from [dev.mysql.com/downloads/mysql/](https://dev.mysql.com/downloads/mysql/).
* **phpMyAdmin (Optional but Recommended):** For easy database management, consider installing phpMyAdmin. You'll typically get this if you install a WAMP/XAMPP/MAMP stack.

### 2. Database Setup

1.  **Create Database:** Open your MySQL client (e.g., phpMyAdmin, MySQL Workbench, or command-line) and create a new database named `farmers`.
    ```sql
    CREATE DATABASE farmers;
    ```
2.  **Import SQL Schema:** Import the `farmers.sql` file into your newly created `farmers` database.
    * **Using phpMyAdmin:** Select the `farmers` database, go to the "Import" tab, and upload the `farmers.sql` file.
    * **Using MySQL Command Line:**
        ```bash
        mysql -u your_username -p farmers < farmers.sql
        ```
        (Replace `your_username` with your MySQL username.)

### 3. Project Setup

1.  **Clone the Repository:**
    ```bash
    git clone <your_repository_url>
    cd farmers-management-system # Or whatever your project folder is named
    ```
    (Replace `<your_repository_url>` with the actual URL of your GitHub repository.)

2.  **Create a Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    ```

3.  **Activate the Virtual Environment:**
    * **On Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
    * **On macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Install Dependencies:**
    ```bash
    pip install Flask Flask-SQLAlchemy Flask-Login Werkzeug
    ```

### 4. Configure Database Connection

Open `main.py` and ensure the database connection string is correct.
```python
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/farmers'
