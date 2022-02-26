items_available_list=[{"item":"apple","qty":10,"cost":120},{"item":"orange","qty":9,"cost":80},{"item":"banana","qty":24,"cost":40},
                 {"item":"strawberry","qty":22,"cost":220},{"item":"kiwi","qty":12,"cost":140}]


def calculation():
    product=input("Enter the item required:")
    dict_count=0

    for dummy_dict in  items_available_list:
    #print(dummy_dict["item"])
        if product == dummy_dict["item"]:
            quantity=input("Enter the quantity required:")

            if int(quantity) <= int(dummy_dict["qty"]):
                product_cost = int(dummy_dict["cost"])*int(quantity)
                new_quantity= int(dummy_dict["qty"])-int(quantity)
                print(product_cost)
                print(new_quantity)
                items_available_list[dict_count]["qty"]=new_quantity
                dict_count=+1



            else:
                print("Insufficient quantity")

                #print("the product is available")
    checkout=input("Do you want to add cart to item :" )


calculation()



# print("the product is not available")
print(items_available_list)
items_required=[{"item":"apple","qty":8},{"item":"kiwi","qty":12}]
