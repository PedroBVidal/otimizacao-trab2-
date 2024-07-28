import sys 
import argparse
import time


opt_x = ""
opt_p = sys.maxsize
cont_nodes = 0
def generate_combinations(bits, current, x, l, current_set, array):
    
    if len(current_set) == l:
        len_current_set = current.count('1');
        global opt_x
        global opt_p
        if len_current_set < opt_p:
            current = current.ljust(x, '0')
            opt_x = current
            opt_p = len_current_set 
        return

    if len(current) == x:
        return

    b = 0  
    if (args.a):
        b = current.count('1') + 1
    else:
        b = current.count('1') + bounding_function(array, current, current_set,l)

  
    for bit in bits:
        global cont_nodes
        len_current_set = len(current_set)
        if (bit == "1"):
            current_set = list(set(current_set + array[len(current)])) 
        
        len_current_set_after = len(current_set)

        generate_bit1_branch = True 
        if (not(args.f)): 
            if (len_current_set == len_current_set_after and bit == '1'):
                generate_bit1_branch = False
                

        len_current = current.count('1') 

        if (args.o):
            if (generate_bit1_branch == True):
                cont_nodes += 1
                generate_combinations(bits, current + bit ,x, l,current_set, array)
        elif (args.a):
            if b < opt_p: 
                if (generate_bit1_branch == True):
                    cont_nodes += 1
                    generate_combinations(bits, current + bit ,x, l,current_set, array)
        else:
            if b < opt_p: 
                if (generate_bit1_branch == True):
                    cont_nodes += 1
                    generate_combinations(bits, current + bit, x, l,current_set, array)

# greddy heuristic
def greddy_heuristic(array, current, current_set,l):
    array_temp = array
    current_set_temp = current_set
    
    # grupos de candidato já decidido não devem ser considerados 
    for i in range(len(current)):
        array_temp[i] = list()

    array_temp.sort(key=len, reverse=True)
    
    len_current_set = current.count('1')

    it = 0
    for i in range(len(array_temp)):
        current_set_temp = list(set(current_set + array_temp[i]))
        it += 1
        if len(current_set) == l:
           return len_current_set + it 
    return sys.maxsize 

def bounding_function(array, current, current_set,l):
    groups_left = l - len(current_set)
    candidates_left_with_groups_filtered = list()
   
    for i in range(len(current),len(array)):
        result = [item for item in array[i] if item not in current_set] 
        candidates_left_with_groups_filtered.append(result)
       

    candidates_left_with_groups_filtered.sort(key=len, reverse=True)
    

    cont_unique_groups = 0
    cont_necessary_candidates = 0

    for i in range(len(candidates_left_with_groups_filtered)):
        cont_unique_groups += len(candidates_left_with_groups_filtered[cont_necessary_candidates]) 
        cont_necessary_candidates += 1
        if cont_unique_groups >= groups_left:
           break

    
    return cont_necessary_candidates

         

input_data = sys.stdin.readline()
numbers  = input_data.split()
nums = [int(num) for num in numbers]

l, n = nums

array = [0 for i in range(n)]


for i in range(n):
    input_data = sys.stdin.readline()
    numbers = input_data.split()
    nums = [int(num) for num in numbers]
    array[i] = nums[1:]


# Definindo os bits e o comprimento desejado
bits = "01"
x = n
current_set = list()

# Create the parser
parser = argparse.ArgumentParser(description="Process some command-line options.")

# Define the command-line arguments
parser.add_argument('-a', '--a', action='store_true', help='função limitante default')
parser.add_argument('-o', '--o', action='store_true', help='desligar cortes por otimalidade')
parser.add_argument('-f', '--f', action='store_true', help='deligar coretes por viabilidade')

# Parse the command-line arguments
args = parser.parse_args()


# Chamando a função recursiva
tempo = 0
tempo_inicial = time.time()
stdout = generate_combinations(bits, "", x,l,current_set,array) 
tempo_final = time.time()
tempo += tempo_final - tempo_inicial 


print(f"{tempo} segundos")
print("cont nos ", cont_nodes);
#print("result recursão stdout \n ", stdout)
#print("opt_p: ", opt_p)
#print("opt_x: ", opt_x)

if (opt_x == ""):
    print("Inviavel")
else:
    for i in range(n):
        if opt_x[i] == '1':
            print(i+1, end=" ");

print("")

