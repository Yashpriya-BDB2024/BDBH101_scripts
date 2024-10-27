# To subtract two matrices using list of lists
def matrix_subtraction(m1, m2):
# Set an empty list to store each resultant difference.
    resultant=[]
    for i in range(len(m1)):  # i - each sub-list
        row=[]
        for j in range(len(m1)):  # j - each no. in the sub-list
            result=m1[i][j]-m2[i][j]
            row.append(result)
        resultant.append(row)
    return resultant

def main():
    m1=[[1,2,3],[4,5,6],[7,8,9]]
    m2=[[10,20,30],[40,50,60],[70,80,90]]
    print(matrix_subtraction(m1,m2))
if __name__ == '__main__':
    main()