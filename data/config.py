from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN") 
ADMINS = env.list("ADMINS")  
GROUP_CHAT_ID = env.int("GROUP_CHAT_ID")