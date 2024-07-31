import razorpay
import time
async def create_razorpay_order(amount, access_key, access_secret):
    client = razorpay.Client(auth=(access_key, access_secret))
    try:
        start_time = time.time()
        order = client.order.create({
            "amount": amount * 100,  
            "currency": "INR",
        })
        end_time = time.time()
        return order,end_time - start_time
    except Exception as e:
        raise RuntimeError(f"Error creating Razorpay order: {str(e)}")

async def fetch_razorpay_order(order_id, access_key, access_secret):
    client = razorpay.Client(auth=(access_key, access_secret))
    try:
        order = client.order.fetch(order_id)
        return order
    except Exception as e:
        raise RuntimeError(f"Error fetching Razorpay order: {str(e)}")
