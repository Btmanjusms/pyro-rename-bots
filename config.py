import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "977080")

API_HASH = os.environ.get("API_HASH", "0c20c4265501492a1513f91755acd42b")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5743083943:AAEZz749XcKTM7Mfb0srymLseTcw5rcCPnk") 

FORCE_SUB = os.environ.get("FORCE_SUB", "") 

DB_NAME = os.environ.get("DB_NAME","pyro-botz")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://abcd:abcd@cluster0.5tsradf.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/76fca600b4e03a713b625.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '2083503061').split()]
