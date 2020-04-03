loop_condition = True

while loop_condition:
    print ("I am a loop")
    loop_condition = False

count = 0

while count < 5:
    print("Loop %d" % count)
    count += 1

num = 1

while num <= 10:
    print("%d ^ 2 = %d" % (num, num ** 2) )
    num += 1


choice = input('Enjoying the course? (y/n)')


"""Tabela Verdade E
v E v = V
V E f = f
f E v = f
f E f = f
"""


while (choice != 'y' \
   and choice != 'Y' \
   and choice != 'n' \
   and choice != 'N'):  # Fill in the condition (before the colon)
    choice = input("Sorry, I didn't catch that. Enter again: ")


count = 0

while True:
    print(count)
    count += 1
    if count >= 10:
        break    ## Comando de saida do loop



import random

print ("Lucky Numbers! 3 numbers will be generated.")
print ("If one of them is a '5', you lose!")

count = 0
while count < 3:
    num = random.randint(1, 6) #necessario importar o arquivo random
    print (num)
    if num == 5:
        print ("Sorry, you lose!")
        break
    count += 1
else:  #o else do while eh executado sempre que nao eh atingido a condição do loop ou
#após a execução do loop sem saída por break
    print ("You win!")

# Generates a number from 1 through 10 inclusive
random_number = random.randint(1, 10)

guesses_left = 3
print(random_number)
# Start your game!
while guesses_left > 0:
    guess = int(input("Your guess: "))
    if guess == random_number:
        print ('You win!')
        break
    
    guesses_left -= 1
else:
    print ('You lose.')

""" Loop com FOR"""

print ("Counting...")

for i in range(20):
    print (i)

hobbies = []
# Adiciona 3 hobbies em uma lista
# Add your code below!
for i in range(3):
    hobby = input("Your hobby: ")
    hobbies.append(hobby)


word = "eggs!"

# Your code here!
for char in word:
    print (char)



phrase = "A bird in the hand..."

# Add your for loop
for char in phrase:
    if char == 'A' or char == 'a':
        print ('X',) # A virgula após a string significa que o print continuará na mesma linha, porém não funcionou neste compilador
    else:
        print (char,)


#Don't delete this print statement!
print



choices = ['pizza', 'pasta', 'salad', 'nachos']

print ('Your choices are:')
for index, item in enumerate(choices): #Index e item sendo iterados
    print (index + 1, item)


"""Loop em multiplas listas
Bem interessante!!
o comando zip cria um conjunto de elementos quando passados varias listas e irá parar no fim da lista mais curta
"""

list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
    # Add your code here!
    if a > b:
        print (a)
    else:
        print (b)



fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print ('You have...')
for f in fruits:
    if f == 'tomato':
        print ('A tomato is not a fruit!') # (It actually is.)
        break
    print ('A', f)
else: #O else só eh executado se o for terminar com sucesso, sem finalizar com o break
    print ('A fine selection of fruits!')
