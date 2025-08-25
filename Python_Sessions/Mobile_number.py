# mobile number validation with limited length
import re
def is_valid_mobile_number(mobile_number):
    # Regular expression to match a valid mobile number
    pattern = r'^\+?[1-9]\d{0,14}$'
    
    # Check if the mobile number matches the pattern
    if re.match(pattern, mobile_number):
        return True
    else:
        return False