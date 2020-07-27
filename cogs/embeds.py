import discord
from discord.ext import commands


class Embeds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def display_embed(self, ctx):
        embed = discord.Embed(
            title='Real Pixel Studio',
            description='This is the description',
            colour=discord.Colour.blue()
        )
        embed.set_footer(text='By Sam')
        embed.set_image(url='')
        embed.set_author(name='Author', icon_url='')
        embed.add_field(name='field name', value='value', inline=False)
        embed.add_field(name='field name', value='value', inline=True)
        embed.add_field(name='field name', value='value', inline=True)

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Embeds(bot))
