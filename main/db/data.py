import sqlite3
import os.path
def get_db_connection():
  BASE_DIR = os.path.dirname(os.path.abspath(__file__))
  conn = sqlite3.connect(BASE_DIR+'/database.db')
  conn.row_factory = None
  return conn
