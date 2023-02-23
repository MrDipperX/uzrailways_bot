from environs import Env
import json

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN") 
ADMINS = env.list("ADMINS")  
GROUP_CHAT_ID = env.int("GROUP_CHAT_ID")
RAILWAY_API = env.str("RAILWAY_API")

HOST = env.str("HOST")
DBNAME = env.str("DBNAME")
USER = env.str("USER")
PORT = env.str("PORT")
PASSWORD = env.str("PASSWORD")



