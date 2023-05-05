import discord
import os
import time
import datetime
from dateutil.relativedelta import relativedelta, MO
from keep_alive import keep_alive
from discord.ext import commands
from discord.utils import get

bot = commands.Bot(
	command_prefix="!",  # Change to desired prefix
	case_insensitive=True,  # Commands aren't case-sensitive
  intents = discord.Intents.default()
)

bot.author_id = 1102963811557855304  # Change to your discord id!!!

@bot.event 
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

@bot.event
async def on_message(ctx):
  if ctx.author.bot:
    return

  member = ctx.author
  j_Y = member.joined_at.strftime("%Y")
  j_M = member.joined_at.strftime("%m")
  j_D = member.joined_at.strftime("%d")
  
  join_date = datetime.datetime(int(j_Y), int(j_M), int(j_D))
  to_date = datetime.datetime.today()
  tdiff = to_date - join_date 
  
  await ctx.channel.send(f" {member.mention} Joined {tdiff.days} , days ago")

  check_month = join_date + relativedelta(months=+1)
  mdiff =  check_month - join_date
  check_year = join_date + relativedelta(years=+1)
  ydiff = check_year - join_date


  
  await ctx.channel.send(f"Your first milestone is {check_month.date()} or {check_year.date()}")
  
  if ydiff > tdiff > mdiff:
    await ctx.channel.send("Its been a month")
    await member.add_roles(discord.utils.get(member.guild.roles, id=1103019257958252604))
    
  if tdiff > ydiff:
    await ctx.channel.send(f"Its been a year {tdiff.days} {ydiff.days}")
    await member.remove_roles(discord.utils.get(member.guild.roles, id=1103019257958252604))
    await member.add_roles(discord.utils.get(member.guild.roles, id=935562753777745960))


extensions = [
	'cogs.cog_example'  # Same name as it would be if you were importing it
]

if __name__ == '__main__':  # Ensures this is the file being ran
	for extension in extensions:
		bot.load_extension(extension)  # Loades every extension.

keep_alive()  # Starts a webserver to be pinged.
token = os.environ.get("DISCORD_BOT_SECRET") 
bot.run(token)  # Starts the bot

