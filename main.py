from db import conn
import mysql.connector

cursor = conn.cursor()

while True:
    print("\n----- Smart Sales Analytics -----")
    print("1. Add Product")
    print("2. View Products")
    print("3. Update Stock")
    print("4.Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter Product Name: ")
        price = float(input("Enter Price: "))
        stock = int(input("Enter Stock: "))

        query = """
        INSERT INTO products(product_name, price, stock)
        VALUES (%s, %s, %s)
        """

        cursor.execute(query, (name, price, stock))
        conn.commit()

        print("Product Added Successfully")

    elif choice == "2":

        cursor.execute("SELECT * FROM products")

        rows = cursor.fetchall()

        print("\nProducts List")

        for row in rows:
            print(row)

    elif choice == "3":

      product_id = int(input("Enter Product ID: "))
      stock = int(input("Enter New Stock: "))

      query = """
      UPDATE products
      SET stock=%s
      WHERE product_id=%s
      """

      cursor.execute(query, (stock, product_id))
      conn.commit()

      print("Stock Updated Successfully")

    elif choice == "4":
        print("Thank You")
        break

else:
    print("Invalid Choice")