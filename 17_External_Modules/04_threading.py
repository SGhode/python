import threading
import time

def worker(num):
    print(f"Thread {num}: Starting")
    time.sleep(2)
    print(f"Thread {num}: Finished")

threads = []
for i in range(3):
    thread = threading.Thread(target=worker, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join() # Wait for all threads to complete
print("All threads completed.")


