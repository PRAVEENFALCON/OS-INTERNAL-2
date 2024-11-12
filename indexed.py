def indexed_allocation():
    n = int(input("Enter the number of files: "))
    index_blocks = [0] * n
    block_lists = [[] for _ in range(n)]

    for i in range(n):
        index_blocks[i] = int(input(f"Enter the index block for file-{i + 1}: "))
        num_blocks = int(input(f"Enter the number of blocks occupied by file-{i + 1}: "))
        block_lists[i] = [int(input(f"Enter block {j + 1} for file-{i + 1}: ")) for j in range(num_blocks)]

    # Display the index and blocks
    print("Filename\tIndex Block\tBlocks Occupied")
    for i in range(n):
        print(f"{i + 1}\t\t{index_blocks[i]}\t\t{block_lists[i]}")

    # Retrieve file details based on file index
    file_index = int(input("Enter file number to view details: ")) - 1
    print(f"File {file_index + 1} with index block {index_blocks[file_index]} occupies blocks: {block_lists[file_index]}")

if __name__ == "__main__":
    print("\nIndexed File Allocation")
    indexed_allocation()
