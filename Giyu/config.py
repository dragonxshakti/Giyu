# Create new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open("{}/Giyu/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = "20457610" # integer value, dont use ""
    API_HASH = "b7de0dfecd19375d3f84dbedaeb92537"
    TOKEN = "6980957140:AAHywBOVsxExbyrynVyrWKDr_znO87dQjBE"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly. 
    CO_OWNER_ID = "6890857225" 
    CO_OWNER_USERNAME = "papa_of_telegram"
    OWNER_ID = "6890857225"  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "papa_of_telegram"
    BOT_USERNAME = "Cheems_x_Music_Bot"
    BOT_ID = "6980957140"
    SUPPORT_CHAT = "lamo"  # Your own group for support, do not add the @
    JOIN_LOGGER = (
        "-1001977783984"
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
        "-1001977783984"
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit

    # RECOMMENDED
    DATABASE_URL = "mongodb+srv://vinamratiwari579:IuhMTKnYMO1nR8lm@cluster0.oezxipv.mongodb.net/?retryWrites=true&w=majority"  # needed for any database modules
    LOAD = []
    NO_LOAD = "rss"
    WEBHOOK = False
    INFOPIC = True
    URL = None 
    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    THUNDERS = get_user_list("elevated_users.json", "thunders")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    FLAMES = get_user_list("elevated_users.json", "flames")
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    WINDS = get_user_list("elevated_users.json", "winds")
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    WATERS = get_user_list("elevated_users.json", "waters")
    BEASTS = get_user_list("elevated_users.json", "beasts")
#fill your id in "[]" id you wanna add two in use "[id, id]" lile this In elevated_users.json file

    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = False  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = ""  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    ALLOW_CHATS = True 
    CASH_API_KEY = (
        "7ORLW6TQGZKP8R59"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "NEIU5O1GPLQJ"  # Get your API key from https://timezonedb.com/api
    MONGO_DB_URI = "mongodb+srv://vinamratiwari579:IuhMTKnYMO1nR8lm@cluster0.oezxipv.mongodb.net/?retryWrites=true&w=majority"
    WALL_API = (
        ""  # For wallpapers, get one from 
    )
    REM_BG_API_KEY = "" 
    TEMP_DOWNLOAD_DIRECTORY = "/tmp"
    OPENWEATHERMAP_ID = ""
    TAN0UB = "" #telethon string 

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
