def validate_order_input(
    symbol: str, 
    side: str, 
    order_type: str, 
    quantity: float, 
    price: float = None,
    stop_price: float = None
) -> bool:
    
    # Validate Side
    if side.upper() not in ['BUY', 'SELL']:
        raise ValueError("Side must be strictly 'BUY' or 'SELL'.")
    
    # Validate Order Type (Added 'STOP' here)
    if order_type.upper() not in ['MARKET', 'LIMIT', 'STOP']:
        raise ValueError("Order type must be strictly 'MARKET', 'LIMIT', or 'STOP'.")
        
    # Validate Quantity
    try:
        if float(quantity) <= 0:
            raise ValueError("Quantity must be a number greater than 0.")
    except (TypeError, ValueError):
        raise ValueError("Quantity must be a valid number.")
        
    # Validate Price for Limit and Stop Orders
    if order_type.upper() in ['LIMIT', 'STOP']:
        if price is None:
            raise ValueError(f"Price is required for {order_type.upper()} orders.")
        try:
            if float(price) <= 0:
                raise ValueError("Price must be a number greater than 0.")
        except (TypeError, ValueError):
            raise ValueError("Price must be a valid number.")

    # Validate Stop Price specifically for Stop Orders
    if order_type.upper() == 'STOP':
        if stop_price is None:
            raise ValueError("Stop price is required for STOP orders.")
        try:
            if float(stop_price) <= 0:
                raise ValueError("Stop price must be a number greater than 0.")
        except (TypeError, ValueError):
            raise ValueError("Stop price must be a valid number.")
    
    return True