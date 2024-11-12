def main():
    n = int(input("Enter no. of files: "))
    b = [0] * 20
    sb = [0] * 20
    t = [0] * 20
    c = [[0] * 20 for _ in range(20)]

    for i in range(n):
        b[i] = int(input(f"Enter no. of blocks occupied by file-{i + 1}: "))
        sb[i] = int(input(f"Enter the starting block of file-{i + 1}: "))
        t[i] = sb[i]
        for j in range(b[i]):
            c[i][j] = sb[i]
            sb[i] += 1

    print("Filename\tStart block\tlength")
    for i in range(n):
        print(f"{i + 1}\t\t {t[i]} \t\t{b[i]}")

    x = int(input("Enter file name: "))
    print(f"File name is: {x}")
    print(f"length is: {b[x - 1]}")
    print("Blocks occupied: ", end="")
    for i in range(b[x - 1]):
        print(f"{c[x - 1][i]:4}", end="")
    print()

if __name__ == "__main__":
    main()
