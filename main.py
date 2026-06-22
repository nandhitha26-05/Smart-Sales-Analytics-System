from db import conn
import mysql.connector
import pandas as pd

cursor = conn.cursor()

while True:
    print("\n----- Smart Sales Analytics -----")
    print("1. Add Product")
    print("2. View Products")
    print("3. Update Stock")
    print("4. Record Sale")
    print("5.Sales Report")
    print("6.Exit")

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
        product_id = int(input("Enter Product ID:"))
        quantity = int(input("Enter QuantitySold:"))
        query = """
        INSERT INTO sales(product_id,quantity)
        VALUES(%s,%s)
        """
        cursor.execute(query, (product_id,quantity))

        update_query = """
        UPDATE products 
        SET stock =stock - %s
        WHERE product_id = %s
        """
        cursor.execute(update_query,(quantity,product_id))

        conn.commit()

        print("Sale Recorded Successfully")   

    elif choice == "5":
        query = "SELECT * FROM sales"
        df = pd.read_sql(query,conn)

        print("\n===== SALES REPORT =====")
        print(df)

        print("\n===== TOTAL SALES BY PRODUCT =====")

        report = df.groupby("product_id")["quantity"].sum()

        print(report)

        top_product = report.idxmax()
        top_sales = report.max()

        print("\n===== TOP SELLING PRODUCT =====")
        print("Product ID:", top_product)
        print("Total sold:",top_sales)

    elif choice == "6":
        print("Thankyou") 
        break             

else:
    print("Invalid Choice")