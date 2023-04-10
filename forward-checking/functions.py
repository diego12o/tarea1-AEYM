# FORWARD CHECKING
# -1 REPRESENTS NO AVAILABLE POSITIONS
# 0 REPRESENTS AVAILABLE POSITIONS
# 1 REPRESENTS FULL BOXES

cols = [[4], [2], [7], [3, 4], [7, 2], [7, 2], [3, 4], [7], [2], [4]]
rows = [[4], [8], [10], [1, 1, 2, 1, 1], [1, 1, 2, 1, 1], [1, 6, 1], [6], [2, 2], [4], [2]]

contador = 0

# UNUSABLE POSITIONS
# RESTART AFTER EVALUATION

# add 2 functions: evaluate rows and columns solution

def assignment(quantity, new_row, i, evaluate=False, used=[]):
    # APPLY RECURTION TO USE ALL QUANTITIES
    # print("-------NUEVA ASIGNACIÓN--------")
    state = True
    aux = new_row[:]

    # ADD -1 BEFORE AND AFTER CONSECUTIVES 1
    if i > 0:
        if aux[i-1] != 1 and state: aux[i-1] = -1
        else: state = False
        #print("First condition: " + str(state))

    if i+quantity < len(aux):
        if aux[i+quantity] != 1 and state: aux[i+quantity] = -1
        else: state = False
        #print("Second condition: " + str(state))

    # ADD CONSECUTIVES 1
    if state:
        if evaluate:
            for j in range(i, i+quantity):
                #print(j)
                if aux[j]!=-1 and j not in used:
                    aux[j] = 1
                    used.append(j)
                else:
                    state = False
                    break

        else:
            for j in range(i, i+quantity):
                if aux[j] == 0: aux[j] = 1
                else:
                    state = False
                    break
        #print("Last condition: " + str(state))
    #print_row(aux)
    return state, aux, used
        
def possible_solution(array, new_row=[], quantities=[], row = 0, pos = 0, revised=[], order=[]):
    quantity = quantities[pos]

    row_array = order[row]
    for i in range(len(array)-quantity+1):
        
        state, aux, used = assignment(quantity=quantity, new_row=new_row[:], i=i)
        
        if state:
            if pos+1 < len(quantities):
                if possible_solution(array=array[:], new_row=aux[:], quantities=quantities, pos=pos+1, row=row, revised=revised[:], order=order): return True
            else:
                # print_row(aux)
                global contador
                contador = contador + 1
                for j in range(len(aux)):
                    if aux[j] == 0:
                        aux[j] = -1
                array[row_array] = aux
                
                evaluation = True
                aux_array = []
                
                for r in array:
                    aux_array.append(r[:])
                
                if row+1 < len(array):
                    revised.append(row_array)
                    aux_array, evaluation = domain_filter(aux_array, row, revised[:])
                
                #if len(aux_array) != 0: array = aux_array
                if evaluation or row+1 == len(array): 
                    if search_solution(aux_array[:], row=row+1, revised=revised[:], order=order): return True

def search_solution(array, row, order, revised=[]):
    if row == len(array):
    # if row == len(array):
        print("SOLUCIÓN")
        for r in array:
            print_row(r)
        print("---------------")
        print("Nodos: " + str(contador))
        
        return True
    
    row_array = order[row]
    if possible_solution(array=array[:], new_row=array[row_array][:], quantities=rows[row_array][:], pos=0, row=row, revised=revised[:], order=order): return True

def domain_filter(array, k=0, revised=[]):
    # print("---------------")
    # for r in array:
    #     print_row(r)
    
    # COLUMNS FIRST    
    for i in range(len(array)):
        bucket = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        col = []
        for j in range(len(array)):
            col.append(array[j][i])
            
        evaluate(col[:], cols[i], bucket)
        
        count = 0
        for j in range(len(array)):
            if j not in revised: array[j][i] = bucket[j]
            if bucket[j] == -1: count = count + 1
            
        if count == len(array): return array, False
    
    
    for i in range(len(array)):
        if i not in revised:
            bucket = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
            evaluate(array[i], rows[i], bucket)
            #print_row(bucket)
            count = 0
            for j in range(len(array)):
                array[i][j] = bucket[j]
                if bucket[j] == -1: count = count + 1

            if count == len(array): return array, False
        
    return array, True

def evaluate(row_or_col, quantities, bucket, pos=0, used=[]):
    sum_quantities = 0
    for quantity in quantities:
        sum_quantities = sum_quantities + quantity
    
    quantity = quantities[pos]
    # print("----------------------------")
    # print_row(row_or_col)
    # print(bucket)
    
    for i in range(len(row_or_col)-quantity+1):        
        state, aux, aux_used = assignment(quantity=quantity, new_row=row_or_col[:], i=i, evaluate=True, used=used[:])
        #print("New possible solution")
        # print_row(aux)
        
        count = 0
        for i in range(len(aux)):
            if aux[i] == 1: count = count + 1
            
        if count > sum_quantities: state = False
        
        if state:
            if pos+1 < len(quantities): evaluate(row_or_col=aux[:], quantities=quantities, bucket=bucket, pos=pos+1, used=aux_used[:])
            else:
                count = 0
                for j in range(len(aux)):
                    if aux[j] == 1: count = count + 1
                    
                    if aux[j] == 0: aux[j] = -1
                    if aux[j] != -1: bucket[j] = 0
                        
                # print("--------------------------------------------------------------")
        
                
    
def print_row(row):
    row_str = str(row).replace('0', ' 0').replace('1', ' 1').replace("- 1", "\033[;31m"+"-1"+"\033[;37m")
    print(row_str)
    