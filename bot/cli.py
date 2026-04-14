import argparse
import sys
from bot.logging_config import setup_logging
from bot.client import BinanceTestnetClient
from bot.orders import OrderManager
from bot.validators import validate_order_input

# Rich imports for enhanced UI
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

def main():
    logger = setup_logging()
    console = Console() # Initialize the rich console
    
    parser = argparse.ArgumentParser(description="Primetrade.ai - Binance Futures Testnet Trading Bot")
    parser.add_argument('--symbol', required=True, help="Trading pair symbol (e.g., BTCUSDT)")
    parser.add_argument('--side', required=True, choices=['BUY', 'SELL', 'buy', 'sell'], help="Order side: BUY or SELL")
    # Added STOP to choices for the bonus feature
    parser.add_argument('--type', required=True, choices=['MARKET', 'LIMIT', 'STOP', 'market', 'limit', 'stop'], help="Order type: MARKET, LIMIT, or STOP")
    parser.add_argument('--quantity', required=True, type=float, help="Order quantity in asset amount")
    parser.add_argument('--price', type=float, help="Order price (Required for LIMIT and STOP orders)")
    # Added stop-price for the Stop-Limit order type
    parser.add_argument('--stop-price', type=float, help="Stop trigger price (Required for STOP orders)")

    args = parser.parse_args()

    symbol = args.symbol.upper()
    side = args.side.upper()
    order_type = args.type.upper()
    quantity = args.quantity
    price = args.price
    stop_price = args.stop_price

    # 1. Print Order Summary (Enhanced with Rich Table)
    table = Table(title="Order Request Summary", title_style="bold cyan", show_header=True, header_style="bold magenta")
    table.add_column("Parameter", style="dim", width=15)
    table.add_column("Value", style="bold white")
    
    table.add_row("Symbol", symbol)
    table.add_row("Side", side)
    table.add_row("Type", order_type)
    table.add_row("Quantity", str(quantity))
    if order_type in ['LIMIT', 'STOP']:
        table.add_row("Price", str(price))
    if order_type == 'STOP':
        table.add_row("Stop Price", str(stop_price))
    
    console.print(table)
    console.print()

    try:
        # 2. Validate Input & Initialize Client
        client_wrapper = BinanceTestnetClient()
        binance_client = client_wrapper.get_client()
        order_manager = OrderManager(binance_client)
        
        # 3. Place Order (Routing based on order type)
        if order_type == 'STOP':
            if not stop_price or not price:
                raise ValueError("Both --price and --stop-price are required for STOP orders.")
            response = order_manager.place_stop_limit_order(symbol, side, quantity, price, stop_price)
        else:
            # We call your standard validator for MARKET and LIMIT
            validate_order_input(symbol, side, order_type, quantity, price)
            response = order_manager.place_order(symbol, side, order_type, quantity, price)

        # 4. Output Result (Enhanced with Rich Panel)
        if response:
            success_text = (
                f"[bold green]Order ID:[/bold green]     {response.get('orderId')}\n"
                f"[bold green]Status:[/bold green]       {response.get('status')}\n"
                f"[bold green]Executed Qty:[/bold green] {response.get('executedQty', 0)}\n"
                f"[bold green]Avg Price:[/bold green]    {response.get('avgPrice', 'N/A')}"
            )
            # Wrap the success message in a clean terminal box
            panel = Panel(success_text, title="✅ Order Placed Successfully", border_style="green", expand=False)
            console.print(panel)
            console.print()
        else:
            console.print("[bold red]❌ Failed to place order. Check the trading_bot.log file for details.[/bold red]\n")
            sys.exit(1)

    except ValueError as ve:
        logger.error(f"Validation Error: {ve}")
        # Wrap errors in a red terminal box
        console.print(Panel(f"{ve}", title="❌ Input Error", border_style="red", expand=False))
        sys.exit(1)
    except Exception as e:
        logger.error(f"System Error: {e}")
        console.print(Panel(f"{e}", title="❌ System Error", border_style="red", expand=False))
        sys.exit(1)

if __name__ == "__main__":
    main()