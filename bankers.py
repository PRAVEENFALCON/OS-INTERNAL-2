def get_matrix(rows, cols, name):
    matrix = []
    print(f"Enter the {name} matrix:")
    for i in range(rows):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        while len(row) != cols:
            print(f"Please enter exactly {cols} integers.")
            row = list(map(int, input(f"Row {i + 1}: ").split()))
        matrix.append(row)
    return matrix

n = int(input("Enter the number of processes: "))
m = int(input("Enter the number of resources: "))

alloc = get_matrix(n, m, "Allocation")
max = get_matrix(n, m, "Maximum")

avail = list(map(int, input("Enter available resources (space-separated): ").split()))
while len(avail) != m:
    print(f"Please enter exactly {m} integers.")
    avail = list(map(int, input("Enter available resources (space-separated): ").split()))

f = [0] * n
ans = [0] * n
ind = 0

need = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        need[i][j] = max[i][j] - alloc[i][j]

for _ in range(n):
    for i in range(n):
        if f[i] == 0:
            flag = 0
            for j in range(m):
                if need[i][j] > avail[j]:
                    flag = 1
                    break
            
            if flag == 0:
                ans[ind] = i
                ind += 1
                for y in range(m):
                    avail[y] += alloc[i][y]
                f[i] = 1

print("Following is the SAFE Sequence:")
for i in range(n - 1):
    print(" P", ans[i], " ->", sep="", end="")
print(" P", ans[n - 1], sep="")

