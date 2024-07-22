import sys 


opt_x = ""
opt_p = sys.maxsize

def generate_combinations(bits, current, x, l, current_set, array):
    
    if len(current_set) == l:
        print("------------------------finded a solution-----------------------------")
        print("formed sequence", current)
        len_current_set = current.count('1');
        global opt_x
        global opt_p
        if len_current_set < opt_p:
            current = current.ljust(x, '0')
            opt_x = current
            opt_p = len_current_set 
        return

    if len(current) == x:
        print("formed sequence", current)
        print("formed sequence current_set", current_set)
        return

    b = greddy_heuristic(array, current, current_set, l)
    
    for bit in bits:
        if (bit == "1"):
            current_set = list(set(current_set + array[len(current)])) 
        print("current ", current)
        print("current set ", current_set)
        len_current_set = current.count('1');
        print("opt_p \n ", opt_p)
        if b >= opt_p:
            return 
        if len_current_set < opt_p: 
            generate_combinations(bits, current + bit, x, l,current_set, array)

# greddy heuristic
def greddy_heuristic(array, current, current_set,l):
    array_temp = array
    current_set_temp = current_set
    
    # grupos de candidato já decidido não devem ser considerados 
    for i in range(len(current)):
        array_temp[i] = list()

    array_temp.sort(key=len, reverse=True)
    
    len_current_set = current.count('1');

    it = 0
    for i in range(len(array_temp)):
        current_set_temp = list(set(current_set + array_temp[i]))
        it += 1
        if len(current_set) == l:
           return len_current_set + it 
    return sys.maxsize 

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


print(l,n)
for i in range(n):
    print(array[i])


# Definindo os bits e o comprimento desejado
bits = "01"
x = n


current_set = list()

# Chamando a função recursiva
stdout = generate_combinations(bits, "", x,l,current_set,array)


print("result recursão stdout \n ", stdout)
print("opt_p: ", opt_p)
print("opt_x: ", opt_x)

if (opt_x == ""):
    print("Inviavel")
else:
    for i in range(n):
        if opt_x[i] == '1':
            print(i+1, end=" ");

print(" ");



