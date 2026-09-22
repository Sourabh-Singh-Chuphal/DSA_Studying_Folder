def pattern1(n):
    for i in range(0, n):
        for j in range(0, n):
            print('*', end="")
        print('')

def pattern4(m):
        for rows in range(1, m+1):
            for colums in range(rows):
                print(rows,end ='')
            print('')


n = int(input("Enter the number of rows: "))
m = int(input("Enter the number of m rows: "))

pattern1(n)
pattern4(m)


