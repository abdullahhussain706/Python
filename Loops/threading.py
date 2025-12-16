# Topic 1: Threading 
import threading
import time

# Shared resource
counter = 0
lock = threading.Lock()

def increment_counter():
    global counter
    for _ in range(5):
        with lock:  # Acquire lock
            temp = counter
            time.sleep(0.1)  # Simulating work
            counter = temp + 1
            print(f"{threading.current_thread().name} incremented counter to {counter}")

# Creating multiple threads
thread1 = threading.Thread(target=increment_counter, name="Thread-1")
thread2 = threading.Thread(target=increment_counter, name="Thread-2")
thread3 = threading.Thread(target=increment_counter, name="Thread-3")
# Starting threads
thread1.start()
thread2.start()
thread3.start()

# Wait for threads to complete
thread1.join()
thread2.join()
thread3.join()

print(f"Final Counter Value: {counter}")

