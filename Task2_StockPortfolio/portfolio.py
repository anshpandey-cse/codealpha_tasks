# Stock Portfolio Tracker
# CodeAlpha Internship - Task 2

stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 420,
    "AMZN": 190
}

portfolio = {}


def show_stocks():
    print("\nAvailable Stocks:")
    for symbol, price in stocks.items():
        print(f"{symbol}: ${price}")


def buy_stock():
    show_stocks()

    symbol = input("\nEnter stock symbol: ").upper().strip()

    if symbol not in stocks:
        print("❌ Stock not available.")
        return

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("❌ Quantity must be greater than 0.")
            return

        portfolio[symbol] = portfolio.get(symbol, 0) + quantity

        print(
            f"✅ Bought {quantity} shares of {symbol} "
            f"for ${stocks[symbol] * quantity}"
        )

    except ValueError:
        print("❌ Please enter a valid quantity.")


def sell_stock():
    if not portfolio:
        print("\n❌ Your portfolio is empty.")
        return

    print("\nYour Portfolio:")
    for symbol, quantity in portfolio.items():
        print(f"{symbol}: {quantity} shares")

    symbol = input("\nEnter stock symbol to sell: ").upper().strip()

    if symbol not in portfolio:
        print("❌ You don't own this stock.")
        return

    try:
        quantity = int(input("Enter quantity to sell: "))

        if quantity <= 0:
            print("❌ Quantity must be greater than 0.")
            return

        if quantity > portfolio[symbol]:
            print("❌ You don't have enough shares.")
            return

        portfolio[symbol] -= quantity

        if portfolio[symbol] == 0:
            del portfolio[symbol]

        print(f"✅ Sold {quantity} shares of {symbol}.")

    except ValueError:
        print("❌ Please enter a valid quantity.")


def show_portfolio():
    if not portfolio:
        print("\n📂 Your portfolio is empty.")
        return

    print("\n========== YOUR PORTFOLIO ==========")

    total_value = 0

    for symbol, quantity in portfolio.items():
        price = stocks[symbol]
        value = quantity * price
        total_value += value

        print(
            f"{symbol}: {quantity} shares × "
            f"${price} = ${value}"
        )

    print("------------------------------------")
    print(f"💰 Total Portfolio Value: ${total_value}")
    print("====================================")


def main():
    while True:
        print("\n========== STOCK PORTFOLIO TRACKER ==========")
        print("1. View Available Stocks")
        print("2. Buy Stock")
        print("3. Sell Stock")
        print("4. View Portfolio")
        print("5. Exit")
        print("==============================================")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            show_stocks()

        elif choice == "2":
            buy_stock()

        elif choice == "3":
            sell_stock()

        elif choice == "4":
            show_portfolio()

        elif choice == "5":
            print("\n👋 Thank you for using Stock Portfolio Tracker!")
            break

        else:
            print("❌ Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()