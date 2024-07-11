import sys 

def generate_combinations(bits, current, x, current_set, opt_value):
    if len(current) == x:
        print("formed sequence", current)

        return
    for bit in bits:
        print(current_set)
        if (bit == "1"):
            print(type(bits)) 
            current_set.union( 
        generate_combinations(bits, current + bit, x, current_set, opt_value)

# Definindo os bits e o comprimento desejado
bits = "01"
x = 3

current_set = {}
opt_value   =  sys.maxsize 
# Chamando a função recursiva
generate_combinations(bits, "", x,current_set,opt_value)

array = [0 for i in range(10)]
for i in range (10):
    array[i] = list()

array[5].append(2);
array[5].append(2);
print(len(array[5]))
print(len(array[6]))
