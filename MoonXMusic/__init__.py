from vexaaXMusic.core.bot import Moony
from vexaaXMusic.core.dir import dirr
from vexaaXMusic.core.userbot import Userbot
from vexaaXMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
dbb()
heroku()

app = Moony()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
