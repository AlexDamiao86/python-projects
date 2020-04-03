# Assigning a dictionary with three key-value pairs to residents:
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}

print(residents['Puffin']) # Prints Puffin's room number

# Your code here!
print(residents['Sloth'])
print(residents['Burmese Python'])



menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
print(menu['Chicken Alfredo'])

# Your code here: Add some dish-price pairs to menu!
menu['Chips'] = 4.50
menu['Fish and chips'] = 12.50
menu['Ceaser salad'] = 9.99
menu['Petit Gateau'] = 3.50

print("There are " + str(len(menu)) + " items on the menu.")
print(menu)



# key - animal_name : value - location 
zoo_animals = { 'Unicorn' : 'Cotton Candy House',
'Sloth' : 'Rainforest Exhibit',
'Bengal Tiger' : 'Jungle House',
'Atlantic Puffin' : 'Arctic Exhibit',
'Rockhopper Penguin' : 'Arctic Exhibit'}
# A dictionary (or list) declaration may break across multiple lines

print(zoo_animals)
# Removing the 'Unicorn' entry. (Unicorns are incredibly expensive.)
del zoo_animals['Unicorn']

# Your code here!
del zoo_animals['Sloth']
del zoo_animals['Bengal Tiger']

zoo_animals['Rockhopper Penguin'] = 'Atlantic sea water'

print(zoo_animals)




inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}
print("Impressao de inventory antes de alterações")
print(inventory)
# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 

# Your code here
# Inserindo uma chave chamada 'pocket' e atribuir uma lista para ela: 
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
# Classificando a lista backpack
inventory['backpack'].sort()
# Removendo o item 'dagger' da lista backpack
inventory['backpack'].remove("dagger")
# Adicionando 50 ao valor existente em 'gold'
inventory['gold'] += 50
print("Impressao de inventory depois de alterações")
print(inventory)
""" Não é possível a classificação de dicionario, apenas de elementos de uma lista
inventory.sort()  /// Não funciona
print("Impressao após a classificação do dicionario")
print(inventory)"""


webster = {
	"Aardvark" : "A star of a popular children's cartoon show.",
    "Baa" : "The sound a goat makes.",
    "Carpet": "Goes on the floor.",
    "Dab": "A small amount."
}

# Add your code below!
for entry in webster:
    print(webster[entry])




a = {}
a['a'] = 'alpha'
a['o'] = 'omega'
a['g'] = 'gamma'


print(a)

#Retorna os valores das chaves do dicionario
print(a.values())

#Retorna apenas as chaves do dicionario
print(a.keys())

#Obtem o valor de uma chave
print(a.get('o'))

#Caso nao encontrado o valor para essa chave retorna None
print(a.get('x'))

#Retorna o valor de uma chave
print(a['g'])

#Mostra o dicionario em formato de tuplas
print(a.items())

#De outra maneira
for tuple in a.items(): print (tuple)

#Quando tenta retornar o valor de uma chave nao existente sem o metodo get ocorre KeyError
## print(a['z'])




