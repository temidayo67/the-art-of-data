first_name = "Muhammed"
last_name = "Alabi"
country = "Nigeria"
city = "Ilorin"
age = 23
is_married = True
skills = ["Python", "Pandas", "Numpy", "Data Extraction"]
person_info = {
    "firstname":"Muhammed",
    "lastname":"Alabi",
    "country":"Nigeria",
    "city":"ilorin"
}
print("Hello World!")
print("First name:",first_name)
print("First name length:",len(first_name))
print("Last name:",last_name)
print("Last name length:",len(last_name))
print("Country:",country)
print("City:",city)
print("Age:",age)
print("Married:", is_married)
print("Skills:",skills)
print("person information:", person_info)

first_name, last_name, country, city, is_married,age = "Muhammed","Alabi","Nigeria","Ilorin",True,25
print(first_name,last_name,country,city,is_married)
print("First name:",first_name)
print("First name length:",len(first_name))
print("Last name:",last_name)
print("Last name length:",len(last_name))
print("Country:",country)
print("City:",city)
print("Age:",age)
print("Married:", is_married)


print(len(first_name),len(last_name))
print(type(first_name))
print(type(age))
print(type(1.2))
num_one = 5
num_two = 4
diff = num_one - num_two
print(f"{num_one} minus {num_two} is:",diff)
mult = num_one * num_two
print(f"{num_one} multiplied by {num_two} is:",mult)
div = num_one/num_two
divv = divmod(num_one,num_two)
divvv = num_one%num_two
print(divv)
print(f"{num_one} divided by {num_two} is:",div,"remainder",divvv)
poww = num_one**num_two
print(f"{num_one} raised to the power of {num_two} is:",poww)
floor_division = num_one//num_two
print(floor_division)
r = int(input("radius: "))
area_of_circle = (3.14) * (r**2)
print(area_of_circle)
help("keyword")
