def find_top_seller(products: dict, sales: dict) -> str:
    max_sum = 0
    top_product = ""
    
    for product in products:
        summa = products[product] * sales[product]

        if summa > max_sum:
            max_sum = summa
            top_product = product

    return top_product


print(find_top_seller(
    {"Olma": 5000, "Banan": 8000, "Uzum": 7000},
    {"Olma": 10,   "Banan": 5,    "Uzum": 8}
))