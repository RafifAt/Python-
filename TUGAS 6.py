print("="*40)
print("Price List Program")
print("="*40)
print("")
number_list = int (input("Please input number series = "))
ammount_price = int (input("Please input ammont price each item = "))
print("="*40)
print("Paper\t\tPrice(Rp.)")
print("="*40)
for i in range(1, number_list + 1):
    print(f"{i:<10}{i*ammount_price:>10}")