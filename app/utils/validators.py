from datetime import datetime
from app.models.expense_model import CategoryEnum

# the partial arg is true when all fields arent necessary
def validate_expense_data(data, partial=False):
    if not data:
        return "Invalid JSON"
    
    if "amount" in data:
        try:
            val = float(data["amount"])
            if val < 0: return "Amount cannot be a negative" 
        except (ValueError, TypeError):
            return "Invalid amount: must be a number"
    elif not partial:
        return "Amount is required"
    
    if "category" in data:
        valid_vals = [item.value for item in CategoryEnum]
        if data["category"] not in valid_vals:
            return f"Invalid category, Must be one of: {', '.join(valid_vals)}"
    elif not partial:
        return "Category is required"
    

    if "date" in data:
        if not data["date"]:
            return "Date cannot be empty"
        try:
            datetime.strptime(data["date"], "%Y-%m-%d")
        except (ValueError, TypeError):
            return "Invalid date format, use YYYY-MM-DD"
    elif not partial:
        return "Date is required"
    
    if "description" in data and data["description"]: # checks if any description with length > 0
        if len(data["description"]) > 255:
            return "description cannot be longer than 255 chars"
    
    return None # the function returns none only when everything is correct

# the func will behave differently in case partial is give value true*