import yfinance as yf
import pandas as pd

class StockPortfolio:
    def __init__(self):
        
        self.portfolio = {}
    
    def add_stock(self, ticker, shares):
       
        if ticker in self.portfolio:
            self.portfolio[ticker]["shares"] += shares
        else:
            self.portfolio[ticker] = {"shares": shares, "avg_price": self.get_stock_price(ticker)}
        print(f"{shares} shares of {ticker} added to your portfolio.")
    
    def remove_stock(self, ticker, shares):
        """Remove a stock from the portfolio."""
        if ticker in self.portfolio and self.portfolio[ticker]["shares"] >= shares:
            self.portfolio[ticker]["shares"] -= shares
            if self.portfolio[ticker]["shares"] == 0:
                del self.portfolio[ticker]
            print(f"{shares} shares of {ticker} removed from your portfolio.")
        else:
            print(f"Error: Not enough shares of {ticker} to remove or stock not found.")
    
    def get_stock_price(self, ticker):
        """Fetch the current price of a stock."""
        stock = yf.Ticker(ticker)
        stock_info = stock.history(period="1d")
        return stock_info["Close"].iloc[-1]  
    
    def track_performance(self):
        """Track and display the performance of the portfolio."""
        portfolio_value = 0
        performance = []
        
        for ticker, data in self.portfolio.items():
            current_price = self.get_stock_price(ticker)
            current_value = current_price * data["shares"]
            performance.append({
                "Ticker": ticker,
                "Shares": data["shares"],
                "Avg Price": data["avg_price"],
                "Current Price": current_price,
                "Total Value": current_value,
                "Profit/Loss": current_value - (data["avg_price"] * data["shares"])
            })
            portfolio_value += current_value
        
        performance_df = pd.DataFrame(performance)
        print("\nPortfolio Performance:")
        print(performance_df)
        print(f"\nTotal Portfolio Value: ${portfolio_value:.2f}")
    
    def get_portfolio(self):
        """View all stocks in the portfolio."""
        if not self.portfolio:
            print("Your portfolio is empty.")
            return
        portfolio_df = pd.DataFrame.from_dict(self.portfolio, orient="index")
        portfolio_df["Current Price"] = portfolio_df.index.map(self.get_stock_price)
        portfolio_df["Total Value"] = portfolio_df["shares"] * portfolio_df["Current Price"]
        portfolio_df["Profit/Loss"] = portfolio_df["Total Value"] - (portfolio_df["avg_price"] * portfolio_df["shares"])
        print("\nYour Portfolio:")
        print(portfolio_df)

# Main Function to interact with the user
def main():
    portfolio = StockPortfolio()
    
    while True:
        print("\nStock Portfolio Tracker")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. Track Portfolio Performance")
        print("4. View Portfolio")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            ticker = input("Enter the stock ticker: ").upper()
            shares = int(input("Enter the number of shares: "))
            portfolio.add_stock(ticker, shares)
        
        elif choice == "2":
            ticker = input("Enter the stock ticker: ").upper()
            shares = int(input("Enter the number of shares to remove: "))
            portfolio.remove_stock(ticker, shares)
        
        elif choice == "3":
            portfolio.track_performance()
        
        elif choice == "4":
            portfolio.get_portfolio()
        
        elif choice == "5":
            print("Exiting the portfolio tracker. Goodbye!")
            break
        
        else:
            print("Invalid option. Please try again.")

# Run the main function
if __name__ == "__main__":
    main()
