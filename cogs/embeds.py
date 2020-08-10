import discord
from discord.ext import commands


class Embeds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def embed(self, ctx):
        embed = discord.Embed(
            title='Real Pixel Studio',
            description='Thank you for accepting our invitation and welcome to Real Pixel Studio',
            colour=discord.Colour.blurple()
        )
        embed.set_footer(text='By Sam & Moh')
        embed.set_image(url='https://cdn.discordapp.com/attachments/734563166775935016/737463765498593371/organi.jpg')
        embed.set_author(name='RPS Bot', icon_url='https://cdn.discordapp.com/attachments/734563166775935016/737464407629627492/Artboard_18.png')
        embed.add_field(name='What Now?', value='we will have a long journey on making this gamedev startup \
                                                dream come true please choose the field that you are mostly capable \
                                                of helping in', inline=False)
        embed.add_field(name='Choose your CARACTERE', value='COM, PROG, ART, DESIGN (Wanted to sound like an RPG but...)', inline=True)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Embeds(bot))
