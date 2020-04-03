
def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False


def is_int(x): 
    if x < 0: 
        x *= -1
    dif = x - int(x)
    if dif > 0:
        return False
    else:
        return True


def digit_sum(x):
    total = 0
    sn = str(x)
    for snum in sn: 
        total = total + int(snum) 
    return total

def factorial(x): 
    fat = 1
    if x != 0:
        for i in range(x):
            fat = fat * (i + 1)
    return fat

def is_prime(x):
    if x > 1:
        n = 2
        while n < x: 
            if x % n == 0: 
                return False 
                break
            n += 1
        else: 
            return True
    else:
        return False


def reverse(text):
    text_reverse = ''
    index = len(text)
    while index > 0:
        index -= 1 
        text_reverse += text[index]
    return text_reverse


def anti_vowel(text):
    text_wvowel = ''
    for char in text: 
        if char != 'a' and char != 'A' and \
           char != 'e' and char != 'E' and \
           char != 'i' and char != 'I' and \
           char != 'o' and char != 'O' and \
           char != 'u' and char != 'U': 
               text_wvowel += char
    return text_wvowel




def scrabble_score(word):

    score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
    
    total = 0
    if len(word) > 0:
        for char in word.lower():
            if score.get(char) != None:
                total += score.get(char)
    return total


def censor(text, word): #Dado um texto, procura por uma palavra e substitui todas as letras dessa palavra por asteriscos     
    if text.find(word) == -1: #word nao encontrado em text
        return text
    else:
        return text.replace(word, "*" * len(word))

def count(sequence, item): #Recebe uma lista de números inteiros, decimais, strings ou etc e busca pelo item dentro dessa lista e conta quantas ocorrencias
    occurs = 0
    for x in sequence: 
        if x == item:
            occurs += 1 
    return occurs

def purify(numbers): #Dada uma lista de números inteiros, retira os números ímpares
    purify_list = []
    for number in numbers: 
        if number % 2 == 0: 
            purify_list.append(number)
    return purify_list

def product(numbers): #Dada uma lista de números, realiza o produto destes numeros
    if len(numbers) == 0: 
        return 0
    else:
        product_total = 1 
        for number in numbers: 
            product_total *= number
        return product_total

def remove_duplicates(numbers): #Dada uma lista de números, retira as ocorrencias duplicadas
    count = {}
    duplicate_list = []
    for number in numbers: 
        if count.get(number) == None:
            count[number] = 1
            duplicate_list.append(number)
        else: 
            count[number] += 1
    print(count) #imprime a contagem de números da lista
    return duplicate_list


def median(numbers): #Dada uma lista, devolve a mediana da lista
    sorted_numbers = sorted(numbers)
    len_numbers = len(numbers)

    if len_numbers % 2 != 0:
        media = sorted_numbers[int(((len_numbers + 1)/2)-1)]   
    else: 
        media = ( sorted_numbers[int((len_numbers/2)-1)] + sorted_numbers[int(len_numbers/2)] ) / 2.0
    return media



print(digit_sum(124))
print(is_even(3))
print(is_int(2.3))
print(is_even(6))
print(is_int(-2.00))
print(factorial(4))
print(is_prime(2))
print(is_prime(3))
print(is_prime(4))
print(reverse('Python!')) 
print(anti_vowel('Hey looks Python!'))
print(scrabble_score('TESTE'))
print(scrabble_score('Me gustas'))
print(censor('This hack is wack hack', 'hack'))
print(censor('Teste final', 'string'))
print(count([1, 3, 1, 3, 1, 2], 1))
print(purify([4, 3, 3, 2, 1, 5, 6]))
print(product([2, 3, 5]))
print(remove_duplicates([2, 1, 3, 2, 1, 1, 5, 3, 2, 4]))
print(median([4, 5, 5, 4]))
