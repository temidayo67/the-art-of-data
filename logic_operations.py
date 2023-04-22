age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to drive")
else:
    print(f"Please wait {18 - age} years to drive")

my_age = 23
your_age = int(input("Enter your age: "))
if my_age > your_age:
    print("I am older than you")
    if my_age - your_age == 1:
        print(f"I am {my_age - your_age} year older than you")
    elif (my_age - your_age) > 1:
        print(f"I am {my_age - your_age} years older than you")
elif your_age > my_age:
    print("You are older than me")
    if (your_age - my_age) == 1:
        print(f"You are {your_age - my_age} year older than me")
    elif (your_age - my_age) > 1:
        print(f"You are {your_age - my_age} years older than me")
num_1 = int(input("Enter number one: "))
num_2 = int(input("Enter number two: "))
if num_1 > num_2:
    print("A is greater than B")
elif num_1 < num_2:
    print(("A is smaller than B"))
else:
    print("A is equal to B")
score = int(input("Enter score: "))
if score >= 80 and score <= 100:
    print("A")
elif score >=70 and score < 80:
    print("B")
elif score >= 60 and score < 70:
    print("C")
elif score >= 50 and score < 60:
    print("D")
else:
    print("F")
month = str(input("Enter month: "))
if month == "September" or month == "October" or month == "November":
    print("The season is Autumn")
elif month == "December" or month == "January" or month == "February":
    print("The season is Winter")
elif month == "March" or month == "April" or month == "May":
    print("The season is Spring")
elif month == "June" or month == "July" or month == "August":
    print("The season is Summer")

fruits = ['banana', 'orange', 'mango', 'lemon']
if "pineapple" in fruits:
    print("Fruit already exist")
else:
    fruits.append("pineapple")
print(fruits)
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if 'skills' in person:
    print((person['skills'][2]))
    print('Python' in person['skills'])
else:
    print("Ignore")

if person['skills']  == ['JavaScript', 'React']:
    print('He is a front end developer')
elif 'Node'and'Python'and 'MongoDB' in person['skills']:
    print('He is a backend developer')
elif 'React'and 'Node'and 'MongoDB' in person['skills']:
    print('He is a full stack developer')
else:
    print('unknown title')

if person['is_marred'] == True and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married")
