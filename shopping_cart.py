import mysql.connector
import pandas as pd

# Read CSV and ensure price is Python float
goods = pd.read_csv("html/item.csv")
goods["price"] = goods["price"].astype(float)

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="260120",
    database="store"
)
cursor = db.cursor()

print(goods)

# Get buyer info
buyer = input("Enter your name: ")
number = input("Enter your number: ")  # Keep as string to match VARCHAR(10)

grand_total = 0
cart = []

while True:
    shop = input("Enter the item: ")

    # Check if item exists in CSV
    if shop not in goods["product"].values:
        print("Item not found. Please try again.")
        continue

    # Get price from dataframe and convert to Python float
    price = float(goods.loc[goods["product"] == shop, "price"].values[0])

    try:
        much = int(input("How much you want: "))
        if much <= 0:
            print("Quantity must be positive.")
            continue
    except ValueError:
        print("Please enter a valid number.")
        continue

    total = price * much
    grand_total += total

    cart.append((shop, much, price))  # save all info

    more = input("Want to shop more (yes/no): ").lower()
    if more == "no":
        print(f"Your total bill is {grand_total}")
        break

# Payment process
pay = input("Payment accept/decline: ").lower()

if pay == "accept":
    for item in cart:
        product, quantity, price = item

        # Ensure all are Python native types
        product = str(product)
        quantity = int(quantity)
        price = float(price)

        try:
            cursor.execute(
                "INSERT INTO st(name, number, product, quantity, price) VALUES (%s, %s, %s, %s, %s)",
                (str(buyer), str(number), product, quantity, price)
            )
        except mysql.connector.Error as err:
            print(f"Database error: {err}")

    db.commit()
    print("Payment successful! Items added to database.")
else:
    print("Come again if you have money.")

db.close()