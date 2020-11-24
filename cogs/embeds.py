import discord
from discord.ext import commands


class Embeds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
# embeds examples Template + Embeds welcome
    @commands.command()
    async def embed(self, ctx):
        embed = discord.Embed(
            title='Real Pixel Studio',
            description='Thank you for accepting our invitation and welcome to Real Pixel Studio',
            colour=discord.Colour.blurple()
        )
        embed.set_footer(text='samcodesign')
        embed.set_image(url='')
        embed.set_author(name='RPS Bot', icon_url='')
        embed.add_field(name='What Now?', value='', inline=False)
        embed.add_field(name='Choose your CARACTERE', value='', inline=True)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Embeds(bot))
