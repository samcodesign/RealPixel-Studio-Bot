import logging
import sys
import time
from datetime import datetime

import discord
from discord.ext import commands

VERSION = (
    f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
)


class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.start_time = datetime.now().replace(microsecond=0)

    @commands.Cog.listener()
    async def on_ready(self):
        logging.info(f"{type(self).__name__} Cog ready.")

    @commands.command()
    async def ping(self, ctx):
        """`{prefix}ping` - *Current ping and latency of the bot*"""
        embed = discord.Embed()
        before_time = time.time()
        msg = await ctx.send(embed=embed)
        latency = round(self.bot.latency * 1000)
        elapsed_ms = round((time.time() - before_time) * 1000) - latency
        embed.add_field(name="ping", value=f"{elapsed_ms}ms ")
        embed.add_field(name="latency", value=f"{latency}ms")
        await msg.edit(embed=embed)

    @commands.command()
    async def uptime(self, ctx):
        """`{prefix}uptime` - *Current uptime of the bot*"""
        current_time = datetime.now().replace(microsecond=0)
        embed = discord.Embed(
            description=f"Time since I went online: {current_time - self.start_time}."
        )
        await ctx.send(embed=embed)

    @commands.command()
    async def starttime(self, ctx):
        """`{prefix}starttime` - *Start time of the bot*"""
        embed = discord.Embed(description=f"I'm up since {self.start_time}.")
        await ctx.send(embed=embed)

# TODO: THIS DAMN SHIT ISN'T WORKING YET (INFO COMMAND)
    @commands.command()
    async def info(self, ctx):
        """`{prefix} info` - *Get Bot info*"""
        embed = discord.Embed(title="Real Pixel Studio Bot", color= discord.Colour.blurple())
        embed.add_field(
            name="Software Versions",
            value=f"```py\n"
            f"Python: {VERSION}```",
            inline=False,
        )
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Utility(bot))
