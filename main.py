import yfinance as yf


def fetch_stock_prices(ticker, start_date, end_date):
    """
    Fetch historical stock prices from Yahoo Finance.

    Args:
    - ticker: Ticker symbol of the stock (e.g., AAPL for Apple Inc.).
    - start_date: Start date of the historical data (YYYY-MM-DD).
    - end_date: End date of the historical data (YYYY-MM-DD).

    Returns:
    - A pandas DataFrame containing historical stock prices.
    """
    data = yf.download(ticker, start=start_date, end=end_date)
    return data['Close']  # Extracting only the 'Close' prices

def find_head_and_shoulders(data):
    """
    Detects head and shoulders pattern in the given time series data.

    Args:
    - data: A pandas Series containing the stock prices over time.

    Returns:
    - True if a head and shoulders pattern is found, False otherwise.
    """
    if len(data) < 5:
        return False  # Not enough data points

    # Find peaks and troughs
    peaks, troughs = [], []
    for i in range(1, len(data) - 1):
        if data[i-1] < data[i] > data[i+1]:
            peaks.append(i)
        elif data[i-1] > data[i] < data[i+1]:
            troughs.append(i)

    # Check if the pattern exists
    for i in range(1, len(peaks) - 1):
        if data[peaks[i]] > data[peaks[i-1]] and data[peaks[i]] > data[peaks[i+1]]:
            left_trough = max(trough for trough in troughs if trough < peaks[i])
            right_trough = min(trough for trough in troughs if trough > peaks[i])
            if data[left_trough] > data[right_trough]:
                return True

    return False




def testfunction():
    print("test")


def main():
    while True:
        # Prompting the user to enter a command
        command = input("Enter a command (type 'exit' to quit): ")
        if command.lower() == "help":
            testfunction()

        if command.lower() == "hs":
            ticker_symbol = "AAPL"  # Apple Inc.
            start_date = "2023-01-01"
            end_date = "2023-12-31"
            stock_prices = fetch_stock_prices(ticker_symbol, start_date, end_date)
            pattern_detected = find_head_and_shoulders(stock_prices)
            print("Head and shoulders pattern detected:", pattern_detected)

        # Checking if the user wants to exit
        if command.lower() == 'exit':
            print("Exiting the console app.")
            break  # Exit the loop and terminate the program

        # Process the command (you can add your logic here)
        print("You entered:", command)


if __name__ == "__main__":
    main()
