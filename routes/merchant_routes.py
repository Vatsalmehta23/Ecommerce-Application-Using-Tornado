# routes/merchant_routes.py

from handlers.auth_handler import AuthHandler
from handlers.user_creation_handler import UserCreationHandler
from handlers.order_handler import OrderHandler
from handlers.razorpay_credential_handler import RazorpayCredentialHandler
from handlers.transaction_inquiry_handler import SimpleInquiryHandler

routes = [
    (r"/create_merchant", UserCreationHandler),
    (r"/auth", AuthHandler),
    (r"/order", OrderHandler),
    (r"/razorpay", RazorpayCredentialHandler),
    (r"/simple_inquiry/(.*)", SimpleInquiryHandler),

]