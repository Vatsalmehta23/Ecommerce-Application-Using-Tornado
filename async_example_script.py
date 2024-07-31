import aiohttp
import asyncio
import time
import razorpay
from config import Config

async def create_razorpay_order(amount):
    client = razorpay.Client(auth=(Config.RAZORPAY_KEY_ID, Config.RAZORPAY_KEY_SECRET))
    try:
        start_time = time.time()
        order = client.order.create({
            "amount": amount * 100,  
            "currency": "INR",
        })
        end_time = time.time()
        return order, end_time - start_time
    except Exception as e:
        raise RuntimeError(f"Error creating Razorpay order: {str(e)}")

async def main():
    amount = 1000  
    num_concurrent_requests = 5  

    start_time = time.time() 

    async def create_order(index):
        try:
            order, elapsed_time = await create_razorpay_order(amount)
            print(f"Order {index} created: {order['id']}")
            print(f"Time taken for Order {index}: {elapsed_time:.4f} seconds")
        except Exception as e:
            print(f"Failed to create order: {e}")

    tasks = [create_order(i) for i in range(num_concurrent_requests)]
    await asyncio.gather(*tasks)

    end_time = time.time()  
    total_time = end_time - start_time
    print(f"Total throughput time: {total_time:.4f} seconds")

if __name__ == "__main__":
    asyncio.run(main())
