import sys
import os

# Add the project root to sys.path so that news_navigator can be imported
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from news_navigator.main import app

# This is the entry point for Vercel
# The app instance is what Vercel will use
