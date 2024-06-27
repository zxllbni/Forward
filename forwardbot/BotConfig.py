from os import environ
class Config(object):
    API_ID = environ.get("API_ID", "26555614")
    API_HASH = environ.get("API_HASH", "93bf5cde23435bb236066dcd7358ae6a")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7250959737:AAEoq5PaAlZU5e83utVh6QUEX75NTgiYpIQ")
    STRING_SESSION = environ.get("STRING_SESSION", "BQGVNN4AFuXM7wtOSvgsFdTMot2SlDySQMt_KTiyam2AutVAjQ2JsJNW7YWfkN7BER9BKVyeJ_9KWynU5sB2sk81IpiZEJwB9e4Y98hKd3OquMP6niT_4dBLlKWixmD2n5LV4NW2HISFH07tigsEnpzKq7U60IXDGbHUkpGiNVH7nOI3lJfAOfjbo8xwSdT_V2syAX4WboRbv0vY9LCFd4JxuJuFRcmzvy-EvjfvTaLxMFWnxyF7683K9Fj8njy4-JM65akQw1xqDBcEmTZovGvqLwf5vHJ_Y88hMdRUL-eEOwbUX_TWwEUgJ_uK3efwQIlCSAPOqhih71OYoj4YKIs38duuwgAAAAGBfkSMAA")
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
