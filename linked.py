def linked_allocation():
    n = int(input("Enter the number of files: "))
    file_blocks = [[] for _ in range(n)]

    for i in range(n):
        num_blocks = int(input(f"Enter the number of blocks occupied by file-{i + 1}: "))
        print(f"Enter the blocks in sequence for file-{i + 1}:")
        file_blocks[i] = [int(input(f"Block {j + 1}: ")) for j in range(num_blocks)]

    # Display the linked allocation details
    print("Filename\tBlocks Sequence")
    for i in range(n):
        print(f"{i + 1}\t\t{' -> '.join(map(str, file_blocks[i]))}")

    # Retrieve file details based on file index
    file_index = int(input("Enter file number to view details: ")) - 1
    print(f"File {file_index + 1} block sequence: {' -> '.join(map(str, file_blocks[file_index]))}")

if __name__ == "__main__":
    print("\nLinked File Allocation")
    linked_allocation()
