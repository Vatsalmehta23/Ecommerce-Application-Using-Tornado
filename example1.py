import time

def simulate_io_bound():
    time.sleep(5) 
def cpu_bound_task(duration):
    time.sleep(duration) 

def process_request(index):
    start_time = time.time()
    
    
    # cpu_bound_task(1)
    
    
    
    cpu_bound_task(1)
    simulate_io_bound()
    
    end_time = time.time()
    total_time = end_time - start_time
    print(f"Request {index}: Total Time = {total_time:.2f} seconds")

def main():
  
    start_time = time.time()
    
    for i in range(4):
        process_request(i)
    
    end_time = time.time()
    total_time = end_time - start_time
    print(f"Total time for all requests: {total_time:.2f} seconds")

if __name__ == "__main__":
    main()
