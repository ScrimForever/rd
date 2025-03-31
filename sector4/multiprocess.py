import threading
from typing import List


def square(number: List, results, index):
    results[index] = number * number


def main_process(numbers):
    results = [None for _ in range(0, len(numbers))]
    threads = []
    
    for i, num in enumerate(numbers):
        thread = threading.Thread(target=square, args=(num, results, i))
        threads.append(thread)
        thread.start()


    
    # Wait for all threads to finish
    
    for thread in threads:
        thread.join()
    
    return results