# this file acts as the data guard, to inspect incoming data from the user's  request before it touches services/database
# ensure data is clean, correctly formatted, and follows rules

from datetime import datetime
from app.models.expense_model import CategoryEnum

# the partial arg is to handle two different cases:
# 1. creating a new expense (p = F): all fields mandatory
# 2. updating an exisiting expense (p = t): update an expense
def validate_expense_data(data, partial=False):

    # basic check, if user did send any data:
    if not data:
        return "Invalid JSON"
    
    # --- Amount Validation ---
    if "amount" in data:
        try:
            val = float(data["amount"]) # ensure inp is a number
            if val < 0: return "Amount cannot be a negative" 
        except (ValueError, TypeError):
            return "Invalid amount: must be a number"
    elif not partial:
        return "Amount is required" # for just updation, amt is not necessary
    
    # --- Category Validation ---
    if "category" in data:
        # grabs ["Food", "Rent"...] from enum class 
        valid_vals = [item.value for item in CategoryEnum]
        # prevents user from choosing wrong category
        if data["category"] not in valid_vals:
            return f"Invalid category, Must be one of: {', '.join(valid_vals)}"
    elif not partial:
        return "Category is required"
    
    # --- Date Validation ---
    if "date" in data:
        if not data["date"]:
            return "Date cannot be empty"
        try:
            # validates that string matches expected format
            datetime.strptime(data["date"], "%Y-%m-%d")
        except (ValueError, TypeError):
            return "Invalid date format, use YYYY-MM-DD"
    elif not partial:
        return "Date is required"
    
    # --- Description Validation ---
    if "description" in data and data["description"]: # checks if any description with length > 0
        if len(data["description"]) > 255:
            return "description cannot be longer than 255 chars"
    
    return None # the function returns none only when everything is correct