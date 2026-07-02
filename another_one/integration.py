import threading
import time
import sqlite3
import uvicorn
import requests
import json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

# --- Setup SQLite DB ---
DB_PATH = "shopsmart_api.db"
