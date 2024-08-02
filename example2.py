import asyncio
import time

async def simulate_io_bound():
    await asyncio.sleep(5) 

def cpu_bound_task(duration):
    time.sleep(duration)  
async def process_request(index):
    start_time = time.time()
    
       
    # cpu_bound_task(2)
    
    
    await simulate_io_bound()
    
    
    cpu_bound_task(1)
    
    end_time = time.time()
    total_time = end_time - start_time
    print(f"Request {index}: Total Time = {total_time:.2f} seconds")

async def main():
   
    tasks = [process_request(i) for i in range(4)]
    
    
    start_time = time.time()
    
    await asyncio.gather(*tasks)
    
    end_time = time.time()
    total_time = end_time - start_time
    print(f"Total time for all requests: {total_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())



# import asyncio
# import time

# # Synchronous CPU-bound function
# def cpu_bound_task(duration):
#     time.sleep(duration)  # Simulating CPU-bound work

# # Asynchronous I/O-bound function
# async def io_bound_task(duration):
#     await asyncio.sleep(duration)  # Simulating I/O-bound work

# # Function to process each request
# async def process_request(index, cpu_pre_time, io_time, cpu_post_time):
#     start_time = time.time()
    
    # Simulate CPU-bound preprocessing
#     # cpu_bound_task(cpu_pre_time)
    
#     # Simulate I/O-bound operation
#     await io_bound_task(io_time)
    
#     # Simulate CPU-bound postprocessing
#     cpu_bound_task(cpu_post_time)
    
#     end_time = time.time()
#     total_time = end_time - start_time
#     print(f"Request {index}: Total Time = {total_time:.2f} seconds")

# async def main():
#     # Task parameters
#     tasks_params = [
#         (2, 5, 1),  # Task 1: 2 sec CPU, 5 sec I/O, 1 sec CPU
#         (2, 7, 1),  # Task 2: 2 sec CPU, 7 sec I/O, 1 sec CPU
#         (11, 9, 1)  # Task 3: 11 sec CPU, 9 sec I/O, 1 sec CPU
#     ]
    
#     # Create a list of tasks
#     tasks = [process_request(i, *params) for i, params in enumerate(tasks_params)]
    
#     # Measure the total time for all requests
#     start_time = time.time()
    
#     await asyncio.gather(*tasks)
    
#     end_time = time.time()
#     total_time = end_time - start_time
#     print(f"Total time for all requests: {total_time:.2f} seconds")

# if __name__ == "__main__":
#     asyncio.run(main())
