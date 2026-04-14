import os
from binance.client import Client
from dotenv import load_dotenv

# Load variables from the .env file
load_dotenv()

class BinanceTestnetClient:
    def __init__(self):
        self.api_key = os.getenv('BINANCE_API_KEY')
        self.api_secret = os.getenv('BINANCE_API_SECRET')
        
        if not self.api_key or not self.api_secret:
            raise ValueError("API keys not found. Please check your .env file.")

        # Initialize client with Testnet setting
        self.client = Client(
            self.api_key, 
            self.api_secret, 
            testnet=True  # Crucial: This points to testnet.binancefuture.com
        )
        
        # Explicitly set the Futures Testnet URL as per assignment requirements
        self.client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'

    def get_client(self):
        return self.client