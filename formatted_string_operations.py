first_name = "muhammed"
last_name = "alabi"
language = "python"
formatted_string = "I am {} {}. I teach {}.".format(first_name,last_name,language)
print(formatted_string)
a = 4
b = 3
print("{} + {} = {}".format(a,b, a+b))
print(f"{a} + {b} = {a + b}")
print(language.upper())
challenge = "thirty days of python"
print(challenge.endswith("on"))
print(challenge.endswith("ion"))
print(challenge.rfind("y"))
print(challenge.index("da"))'''
'''print("Thirty" + " " + "Days" + " " + "of" + " " + "Python")
print("Coding" + " " + "For" + " " + "All")
company = "Coding For All"
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
print(company[0:7])
print(company.find("Coding"))
companyy = (company.replace("Coding", "Python"))
print(companyy)
print(companyy.replace("All","Everyone"))
print(company.split())
c = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(c.split(","))
print(company[0])
print(company.index("C"))
print(company.index("F"))
print(company.rfind("l"))
print("You cannot end a sentence with because because because is a conjuction".index("because"))
print("You cannot end a sentence with because because because is a conjuction".rindex("because"))
print("You cannot end a sentence with because because because is a conjuction"[31:54])
print(company.startswith("Coding"))
print(company.endswith("Coding"))
print("   Coding For All   ".strip())
print("30DaysOfPython".isidentifier())
print("thirty_days_of_python".isidentifier())
list_1 = ["Django","Flask","Bottle","Pyramid","falcon"]
print(" ".join(list_1))
print("I am enjoying this challenge" "\n" "I just wonder what is next")
print("Name""\t""Age""\t""Country""\t""City""\n""Muhammed""\t",23,"\t""Nigeria""\t""Ilorin")
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square")
a = 8
b = 6
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a/ b}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a//b}")
print(f"{a} ** {b} = {a ** b}")
