print("Event Shopping Cart")
store_locations = ("Sector 80", "Phase 7") 
prices = {"Banner": 500, "T-Shirt": 300, "Trophy": 800}
cart = ["Banner", "T-Shirt", "Banner"]
categories = {"Decor", "Merchandise", "Awards"} 
total_bill = 0
for item in cart:
    total_bill = total_bill + prices[item]
print(f"Available pick-up locations: {store_locations}")
print(f"Items in cart: {cart}")
print(f"Categories included: {categories}")
print(f"Total Bill: ₹{total_bill}")