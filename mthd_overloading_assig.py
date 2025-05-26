class Payment:
    def process_payment(self, amount,currency="USD", payment_method=None):
        if isinstance(amount, int) or isinstance(amount, float):
            if payment_method is None:
                return f"Processing {currency} {amount} using default payment method."
            else:
                return f"Processing {currency} {amount} via {payment_method}"
        else:
            return "Invalid payment amount"
        
#creating the object of the class above
payment = Payment()
print(payment.process_payment(3000))
print(payment.process_payment(60000, "UGX."))
print(payment.process_payment(60000, "UGX.", "momo"))
