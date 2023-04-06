array = [1, 1, 1, 1, -1, -1, 0, 0, 0, 0]
cols = [4, 2]
bucket = [0, 0, 0, 0, -1, -1, 0, 0, 0, 0]

def soluciones(array, bucket, quantities=[], pos=0):
    # INITIAL VALUES
    state = True
    print(pos)
    quantity = quantities[pos]
    count = 0
    
    while(count != 10-quantity+1):
        if bucket[count] == 0:
            ones = 0
            aux_bucket = bucket[:]
            aux_array = array[:]
            
            for i in range(count, count+quantity):
                if bucket[i] == 0:
                    if aux_array[i] == 1: ones = ones + 1
                    
                    aux_array[i] = 1
                    aux_bucket[i] = -1
                else:
                    count = i
                    state = False
                    break
        
            if state:
                bucket = aux_bucket
                array = aux_array
                
                if pos+1 == len(quantities): print(array)
                else: soluciones(array[:], bucket[:], quantities, pos+1)
                
                if ones == quantity: break
        
        count = count + 1
        
soluciones(array, bucket, cols, 0)