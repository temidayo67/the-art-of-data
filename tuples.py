empty_tuple = ()
siblings_brothers = ("Abdulhamid","Moshood","Bolaji","Abdullah")
siblings_sisters = ("Asmau","Kehinde","Jelila","Azeemah")
siblings_total = siblings_brothers + siblings_sisters
print(len(siblings_total))
siblings_total = list(siblings_total)
siblings_total.append("Alabi")
siblings_total.append("Muhammed")
family_members = tuple(siblings_total)
print(family_members)
family_members = list(family_members)
siblings_1,siblings_2,siblings_3,siblings_4,siblings_5,siblings_6,siblings_7,siblings_8,father,mother = family_members
print(siblings_1)
print(siblings_2)
print(siblings_3)
print(siblings_4)
print(siblings_5)
print(siblings_6)
print(siblings_7)
print(siblings_8)
print(father)
print(mother)
fruits = ("Apple","Mango","Banana","Pineapple")
vegetables = ("Ewedu","Efo","Okra")
animal_products = ("Milk","Beef","Meat")
food_stuff_tp = fruits + vegetables + animal_products
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)
print(len(food_stuff_lt))
print(food_stuff_lt[4:6])
print(food_stuff_tp[4:6])
first_3_foods = food_stuff_lt[0:3]
last_3_foods = food_stuff_lt[7:]
print(f"first 3 items: {first_3_foods}")
print(f"last 3 items: {last_3_foods}")
del food_stuff_tp
nordic_country = ("Denmark","Finland","Iceland","Norway","Sweden")
print("Estonia" in nordic_country)
print("Iceland" in nordic_country)