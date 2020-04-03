"""
The string "PYTHON" has six characters,
numbered 0 to 5, as shown below:

+---+---+---+---+---+---+
| P | Y | T | H | O | N |
+---+---+---+---+---+---+
  0   1   2   3   4   5

So if you wanted "Y", you could just type
"PYTHON"[1] (always start counting from 0!)
"""
fifth_letter = "MONTY"[4]
print("The fifth letter of MONTY is:")
print(fifth_letter)


#The length function includes de blankspace as a character
#The result of length of the string below is 14
parrot = "Norwegian Blue"
print(len(parrot))
print(parrot.lower()) 
print(parrot.upper())


"""Declare and assign your variable on line 4,
then call your method on line 5!"""

pi = 3.14151692
print(str(pi))
print(pi)


ministry = "The Ministry of Silly Walks"

print(len(ministry)) 
print(ministry.upper())

# Print the concatenation of "Spam and eggs" on line 3!

print("Spam " + "and " + "eggs")


# Turn 3.14 into a string on line 3!

print("The value of pi is around " + str(3.14))

#The word Teste is printed on the line below to the next phrase
print("The value of pi is around 3.14\nTeste")

string_1 = "Camelot"
string_2 = "place"

print("Let's not go to %s. 'Tis a silly %s." % (string_1, string_2))

# The string below is broken. Fix it using the escape backslash!
print('This isn\'t flying, this is falling with style!')
# But there isn't any problem if you type this between parenthesis:
print ("This isn't flying, this is falling with style!")

"""

name = input("What is your name? ")
quest = input("What is your quest? ")
color = input("What is your favorite color? ")

print("Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color))


"""
#Gera um array de numberos com o comando split
numbers = "000;111;222;333".split(";")
print(numbers)
print("555;444;333".split(";"))

#Concatena um array em uma string com o delimitador informado 
numbers_string = '-'.join(numbers)
print(numbers_string)

string_3 = "The book is on the table"
print(string_3.find('book')) #retorna 4, posicao a partir de zero do inicio da palavra book
print(string_3.find('to')) #retorna -1, nao encontrado o texto -1
print(string_3.find('e')) #retorna 2, posicao a partir de zero da primeira ocorrencia da letra 'e'
print(string_3.find('t')) #retorna 15, posicao a partir de zero da palavra table, eh case sensitive
print(string_3.find('T')) #retorna 0, posicao a partir de zero da letra T

#Retira os espaços em branco do inicio e do fim da string
string_4 = "      Could you help me      ....      please       ?      "
s5 = string_4.strip()
print(s5)

print(string_4.startswith("Could")) #retona False quando nao começa com Could
print(s5.startswith("Could")) #retorna True quando começa com Could, case sensitive

print(string_4.endswith("?")) #retorna False quando nao termina com ?
print(s5.endswith("?")) #retorna True quando termina com ?




