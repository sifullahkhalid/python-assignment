def calculator(customer_name,product_1_name,product_1,product_2_name,product_2,product_3_name,product_3):
        sub_total = int(product_1+product_2+product_3)
        print(f"Customer Name: {customer_name}")
        print(f"\n\nProduct 1: {product_1_name}")
        print(f"Price: {product_1}")
        print(f"\n\nProduct 2: {product_2_name}")
        print(f"Price: {product_2}")
        print(f"\n\nProduct 3: {product_3_name}")
        print(f"Price: {product_3}")
        print(f"\n\nSubtotal: {sub_total}")

        if sub_total >= 5000 :
                discount = int(sub_total*20)/100
                final_total = int(sub_total - discount)
                print(f"Discount: {discount}")
                print(f"Final Total:: {final_total}")
        elif sub_total < 5000 and sub_total>=3000:
                discount = (sub_total*10)/100
                final_total = sub_total - discount
                print(f"Discount: {discount}")
                print(f"Final Total:: {final_total}")
        elif sub_total < 3000 and sub_total>=1000:
                discount = (sub_total*5)/100
                final_total = sub_total - discount
                print(f"Discount: {discount}")
                print(f"Final Total:: {final_total}")
        else:
                print(f"Discount: No discount")
                print(f"Final Total:: {sub_total}")

       
customer_name = str(input("Enter Customer Name : "))
product_1_name,product_1 = str(input("Enter 1st Product name : ")),int(input("Enter 1st Product Price : "))
product_2_name,product_2 = str(input("Enter 2nd Product name : ")),int(input("Enter 2nd Product Price : "))
product_3_name,product_3 = str(input("Enter 3rd Product name : ")),int(input("Enter 3rd Product Price : "))


calculator(customer_name,product_1_name,product_1,product_2_name,product_2,product_3_name,product_3)