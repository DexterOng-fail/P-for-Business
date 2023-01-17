#1
fruits_order = { "apple" : 200, "orange": 150, "papaya": 50, "pineapple" : 45.}
fruits_order["durian"] = 300
#print(fruits_order)

print(fruits_order.get("papaya"))
print(fruits_order["papaya"])

if "durian" in fruits_order.keys():
    fruits_order["durian"] = 100

for fruits, key in fruits_order.items():
    print(f'{fruits} order: {key}')

for fruits, key in fruits_order.items():
    if key< 100:
        print(f"urgent order: {fruits}")
total_quantity = []
total_quantity = fruits_order.values()
print(sum(total_quantity))

business_data = [['Armchair', 120000, 85000], ['Dining Table', 180000, 100000], ['Bed', 230000, 140000]]
def total_function(option):
    total  = 0
    if option == "revenue":
        for i in business_data:
            total += (i[1])
    elif option == "cost":
        for i in business_data:
            total += (i[2])
    else:
        return("invalid input")
    return(total)
print(total_function("cost"))