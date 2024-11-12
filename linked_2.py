class File:
    def __init__(self):
        self.fname = ""
        self.start = 0
        self.size = 0
        self.block = [0] * 10

def main():
    files = []
    n = int(input("Enter no. of files: "))
    
    for i in range(n):
        file = File()
        file.fname = input("Enter file name: ")
        file.start = int(input("Enter starting block: "))
        file.block[0] = file.start
        file.size = int(input("Enter no. of blocks: "))
        
        print("Enter block numbers:")
        for j in range(1, file.size):
            file.block[j] = int(input())
        
        files.append(file)

    print("File\tstart\tsize\tblock")
    for file in files:
        print(f"{file.fname}\t{file.start}\t{file.size}\t", end="")
        for j in range(1, file.size - 1):
            print(f"{file.block[j]}--->", end="")
        print(file.block[file.size - 1])

if __name__ == "__main__":
    main()
