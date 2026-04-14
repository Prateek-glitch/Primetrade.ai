import logging
from binance.exceptions import BinanceAPIException, BinanceOrderException

logger = logging.getLogger("TradingBot")

class OrderManager:
    def __init__(self, client):
        self.client = client

    def place_order(self, symbol, side, order_type, quantity, price=None):
        logger.info(f"Attempting to place {order_type} {side} order for {quantity} {symbol}")
        
        # Base parameters required for all futures orders
        params = {
            'symbol': symbol.upper(),
            'side': side.upper(),
            'type': order_type.upper(),
            'quantity': quantity
        }

        # Inject limit-specific parameters
        if order_type.upper() == 'LIMIT':
            if not price:
                logger.error("Price is missing for LIMIT order.")
                raise ValueError("Price is required for LIMIT orders.")
            params['price'] = price
            params['timeInForce'] = 'GTC'  # Good Till Canceled is standard

        try:
            # Using futures_create_order specifically for the USDT-M Futures network
            response = self.client.futures_create_order(**params)
            logger.info(f"Order Success! ID: {response.get('orderId')}, Status: {response.get('status')}")
            return response
            
        except BinanceAPIException as e:
            logger.error(f"Binance API Exception: {e.status_code} - {e.message}")
            return None
        except BinanceOrderException as e:
            logger.error(f"Binance Order Exception: {e.message}")
            return None
        except Exception as e:
            logger.error(f"Unexpected system error occurred: {e}")
            return None

    def place_stop_limit_order(self, symbol, side, quantity, price, stop_price):
        """
        Places a Stop-Limit order. 
        When the 'stop_price' trigger is hit, a LIMIT order is placed at the 'price'.
        """
        logger.info(f"Attempting to place STOP-LIMIT {side} order for {quantity} {symbol} at limit {price} (Trigger: {stop_price})")
        
        # In Binance Futures, 'STOP' is the type for a Stop-Limit order
        params = {
            'symbol': symbol.upper(),
            'side': side.upper(),
            'type': 'STOP', 
            'quantity': quantity,
            'price': price,
            'stopPrice': stop_price,
            'timeInForce': 'GTC'
        }

        try:
            response = self.client.futures_create_order(**params)
            logger.info(f"Stop-Limit Order Success! ID: {response.get('orderId')}, Status: {response.get('status')}")
            return response
            
        except BinanceAPIException as e:
            logger.error(f"Binance API Exception: {e.status_code} - {e.message}")
            return None
        except BinanceOrderException as e:
            logger.error(f"Binance Order Exception: {e.message}")
            return None
        except Exception as e:
            logger.error(f"Unexpected system error occurred: {e}")
            return None