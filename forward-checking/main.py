# FORWARD CHECKING
# -1 REPRESENTS NO AVAILABLE POSITIONS
# 0 REPRESENTS AVAILABLE POSITIONS
# 1 REPRESENTS FULL BOXES


# add 2 functions: evaluate rows and columns solution

def assignment(new_row, quantities, pos = 0):
    count = 0
    quantity = quantities[pos]

    for i in range(10-quantity+1):
        state = True
        aux = new_row[:]

        # ADD -1 BEFORE AND AFTER CONSECUTIVES 1
        if i > 0:
            if aux[i-1] != 1 and state: aux[i-1] = -1
            else: state = False

        if i+quantity < 9:
            if aux[i+quantity] != 1 and state: aux[i+quantity] = -1
            else: state = False

        # ADD CONSECUTIVES 1
        if state:
            for j in range(i, i+quantity):
                if aux[j] != 1 and aux[j] != -1: aux[j] = 1
                else:
                    state = False
                    break

        # APPLY RECURTION TO USE ALL QUANTITIES
        print(aux)
        if state:
            if pos+1 < len(quantities): assignment(new_row=aux, quantities=quantities, pos=pos+1)
            #else: print(aux)
        

def search_solution(array, row, rows, cols):
    new_row = array[row]
    quantities = rows[row]
    
    
    if row == 10:
        return True

def main():
    cols = [[4], [2], [7], [3, 4], [7, 2], [7, 2], [3, 4], [7], [2], [4]]
    rows = [[4], [8], [10], [1, 1, 2, 1, 1], [1, 1, 2, 1, 1], [1, 6, 1], [6], [2, 2], [4], [2]]

    array = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    #search_solution(array=array, col=0, row=0, rows=rows, cols=cols)
    assignment(array[0], quantities = rows[7], pos = 0)

if __name__ == '__main__':
    main()