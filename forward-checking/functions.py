# FORWARD CHECKING
# -1 REPRESENTS NO AVAILABLE POSITIONS
# 0 REPRESENTS AVAILABLE POSITIONS
# 1 REPRESENTS FULL BOXES

cols = [[4], [2], [7], [3, 4], [7, 2], [7, 2], [3, 4], [7], [2], [4]]
rows = [[4], [8], [10], [1, 1, 2, 1, 1], [1, 1, 2, 1, 1], [1, 6, 1], [6], [2, 2], [4], [2]]


# add 2 functions: evaluate rows and columns solution

def assignment(array, new_row, quantities, row, pos = 0):
    count = 0
    quantity = quantities[pos]
    

    for i in range(10-quantity+1):
        if row == 0: print("-------ASIGNACIÓN--------")
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
        # APPLY RECURTION TO USE ALL QUANTITIES
        if state:
            if pos+1 < len(quantities): assignment(array=array, new_row=aux, quantities=quantities, pos=pos+1, row=row)
            else:
                # print_row(aux)
                for j in range(len(aux)):
                    if aux[j] == 0:
                        aux[j] = -1
                array[row] = aux
                search_solution(array, row=row+1)

def search_solution(array, row):
    if row == len(array):
        print("SOLUCIÓN")
        for r in array:
            print_row(r)
        print("---------------")
        
        return True
    
    assignment(array=array[:], new_row=array[row][:], quantities=rows[row][:], pos=0, row=row)
    
    
def print_row(row):
    row_str = str(row).replace("-1", "\033[;31m"+"-1"+"\033[;37m")
    print(row_str)