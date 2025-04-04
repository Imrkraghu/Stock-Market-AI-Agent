import os
import gradio as gr
from langchain_anthropic import ChatAnthropic
from langchain_community.tools import DuckDuckGoSearchRun

# Set up Anthropic API key (ensure you replace with your actual key)
os.environ["ANTHROPIC_API_KEY"] = "your_real_api_key"

# Initialize Claude LLM
llm = ChatAnthropic(model="claude-3")

# Initialize DuckDuckGo search tool
search_tool = DuckDuckGoSearchRun()

def fetch_stock_price(stock_name: str):
    """Searches the web for the latest stock price."""
    query = f"{stock_name} latest stock price"
    search_results = search_tool.run(query)
    return search_results

# Define Gradio interface
def stock_price_interface(stock_name):
    price_info = fetch_stock_price(stock_name)
    return f"Latest price info for {stock_name}: {price_info}"

# Launch Gradio app
iface = gr.Interface(
    fn=stock_price_interface,
    inputs="text",
    outputs="text",
    title="Stock Price AI",
    description="Enter a stock name to get the latest price information",
)

iface.launch(share=True)  # Enables a public URL