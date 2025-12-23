import os
import gradio as gr
import yfinance as yf
from yahooquery import search
from langchain_anthropic import ChatAnthropic
from langchain_community.tools import DuckDuckGoSearchRun

# Set up Anthropic API key (replace with your actual key)
os.environ["ANTHROPIC_API_KEY"] = "your_real_api_key"

# Initialize Claude AI model
llm = ChatAnthropic(model="claude-3")

# Initialize DuckDuckGo search tool
search_tool = DuckDuckGoSearchRun()

def get_ticker_from_name(stock_name: str):
    """Searches for a stock ticker based on the company name using Yahoo Query."""
    try:
        result = search(stock_name)
        if "quotes" in result and result["quotes"]:
            return result["quotes"][0]["symbol"], result["quotes"][0]["longname"]  # Extract ticker & full name
    except Exception:
        return None, stock_name  # Return None if no ticker is found

def fetch_stock_info(stock_name_or_ticker: str):
    """Fetches latest stock price, ticker, and key financial metrics in a single function."""
    
    # Convert stock name to ticker if needed
    stock_ticker, stock_full_name = get_ticker_from_name(stock_name_or_ticker)

    if stock_ticker is None:
        return {"Error": f"Could not find ticker for '{stock_name_or_ticker}'"}

    try:
        stock = yf.Ticker(stock_ticker)
        live_price = stock.history(period="1d")["Close"].iloc[-1]

        # Fetch latest stock price via DuckDuckGo
        query = f"{stock_full_name} latest stock price"
        latest_price_info = search_tool.run(query)

        stock_data = {
            "Stock Name": stock_full_name,
            "Ticker Symbol": stock_ticker,
            "Current Price 💰": live_price,
            "Latest Web Price Info 🌍": latest_price_info  # Web search-based price lookup
        }

        return stock_data
    
    except Exception as e:
        return {"Error": f"Failed to fetch stock data: {str(e)}"}

# Define Gradio interface (new version: no allow_flagging)
iface = gr.Interface(
    fn=fetch_stock_info,
    inputs=gr.Textbox(label="Enter Stock Name or Ticker"),
    outputs=gr.JSON(label="Stock Data"),
    title="📊 Stock Price & Details Lookup",
    description="Enter a stock name or ticker to get the latest price and key financial metrics."
)

# Launch with public sharing enabled
iface.launch(share=True)