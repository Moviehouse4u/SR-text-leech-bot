import os

API_ID    = os.environ.get("25216035", "")
API_HASH  = os.environ.get("49f43d961586a02803de09571b345eb2", "")
BOT_TOKEN = os.environ.get("7353698989:AAGH-yqxXXfrCackrxlVYunop6LBtOQlPWY", "") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
