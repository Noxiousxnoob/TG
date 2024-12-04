pimport os, time, re

id_pattern = re.compile(r'^.\d+$') 


class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "24269862")  # ⚠️ Required
    API_HASH  = os.environ.get("API_HASH", "5b1a646f8c8ed40f15af84c9b2dfa9e8") # ⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7762669342:AAFSMNMxx2HPNn7l6z2e-EuO_smwwIP33M0") # ⚠️ Required
    FORCE_SUB = os.environ.get('FORCE_SUB', 'NoxBots') # ⚠️ Required
    AUTH_CHANNEL = int(FORCE_SUB) if FORCE_SUB and id_pattern.search(
    FORCE_SUB) else None
   
    # database config
    DB_URL  = os.environ.get("DB_URL", "mongodb+srv://nox:nox@nox.0erqdpv.mongodb.net/?retryWrites=true&w=majorityl")  # ⚠️ Required
    DB_NAME  = os.environ.get("DB_NAME","SnowEncoderBot") 

    # Other Configs 
    ADMIN = int(os.environ.get("ADMIN", "5154912723")) # ⚠️ Required
    LOG_CHANNEL = int(os.environ.get('LOG_CHANNEL', '-1002052189895')) # ⚠️ Required
    BOT_UPTIME = BOT_UPTIME  = time.time()
    START_PIC = os.environ.get("START_PIC", "https://graph.org/file/15e82d7e665eccc8bd9c5.jpg")

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8080"))


    caption = """
**File Name**: {0}

**Original File Size:** {1}
**Encoded File Size:** {2}
**Compression Percentage:** {3}

__Downloaded in {4}__
__Encoded in {5}__
__Uploaded in {6}__
"""
