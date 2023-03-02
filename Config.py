import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "4450669"))
    API_HASH = os.environ.get("API_HASH", "d21881748a24cf68c65ef904673be857")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5663709234:AAEGFc2TxWh5NRdYBSeGOspFf4CCtSDg-CQ")
    STRING_SESSION = os.environ.get("STRING_SESSION", "BQBrSxGeoB_f7J_8JvbZyfKAx1OOertQ45XRXICqZrTMlvRpMokgre3ucAzLaG3oyMofF3J2Klu2MThbpah2k8I2oeTkQfwjtpPtQsH1-N3_yhXvuQF-H7Tx8jrSnBS9qINDBCM8_Os_O4atAKGDc-xL4e__tYn1pSK_TQxMu0i1hgihDGt7v8J5QuL6yN0Pz431CIvSVBo77z1rAn6ShNl09VbzNWIoAI8F0G2pJPDbDmnjHmXA2dEibQG7EAU3kxu5CiWHD35Xw8XX9aLI_PHyBwJOlDF9QbsapcANNVbcAA7IMRC36Oar7P7-DMS0V2EslRKPBSA4TfIxkRTwbrGBAAAAAWQJ3lkA")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "@sakshammusicbot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/3d8ecee0ba7dddfc6fce4.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5973335641")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', "True") # Change it to "True"
