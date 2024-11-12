import threading
import time

# Task for the first thread: Counting numbers
def count_numbers():
    for i in range(1, 6):
        print(f"Count: {i}")
        time.sleep(1)  # Simulating a time-consuming task

# Task for the second thread: Printing letters
def print_letters():
    for letter in "ABCDE":
        print(f"Letter: {letter}")
        time.sleep(1)  # Simulating a time-consuming task

# Creating two threads for the tasks
thread1 = threading.Thread(target=count_numbers)
thread2 = threading.Thread(target=print_letters)

# Starting both threads
thread1.start()
thread2.start()

# Waiting for both threads to complete
thread1.join()
thread2.join()

print("Both tasks completed.")

