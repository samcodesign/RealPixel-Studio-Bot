import discord
from discord.ext import commands


class Meet(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
# A command to put your meeting plan
    @commands.command()
    async def meeting(self, ctx):
        embed = discord.Embed(
            title='Metting#5 AT 9PM',
            description='The plan @here',
            colour=discord.Colour.blurple()
        )
        embed.set_footer(text='By @Co-Founders')
        embed.set_author(name='RPS Bot', icon_url='')
        embed.add_field(name='4- Feature Set:', value='', inline=False)
        embed.add_field(name='5- Elevator Pitch', value='nothing to add', inline=True)
        embed.add_field(name='6- Development:', value='', inline=False)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Meet(bot))
