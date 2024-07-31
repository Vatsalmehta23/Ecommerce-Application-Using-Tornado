import requests
import time
import razorpay
from config import Config

def create_razorpay_order(amount):
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

def main():
    amount = 1000  
    num_requests = 5  

    start_time = time.time() 

    for i in range(num_requests):
        try:
            order, elapsed_time = create_razorpay_order(amount)
            print(f"Order {i} created: {order['id']}")
            print(f"Time taken for Order {i}: {elapsed_time:.4f} seconds")
        except Exception as e:
            print(f"Failed to create order: {e}")

    end_time = time.time()  
    total_time = end_time - start_time
    print(f"Total throughput time: {total_time:.4f} seconds")

if __name__ == "__main__":
    main()
