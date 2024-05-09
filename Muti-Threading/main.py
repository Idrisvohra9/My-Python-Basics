import threading
import time

# Define a function representing a resource-heavy task
def heavy_task(name, duration):
    print(f"{name} starting...")
    start_time = time.time()
    # Simulate a heavy computation
    result = 0
    for _ in range(duration):
        result += 1
    elapsed_time = time.time() - start_time
    print(f"{name} finished in {elapsed_time:.2f} seconds")

def main():
    # Create threads for each heavy task
    task1 = threading.Thread(target=heavy_task, args=("Task 1", 10000000))
    task2 = threading.Thread(target=heavy_task, args=("Task 2", 8000000))

    # Start the threads
    task1.start()
    task2.start()

    # Wait for both threads to finish
    task1.join()
    task2.join()

    print("All tasks are completed.")

if __name__ == "__main__":
    main()
