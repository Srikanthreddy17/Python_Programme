# one time password generator to mobile number
# OTP generation for mobile number verification
import random
import string
import re
def generate_otp(length=6):
    if length < 4:
        raise ValueError("OTP length should be at least 4 characters.")
    
    # Generate a random OTP consisting of digits
    otp = ''.join(random.choices(string.digits, k=length))
    
    return otp

def is_valid_mobile_number(mobile_number):
    # Simple validation for Indian mobile numbers with country code +91
    pattern = r"^\+91\d{10}$"
    return re.match(pattern, mobile_number) is not None

# Example usage
if __name__ == "__main__":
    otp = generate_otp()
    print(f"Generated OTP: {otp}")
    # Example usage
    mobile_number = "+917095160127"
    if is_valid_mobile_number(mobile_number):
        print(f"Mobile number {mobile_number} is valid.")
    else:
        print(f"Mobile number {mobile_number} is invalid.")