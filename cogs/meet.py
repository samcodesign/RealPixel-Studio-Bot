import discord
from discord.ext import commands


class Meet(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def meeting(self, ctx):
        embed = discord.Embed(
            title='Metting#5 AT 9PM',
            description='The plan @here',
            colour=discord.Colour.blurple()
        )
        embed.set_footer(text='By @Co-Founders')
        embed.set_author(
            name='RPS Bot', icon_url='https://cdn.discordapp.com/attachments/734563166775935016/737464407629627492/Artboard_18.png')
        embed.add_field(name='4- Feature Set:', value='A List of all major Elements\n Can be non-functional things (build, tools and dev related stuff)\n Everything necessary to ship\n What matters most for every feature -> the main goal of the feature\n What Cannot be compromised\n Guide your decision making', inline=False)
        embed.add_field(name='5- Elevator Pitch', value='', inline=True)
        embed.add_field(name='6- Development:', value='https://www.youtube.com/watch?v=a7vZFiFLw-w', inline=False)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Meet(bot))
