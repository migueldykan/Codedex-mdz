gryffindor = 0
hufflepuff = 0
ravenclaw = 0
slytherin = 0

print('The Sorting Hat')

print('Pregunta 1) ¿Te gusta el amanecer o el anochecer?')

print('  1) amanecer')
print('  2) anochecer')

answer = int(input('Pon tu respuesta (1-2):'))

if answer == 1:
  gryffindor += 1
  ravenclaw += 1
elif answer == 2:
  hufflepuff += 1
  slytherin +=1
else:
  print('Error')

print("Pregunta 2) Cuando muera, quiero ser recordado como:")

print('  1) El bueno')
print('  2) El grande')
print('  3) El sabio')
print('  4) El audaz')

answer = int(input('Pon tu respuesta (1-4):'))

if answer == 1:
  hufflepuff += 1
elif answer == 2:
  slytherin +=1
elif answer == 3:
  ravenclaw +=1
elif answer == 4:
  gryffindor +=1
else:
  print('Error')

print('Pregunta 3) ¿Qué instrumento te gusta más oír')

print('  1) El violin')
print('  2) La trompeta')
print('  3) El piano')
print('  4) El tambor')

answer = int(input('Pon tu respuesta (1-4):'))

if answer == 1:
  slytherin +=1
elif answer == 2:
  hufflepuff +=1
elif answer == 3:
  ravenclaw +=1
elif answer == 4:
  gryffindor +=1
else:
  print('Error')

if gryffindor >= ravenclaw and gryffindor >= hufflepuff and gryffindor >= slytherin:
  print('Your house is Gryffindor!')
elif ravenclaw >= hufflepuff and ravenclaw >= slytherin:
  print('Your house is Ravenclaw!')
elif hufflepuff >= slytherin:
  print('Your house is Hufflepuff!')
else:
  print('Your house is Slytherin!')