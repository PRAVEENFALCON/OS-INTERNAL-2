def contiguous_allocation():
    n = int(input("Enter the number of files: "))
    start_blocks = [0] * n
    block_lengths = [0] * n
    occupied_blocks = []

    for i in range(n):
        start_blocks[i] = int(input(f"Enter starting block for file-{i + 1}: "))
        block_lengths[i] = int(input(f"Enter number of blocks occupied by file-{i + 1}: "))
        occupied_blocks.append(list(range(start_blocks[i], start_blocks[i] + block_lengths[i])))

    # Display the allocated blocks
    print("Filename\tStart Block\tLength\tBlocks Occupied")
    for i in range(n):
        print(f"{i + 1}\t\t{start_blocks[i]}\t\t{block_lengths[i]}\t\t{occupied_blocks[i]}")

    # Retrieve file details based on file index
    file_index = int(input("Enter file number to view details: ")) - 1
    print(f"File {file_index + 1} occupies blocks: {occupied_blocks[file_index]}")

if __name__ == "__main__":
    print("Contiguous File Allocation")
    contiguous_allocation()
