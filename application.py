from flask import Flask
import traceback

app = Flask(__name__)

@app.route('/')
def home():
    try:
        return "✅ SmartMart is LIVE! 💛 Powered by Noor"
    except Exception as e:
        return f"❌ Error: {str(e)}\n\n{traceback.format_exc()}"
