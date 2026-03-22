# Shopping-Cart-Project-Python-MySQL-
## About
This project is a simple command-line shopping cart system written in Python that uses pandas and MySQL to manage purchases and store records.

The program allows a user to:
1. Enter their name and phone number.
2. Browse a list of available products (from a CSV file).
3. Add products to their cart specifying the quantity.
4. See the total bill for their purchases.
5. Confirm payment, after which all purchase details are saved in a MySQL database.

## Features
- Dynamic product pricing: Prices are read from a CSV file (```item.csv```) using ```pandas```.
- Cart system: Users can add multiple items before checkout.
- Total calculation: The program calculates the total bill automatically.
- Database storage: Successful purchases are inserted into a MySQL table st.
- Data safety: The program converts all NumPy types from pandas to native Python types to prevent errors when inserting into MySQL.
- Error handling: Checks for invalid item names and invalid quantities.

## Files
1. Python Code: ```shopping_cart.py```
 - This is the main program file.
 - Handles user input, calculates totals, and stores data in the database.
2. CSV File: ```item.csv``` (placed in html/ folder in this project)
 - Contains the product catalog and prices.
 - Example format:
   ```product,price
      Apple,20
      Banana,10
      Orange,15

3. SQL File: store.sql    
   - Contains the MySQL table creation query:

   ```CREATE DATABASE IF NOT EXISTS store;

      USE store;

      CREATE TABLE IF NOT EXISTS st (
      id INT AUTO_INCREMENT PRIMARY KEY,
      name VARCHAR(100),
      number VARCHAR(10),
      product VARCHAR(100),
      quantity INT,
      price DECIMAL(10,2)
      );  

## How It Works      
 1. Read products from CSV
   - Uses pandas to load ```item.csv```.
   - Ensures that price values are Python floats to avoid type errors when inserting into MySQL.
 2. User adds items to cart
   - The program asks for the product name and quantity.
   - Checks if the product exists in the CSV.
 3. Calculate total
   - Multiplies the quantity by the price of each product.
   - Keeps a running total (```grand_total```).
4. Payment confirmation
   - If the user confirms payment (```accept```), the program inserts each item in the cart into the MySQL table ```st```.
   - Each entry includes: ```name, number, product, quantity, price```.

5. Database insertion   
   - Converts all values to native Python types (```int, float, str```) before inserting to avoid ```_mysql_connector.MySQLInterfaceError```.

## Requirements 
 - Python 3.11+
 - ```pandas``` library
 - ```mysql-connector-python``` library
 - MySQL server installed and running
 - CSV file (```item.csv```) with product and price data

Install Python dependencies:
 ```pip install pandas mysql-connector-python```

 ## Notes
  - Make sure the MySQL server is running before running the Python program.
  - Adjust ```host, user, password```, and ```database``` in the Python code to match your MySQL setup.
  - The CSV file path is currently ```html/item.csv```. You can change this in the code if your file is elsewhere.


