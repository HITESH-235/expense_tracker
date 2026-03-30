from datetime import datetime

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
    
    if "category" in data: # checks key
        if not str(data["category"]).strip(): # checks value
            return "Category cannot be empty"
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
    
    return None # the function returns none only when everything is correct

# the func will behave differently in case partial is give value true*