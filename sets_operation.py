it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print(len(it_companies))
it_companies.add("Twitter")
print(it_companies)
it_companies.update(["Instagram","Whatsapp","Yahoo"])
print(it_companies)
it_companies.remove("Oracle")
print(it_companies)
C = A.union(B)
print(C)
D = A.intersection(B)
print(D)
print(A.issubset(B))
print(A.isdisjoint(B))
E = B.union(A)
F = C.union(E)
print(F)
print(A.symmetric_difference(B))
del A
del B
age = set(age)
print(age)
text = "I am a teacher and I love to inspire"
text_list = text.split(" ")
print(len(text_list))
