import discord
from discord.ext import commands


class Meet(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def meeting(self, ctx):
        embed = discord.Embed(
            title='Metting#4 AT 9PM',
            description='The plan @here',
            colour=discord.Colour.blurple()
        )
        embed.set_footer(text='By @Co-Founders')
        embed.set_author(name='RPS Bot', icon_url='https://cdn.discordapp.com/attachments/734563166775935016/737464407629627492/Artboard_18.png')
        embed.add_field(name='1- Defining our pillars:', value='Must have elements, More than a feature set\n You have to define what makes this pillars important\n Define in one sentence\n 3 to 5 design pillars\n They are no features\n What the consumer thinks of first on your title', inline=False)
        embed.add_field(name='2- Talking about the Game loop:', value='Should be funny and rewarding\n Called addiction loop\n The crux of the experience\n Ex:  Clash of Clans -> Collecting Resources, Building & Training, Batting', inline=True)
        embed.add_field(name='3- Magic Moments:', value='Shareable with friends\n Causes emotion\n Needs to be Specific\n On sentence definition\n No more than 3 - 5\n Ex: Mario Kart magic moments -> Cross a finish line (zoom of on the distance), Red shell Hit, Drift perfect', inline= False)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Meet(bot))
