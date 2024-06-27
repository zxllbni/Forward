from os import environ
class Config(object):
    API_ID = environ.get("API_ID", "26555614")
    API_HASH = environ.get("API_HASH", "93bf5cde23435bb236066dcd7358ae6a")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7250959737:AAEoq5PaAlZU5e83utVh6QUEX75NTgiYpIQ")
    STRING_SESSION = environ.get("STRING_SESSION", "1BVtsOKEBu8YRuj9QiEDi_2yvFCi-c7raOlzaiMx58dsL6sbCmbuXuV8YZyjhAIMff4sNgtFulzeb_h_uaz79mJFNmzaAwABWwiY9de0xf4rZdSFdGmcpCFh8qcQRnJM6sA3WS1JPth2L88WnYI6oSrEOkMBAy6jmCzaoo4C4P7k7ekxo4jkDA8XuDS-uN4UB-xVn0y9m2R_udqgjNygkI8w9k3yKrATAPXrQ0ETrr-6g3FGXb0ynpxGxqoRQrjG-9tYPwwBMVm57httR32-kStnaxM1T3X_SkI0NPH_3ff69U0HMyiV9PmmFN9_t3FPFye7hDRhJPDy4Pk5_CyyoDkf_CS4XA8o=")
    SUDO_USERS = environ.get("SUDO_USERS", "6467503244")
    COMMAND_HAND_LER = environ.get("COMMAND_HAND_LER", "^/")
    HELP_MSG = """
    💢 **ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅs ɪɴ ᴛʜᴇ ʙᴏᴛ ᴀʀᴇ:**
    
    🔻 **Command :** /forward
    **Usage : ** Forwards messages from a channel to other.
    🔻 **Command :** /count
    **Usage : ** Returns the Total message sent using the bot.
    🔻 **Command :** /reset
    **Usage : ** Resets the message count to 0.
    🔻 **Command :** /restart
    **Usage : ** Updates and Restarts the Bot.
    🔻 **Command :** /join
    **Usage : ** Joins the channel.
    🔻 **Command :** /help
    **Usage : ** Get the help of this bot.
    🔻 **Command :** /status
    **Usage :** Check current status of Bot.
    🔻 **Command :** /uptime
    **Usage :** Check uptime of Bot.
    
    ⭕ **ʙᴏᴛ ɪs ᴄʀᴇᴀᴛᴇᴅ ʙʏ** **@x_O4i**
    """
