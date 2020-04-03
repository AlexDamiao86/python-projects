def square(n):
    """Returns the square of a number."""
    squared = n**2
    print("%d squared is %d." % (n, squared))
    return squared
    
# Call the square function on line 9! Make sure to
# include the number 10 between the parentheses.
square(10)

print(square(2)) #imprime 2 squared is 4 e na outra linha 4.


def power(base, exponent):  # Add your parameters here!
    result = base**exponent
    print("%d to the power of %d is %d." % (base, exponent, result))

power(37,4)  # Add your arguments here!

print(power(2,4)) 

"""imprime 2 to the power of 4 is 16 e na outra linha None
porque a função power nao retonou nenhum valor"""

def one_good_turn(n):
    return n + 1
    
def deserves_another(n):
    return one_good_turn(n) + 2

print(deserves_another(3))
                    
