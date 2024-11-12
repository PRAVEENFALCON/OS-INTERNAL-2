import threading
import time
import random

NUM_PHILOSOPHERS = 5

forks = [threading.Semaphore(1) for _ in range(NUM_PHILOSOPHERS)]

def philosopher(id):
    left_fork = id
    right_fork = (id + 1) % NUM_PHILOSOPHERS

    while True:
        print(f"Philosopher {id} is thinking.")
        time.sleep(random.uniform(1, 3))

        print(f"Philosopher {id} is hungry.")

        with forks[left_fork]:
            with forks[right_fork]:
                print(f"Philosopher {id} is eating.")
                time.sleep(random.uniform(1, 2))
                
        print(f"Philosopher {id} finished eating and is thinking.")

philosophers = [threading.Thread(target=philosopher, args=(i,)) for i in range(NUM_PHILOSOPHERS)]
for p in philosophers:
    p.start()
for p in philosophers:
    p.join()
