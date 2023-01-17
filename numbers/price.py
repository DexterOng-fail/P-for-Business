tot_price = float(input("input total price: "))
discount = float(input("enter discount: "))
disprice = tot_price*(discount/100)
final = tot_price - disprice
print("discount is ${}".format(disprice))
print("final price is ${}".format(final))