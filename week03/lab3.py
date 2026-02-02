

# Question 1
grades = [85, 92, 78, 95, 88]

grades.append(90)
grades.sort()

print("Sorted grades:", grades)
print("Highest grade:", grades[-1])
print("Lowest grade:", grades[0])
print("Total number of grades:", len(grades))
print()

# Question 2
cart = ["apple", "banana", "milk", "bread", "apple", "eggs"]

print("Number of apples:", cart.count("apple"))
print("Position of milk:", cart.index("milk"))

cart.remove("apple")

removed_item = cart.pop()
print("Removed item using pop:", removed_item)

print("Is banana in cart?", "banana" in cart)
print("Final cart:", cart)
print()

# Question 3
point1 = (3, 5)
point2 = (7, 2)

print("Point 1:", point1)
print("Point 2:", point2)

x1, y1 = point1
x2, y2 = point2

print(f"x1 = {x1}, y1 = {y1}")
print(f"x2 = {x2}, y2 = {y2}")

distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print("Distance between points:", distance)

chars = tuple("PYTHON")
print("Characters tuple:", chars)

for ch in chars:
    print(ch)
print()

# Question 4
monday_class = {"Alice", "Bob", "Charlie", "Diana"}
wednesday_class = {"Bob", "Diana", "Eve", "Frank"}

monday_class.add("Grace")

print("Monday class:", monday_class)
print("Wednesday class:", wednesday_class)

print("Attended both classes:", monday_class & wednesday_class)
print("Attended either class:", monday_class | wednesday_class)
print("Only Monday:", monday_class - wednesday_class)
print("Only one class (not both):", monday_class ^ wednesday_class)

all_students = monday_class | wednesday_class
print("Is Monday subset of all students?", monday_class <= all_students)
print()

# Question 5
contacts = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9999",
}

print("Alice's number:", contacts["Alice"])

contacts["Diana"] = "555-4321"
print("Contacts after adding Diana:", contacts)

contacts["Bob"] = "555-0000"
print("Contacts after updating Bob:", contacts)

del contacts["Charlie"]
print("Contacts after deleting Charlie:", contacts)

print("All names:", contacts.keys())
print("All numbers:", contacts.values())
print("Total contacts:", len(contacts))
print()

# Question 6
inventory = {
    "Laptop": (999.99, 5),
    "Mouse": (29.99, 15),
    "Keyboard": (79.99, 10),
    "Monitor": (299.99, 8),
}

print("=== Current Inventory ===")
for name, (price, qty) in inventory.items():
    print(f"{name} - Price: ${price:.2f}, Quantity: {qty}")

electronics = {"Laptop", "Monitor"}
accessories = {"Mouse", "Keyboard"}

all_products = electronics | accessories
print("\nAll product categories:", all_products)

prices = []
for price, qty in inventory.values():
    prices.append(price)

print("\nPrice list:", prices)

prices.sort()
print("Sorted prices:", prices)
print(f"Lowest price: ${prices[0]:.2f}")
print(f"Highest price: ${prices[-1]:.2f}")

inventory["Headphones"] = (49.99, 20)

mouse_price = inventory["Mouse"][0]
inventory["Mouse"] = (mouse_price, 12)

if "Monitor" in inventory:
    del inventory["Monitor"]

print("\n=== Final Inventory ===")
for name, (price, qty) in inventory.items():
    print(f"{name} - Price: ${price:.2f}, Quantity: {qty}")