zoo_animals = ["pangolin", "cassowary", "sloth", "tiger"];
# One animal is missing!

print(len(zoo_animals))

if len(zoo_animals) > 3:
	print("The first animal at the zoo is the " + zoo_animals[0])
	print("The second animal at the zoo is the " + zoo_animals[1])
	print("The third animal at the zoo is the " + zoo_animals[2])
	print("The fourth animal at the zoo is the " + zoo_animals[3])


#index in lists

numbers = [5, 6, 7, 8]

print("Adding the numbers at indices 0 and 2...\n" + str(numbers[0] + numbers[2]))
print("Adding the numbers at indices 1 and 3...\n" + str(numbers[1] + numbers[3]))


# Last night our zoo's sloth brutally attacked 
#the poor tiger and ate it whole.

# The ferocious sloth has been replaced by a friendly hyena.
zoo_animals[2] = "hyena"

# What shall fill the void left by our dear departed tiger?
# Your code here!
zoo_animals[3] = "parrot"



"""Criando itens em uma lista, a lista em Python não tem um número determinado de itens, o comando append adiciona novos itens"""
suitcase = [] 
suitcase.append("sunglasses")

# Your code here!
suitcase.append("suncream")
suitcase.append("wallet")
suitcase.append("umbrella")

list_length = len(suitcase) # Set this to the length of suitcase

print("There are %d items in the suitcase." % (list_length))
print(suitcase)



letters = ['a', 'b', 'c', 'd', 'e']

# O comando abaixo signifca que será criado uma lista com o segundo item ate o terceiro item da lista acima
portion = letters[1:3]
print(portion)
print(letters)


suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]

first  = suitcase[0:2]  # The first and second items (index zero and one)
middle = suitcase[2:4]  # Third and fourth items (index two and three)
last   = suitcase[4:6]  # The last two items (index four and five)

print(suitcase)
print(first)
print(middle)
print(last)



animals = "catdogfrog"
cat  = animals[:3]   # The first three characters of animals (cria uma lista apenas com os 3 primeiros caracteres)
dog  = animals[3:6]  # The fourth through sixth characters (cria uma lista do quarto caractere até o sexto)
frog = animals[6:]   # From the seventh character to the end (cria uma lista a partir do setimo caractere)
print(animals)
print(cat)
print(dog)
print(frog)


animals = ["ant", "bat", "cat"]
print(animals.index("bat")) #imprime o numero do indice do animal "bat"
animals.insert(1, "dog")
print(animals)



animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck") # Use index() to find "duck"
print(animals)
print(duck_index)
# Your code here!
animals.insert(duck_index, "cobra")
print(animals) # Observe what prints after the insert operation



my_list = [1,9,3,8,5,7]
print(my_list)

for number in my_list:
    # Your code here
    print(2 * number)


"""Classificando uma lista"""
    
start_list = [5, 3, 1, 2, 4]
square_list = []

for x in start_list:
    square_list.append(x ** 2)
    
square_list.sort()

print(square_list)


##Removendo item da lista
beatles = ["john","paul","george","ringo","stuart"]
print(beatles)
beatles.remove("stuart")
print(beatles)
    


names = ["Adam","Alex","Mariah","Martine","Columbus"]
for item in names: 
    print(item)


a = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
for number in a:
    if number % 2 == 0:
        #Imprime o indice do numero par na lista a
        print("IDX %d - NUM %d" % (a.index(number), number))
       



doubles_by_3 = [x*2 for x in range(1,7) if (x*2) % 3 == 0]

# Complete the following line. Use the line above for help.
even_squares = [ x ** 2 for x in range(1,12) if x % 2 == 0]

print (doubles_by_3)
print (even_squares)

cubes_by_four = [ x ** 3 for x in range(1,11) if (x ** 3) % 4 == 0 ]

print (cubes_by_four)


l = [i ** 2 for i in range(1, 11)]
# Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print (l[2:9:2])
#l[start:end:stride]
#imprime [9, 25, 49, 81]

to_five = ['A', 'B', 'C', 'D', 'E']

print (to_five[3:])
# prints ['D', 'E'] 

print (to_five[:2])
# prints ['A', 'B']

print (to_five[::2])
# print ['A', 'C', 'E']

my_list = [x for x in range(1, 11)] # List of numbers 1 - 10

# Imprime todas os numeros impares da lista my_list
# Add your code below!
print (my_list[::2])

my_list_reverse = my_list[::-1]

print(my_list_reverse)

to_one_hundred = [x for x in range(101)]
# Add your code below!
backwards_by_tens = to_one_hundred[::-10]
print (backwards_by_tens)

threes_and_fives = [x for x in range( 1,  16) if x % 3 == 0 or x % 5 == 0  ]
