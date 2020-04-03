def my_function(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x

n = [0, 1, 2]
print(my_function(n)) # Add your range between the parentheses!


n = [3, 5, 7]

print(n)

def total(numbers):
    print("Função Total")
    result = 0
    for x in numbers:
        print(x)
        result = result + x
    return result 
    
print(total(n))

def soma(numbers):
    print("Função soma")
    result = 0
    for i in range(len(numbers)):
        print(i)
        result = result + numbers[i]
    return result

print(soma(n))


n = ["Michael", "Lieberman"]
# Add your function here
def join_strings(words):
    result = "" 
    for i in range(len(words)):
        result = result + words[i]
    return result


print (join_strings(n))



m = [5, 2, 6]
n = [4, 1, 3]

# Add your code here!
def join_lists(x, y):
    return sorted(x + y)


print(join_lists(m, n))
# You want this to print [1, 2, 3, 4, 5, 6]



n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here
def flatten(lists):
    results = []
    for numbers in lists:
        for number in numbers:
            results.append(number)
    return results

print(flatten(n))
