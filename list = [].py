notas = []
for i in range (4):
    sem_notes = float(input(f"write the {i + 1}o number "))
    notas.append(sem_notes)
soma = sum(notas)
media = soma/4
print(f"your notes are {" , ".join(map(str, notas))}")
print(f"the average nubmers are {media} ")
print(f" you max note are {max(notas)}, and you lower are {min(notas)} ")

