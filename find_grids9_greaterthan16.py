
tokens = [ [1,1,3,1,1],
           [1,2,2,1,2],
           [1,2,1,2,3],
           [1,3,1,1,1],
           [1,2,3,2,3],
         ]

# Find cells where sum of itself and other eight cells around it > 16

def find_cell_wsum_greaterthan_16(t):
    cells_wsum_greaterthan_16 = list()
    for i in range(-1,4): #rows
        for j in range(-1,4): #cols
            sum = t[i-1][j-1] + t[i-1][j] + t[i-1][j+1] + \
                  t[i][j-1] + t[i][j] + t[i][j+1] + \
                  t[i+1][j-1] + t[i+1][j] + t[i+1][j+1]
            if sum > 16:
                if i == -1:
                    row = 4
                else:
                    row = i
                if j == -1:
                    col = 4
                else:
                    col = j
                cells_wsum_greaterthan_16.append([row,col])
    return cells_wsum_greaterthan_16

def main():
    answer = find_cell_wsum_greaterthan_16(tokens)
    for val in answer:
        print "tokens[", val[0], "][", val[1], "]"

if __name__ == "__main__":
   main()

            
