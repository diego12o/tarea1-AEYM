# FORWARD CHECKING
# -1 REPRESENTS NO AVAILABLE POSITIONS
# 0 REPRESENTS AVAILABLE POSITIONS
# 1 REPRESENTS FULL BOXES

cols = [[4], [2], [7], [3, 4], [7, 2], [7, 2], [3, 4], [7], [2], [4]]
rows = [[4], [8], [10], [1, 1, 2, 1, 1], [1, 1, 2, 1, 1], [1, 6, 1], [6], [2, 2], [4], [2]]

# UNUSABLE POSITIONS
# RESTART AFTER EVALUATION

# add 2 functions: evaluate rows and columns solution

def assignment(quantity, new_row, i):
    # APPLY RECURTION TO USE ALL QUANTITIES
    # print("-------NUEVA ASIGNACIÓN--------")
    state = True
    aux = new_row[:]

    # ADD -1 BEFORE AND AFTER CONSECUTIVES 1
    if i > 0:
        if aux[i-1] != 1 and state: aux[i-1] = -1
        else: state = False
        #print("First condition: " + str(state))

    if i+quantity < 10:
        if aux[i+quantity] != 1 and state: aux[i+quantity] = -1
        else: state = False
        #print("Second condition: " + str(state))

    # ADD CONSECUTIVES 1
    if state:
        for j in range(i, i+quantity):
            if aux[j] != 1 and aux[j] != -1: aux[j] = 1
            else:
                state = False
                break
        #print("Last condition: " + str(state))
        
    #print_row(aux)
    return state, aux
        
def possible_solution(array, new_row=[], quantities=[], row = 0, pos = 0):
    quantity = quantities[pos]

    for i in range(10-quantity+1):
        if row == 0 and not evaluate: print("-------ASIGNACIÓN--------")
        
        state, aux = assignment(quantity=quantity, new_row=new_row, i=i)
        
        if state:
            if pos+1 < len(quantities): possible_solution(array=array, new_row=aux, quantities=quantities, pos=pos+1, row=row)
            else:
                # print_row(aux)
                for j in range(len(aux)):
                    if aux[j] == 0:
                        aux[j] = -1
                array[row] = aux
                
                evaluation = False
                aux_array = []
                
                if row+1 < len(array): aux_array, evaluation = domain_filter(array[:], row)
                if evaluation or row+1 == len(array): search_solution(aux_array, row=row+1)

def search_solution(array, row):
    if row == len(array):
        print("SOLUCIÓN")
        for r in array:
            print_row(r)
        print("---------------")
        
        return True
    possible_solution(array=array[:], new_row=array[row][:], quantities=rows[row][:], pos=0, row=row)
    
# def evaluate_solution(array, pos = 0):    
#     for col in array:

def domain_filter(array, k=0):
    for r in array:
        print_row(r)
    print("---------------")
    
    # COLUMNS FIRST
    for i in range(len(array)-8):
        bucket = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        col = []
        for j in range(len(array)):
            col.append(array[j][i])
        evaluate(col, cols[i], bucket, 0)
        count = 0
        for j in range(k+1, len(array)):
            array[j][i] = bucket[j]
            if bucket[j] == -1: count = count + 1
            
        if count == len(array): return [], False
            
            
    # ROWS SECOND
    # for i in range(k+1, len(array)):
    #     bucket = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    #     evaluate(array[i], rows[i], bucket, 0)
    #     count = 0
    #     for j in range(len(array)):
    #         array[j][i] = bucket[j]
    #         if bucket[j] == -1: count = count + 1

    #     if count == len(array): return [], False
        
    return array, True

def evaluate(row_or_col, quantities, bucket, pos=0):
    quantity = quantities[pos]
    
    print_row(row_or_col)
    for i in range(10-quantity+1):
        state, aux = assignment(quantity=quantity, new_row=row_or_col[:], i=i)
        if state:
            if pos+1 < len(quantities): evaluate(row_or_col=aux, quantities=quantities, bucket=bucket, pos=pos+1)
            else:
                for j in range(len(aux)):
                    if aux[j] == 0: aux[j] = -1
                    if aux[j] != -1: bucket[j] = 0
                    
#evaluate([0, 0, 1, 0, 0, 1, 0, 0, 0, 0], rows[0])
#print(bucket)
    
def print_row(row):
    row_str = str(row).replace('0', ' 0').replace('1', ' 1').replace("- 1", "\033[;31m"+"-1"+"\033[;37m")
    print(row_str)