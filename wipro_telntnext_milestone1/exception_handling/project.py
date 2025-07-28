# You had saved the items and their price details in a text file, which you purchased yesterday from a nearby super market.
# You need to know:
# 1. How many items did you purchase?
# 2. How many items are free?
# 3. What is the total amount you had to pay?
# 4. What is the discount amount?
# 5. What is the final amount did you pay after the discount?
# Help yourself by writing a python code to do this. Include necessary code to handle the possible exceptions.
# Note:
# Data is stored in a text file Purchase-1.txt.
# Each line contains one item's details.
# Item name and price is separated by a space.
# You have to enter the file name during run time.

filename = input("Enter the file name: ")

try:
    with open(filename, 'r') as file:
        lines = file.readlines()

    total_items = len(lines)
    free_items = 0
    total_amount = 0.0

    for line in lines:
        parts = line.strip().split()
        if len(parts) < 2:
            continue
        item_name, price_str = parts[0], parts[1]
        try:
            price = float(price_str)
            if price == 0:
                free_items += 1
            total_amount += price
        except ValueError:
            print(f"Warning: Invalid price '{price_str}' for item '{item_name}', skipping.")

    discount = 0.10 * total_amount  # Assuming 10% discount
    final_amount = total_amount - discount

    print("Total items purchased:", total_items)
    print("Number of free items:", free_items)
    print("Total amount to pay:", total_amount)
    print("Discount amount:", discount)
    print("Final amount after discount:", final_amount)

except FileNotFoundError:
    print("Error: File not found")
except Exception as e:
    print("An error occurred:", e)
