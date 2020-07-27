import logging
import sys
import time
from datetime import datetime
from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.start_time = datetime.now().replace(microsecond=0)




def setup(bot):
    bot.add_cog(Help(bot))
