dog = {}
dog["name"] = "Rio"
dog["breed"] = "German Shepard"
dog["legs"] = 4
dog["age"] = 3
print(dog)
student = {
    "first_name":"Muhammed",
    "last_name":"Alabi",
    "gender":"male",
    "age":23,
    "marital_status":"single",
    "skills":["Python","Java","HTML","CSS"],
    "country":"Nigeria",
    "city":"Ilorin",
    "address":"Gaa odota community, Ilorin, Nigeria"
}
print(len(student))
print(type(student["skills"]))
print(student["skills"])
student["skills"].append("PHP")
student["skills"].append(("GoLang"))
print(student["skills"])
print(student.keys())
print(
    student.values()
)
list_student = student.items()
print(list_student)
del student["age"]
print(student)
del student
print(student)
