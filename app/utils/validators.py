# the partial arg is true when all fields arent necessary
def validate_expense_data(data, partial=False):
    if not data:
        return "Invalid JSON"
    
    if "amount" in data:
        try:
            float(data["amount"]) # checks if give amount is a float type (or integer)
            # goes to except block if amount is invalid even here
        except:
            return "Invalid amount"
    elif not partial:
        return "Amount is required"
    
    if "category" in data:
        if not data["category"]:
            return "Category cannot be empty"
    elif not partial:
        return "Category is required"
    

    if "date" in data:
        if not data["date"]:
            return "Date cannot be empty"
    elif not partial:
        return "Date is required"
    
    return None # the function returns none only when everything is correct

# the func will behave differently in case partial is give value true*