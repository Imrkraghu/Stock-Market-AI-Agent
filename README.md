# 📊 Stock Price AI

Stock Price AI is a **Gradio-powered application** that retrieves **live stock market data** using **Anthropic Claude LLM and DuckDuckGo search**. This project enables users to quickly **search for stock prices and fundamental metrics** via a simple web interface.

## 🚀 Features
- **AI-Powered Stock Search 💰**
- **Live Price Retrieval via DuckDuckGo**
- **Anthropic Claude-3 Integration**
- **Gradio Web UI for Real-Time Queries**

---

## 🛠️ Getting Started

### 🔹 **Prerequisites**
- Python 3.10+
- All required dependencies are listed in `requirements.txt`

### 🔹 **Installation**
1️⃣ **Clone the Repository**
```bash
git clone https://github.com/your-repo/Stock-Price-AI.git
cd Stock-Price-AI
```
2️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```

---

## 🏃 Running the Application
### 🔹 **Run Locally**
```bash
python app.py
```
This will generate **a local Gradio-based UI** where users can enter stock names to retrieve prices.

---

## 🎯 **Usage**
1️⃣ **Open the Gradio web UI.**  
2️⃣ **Enter the stock name (e.g., Tesla, Apple, Infosys).**  
3️⃣ **Get real-time stock price, powered by AI and web search!**  

---

## ⚡ **Example Queries**
- **Stock Price for Tesla:** `Tesla`
- **Stock Price for Apple:** `Apple`
- **Stock Price for Infosys:** `Infosys`

---

## 📜 **Requirements**
Below are the **required dependencies** for this project:

### `requirements.txt` File
```txt
gradio
fastapi
requests
uvicorn
langchain-anthropic
langchain-community
duckduckgo-search
```

### **Installation**
To install dependencies:
```bash
pip install -r requirements.txt
```

### User Interface

The main file uses Gradio to run a local web server and provide a user interface for interaction.

---
