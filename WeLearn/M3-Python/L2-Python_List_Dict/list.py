
students = ["Alice", "Javi", "Damien"]
students.append("Delilah")
print(students)

students = ["Alice", "Javi", "Damien"]
students.remove("Javi")
print(students)

students = ["Alice", "Javi", "Damien", "Javi"]
students.remove("Javi")
print(students)

smith_siblings = ["Emily", "Monique", "Giovanni"]
smith_siblings.append("Francis")
smith_siblings.append("Nate")
smith_siblings.append("Lawrence")
smith_siblings.append("Hunter")
for name in smith_siblings:
    print(name +" Smith")

smith_siblings = ["Emily", "Monique", "giovanni", "Brianna", "Javi"]
for index in range(len(smith_siblings)):
    smith_siblings[index] = smith_siblings[index] + " Smith"

print(smith_siblings)

superheroes = ["Captian Marvel", "Wonder Woman", "Storm", "Kamala Kahn", "Bumblebee", "Jessica Jones"]
print("Captian Marvel, Wonder Woman, Storm, Kamala Kahn, Bumblebee, Jessica Jones")
demoted_hero = str(raw_input("what superhero do you want to elimination from the top 5?"))

if demoted_hero in superheroes:
    superheroes.remove(demoted_hero)
    print("Top 5 heroes:", superheroes)
else:
    print("Hero not found")
names = ["Rickon", "Bran", "Arya", "Sansa", "Robb"]

print(names[::-1])


print(names[4:2:-1])
names = (names[::-1])
x = names
print(x)
