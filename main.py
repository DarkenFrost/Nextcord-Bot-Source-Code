import nextcord
import urllib
import json
import random
import datetime
import asyncio
from nextcord.ext import commands
from datetime import datetime

TOKEN = "YOUR BOT TOKEN"

intents = nextcord.Intents.all()
intents.members = True
intents.message_content = True
intents.messages = True

bot = commands.Bot(command_prefix="?", intents=intents)
botversion = 'Beta 1.0'

def remove(afk):
    if "(AFK)" in afk.split():
        return " ".join(afk.split()[1:])

@bot.event
async def on_ready():
    print("★★★•••★•••★★★•••★•••★★★\nLogged in as "+str(bot. user)+"\nBot Id = "+str(bot.user.id)+"\n""I am in "+str(botversion)+"\n★★★•••★•••★★★•••★•••★★★")

@bot.slash_command(name="avatar", description="Avatar command which shows your avatar")
async def avatar(ctx, member: nextcord.Member = None):
    if member == None:
        member = ctx.user

    icon_url = member.avatar.url
    avatarEmbed = nextcord.Embed(title = f"{member.name}\'s Avatar")
    avatarEmbed.set_image(url = f"{icon_url}")
    avatarEmbed.set_footer(icon_url = icon_url, text=f"Requested by {member.name}#{member.discriminator}")
    await ctx.send(embed = avatarEmbed)

@bot.slash_command(name="av", description="An alias for avatar command.")
async def av(ctx, member: nextcord.Member = None):
    if member == None:
        member = ctx.user

    icon_url = member.avatar.url
    avatarEmbed = nextcord.Embed(title = f"{member.name}\'s Avatar")
    avatarEmbed.set_image(url = f"{icon_url}")
    avatarEmbed.set_footer(icon_url = icon_url, text=f"Requested by {member.name}#{member.discriminator}")
    await ctx.send(embed = avatarEmbed)

@bot.slash_command(name="meme", description="meme")
async def meme(ctx):
            memeApi = urllib.request.urlopen('https://meme-api.herokuapp.com/gimme')

            memeData = json.load(memeApi)
            memeUrl = memeData['url']
            memeName = memeData['title']
            memePoster = memeData['author']
            memeSub = memeData['subreddit']
            memeLink = memeData['postLink']

            embed= nextcord.Embed(title=memeName)
            embed.set_image(url=memeUrl)
            embed.set_footer(text=f"Meme by: {memePoster} | Post: {memeLink}")
            await ctx.send(embed=embed)

@bot.event
async def on_message(message):
    messagee = f'<@{bot.user.id}>'
    embed=nextcord.Embed(title="**Bot Info**",description=f"**I am based on slash commands. Please use /help for further information**",color=0xff6161)
    if message.content == messagee:
        await message.channel.send(embed=embed)
        return

@bot.slash_command(name="8ball", description="meme")
async def eightball(ctx,  *, question):
            responses = [
                "It is certain.",
                "It is decidedly so.",
                "Without a doubt.",
                "Yes - definitely.",
                "You may rely on it.",
                "As I see it, yes.",
                "Most likely.",
                "Outlook good.",
                "Yes.",
                "Signs point to yes.",
                "Reply hazy, try again.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don't count on it.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Very doubtful",
                "OUTRIGHT DISGUSTING!",
                "I'm 8ball, not deal with your shit ball.",
                "Dont sass me, BITCH!",
                "I'm busy doing your mom, dont you see!",
                "No, sugma balls instead",
                "Honestly, who cares?",
                "Yes, perhaps",
                "My visions are clouded, ask again.",
                "The universe says 'yes'... ",
                "Signs point to a yes!",
                "NO!, Ew, I'd rather die",
                "UNACCEPTABLE!!",
                "YESSSS!!! :GRIN:",
                "I will ignore you so hard you will start doubting your existence.",
                "Ask god, why ask me? HUH!?",
                "Yesssssssssssssss *slips in parseltongue*"
            ]
            embed = nextcord.Embed(title="8ball", description=f"Question: {question}\nAnswer: {random.choice(responses)}", color=0x00ff00)
            await ctx.send(embed=embed)

@bot.event
async def on_command_error(ctx, error):
  embed=nextcord.Embed(title=f"**Unknown Command**",description=f"**Please use ?help**",color=0xff6161)
  embed2=nextcord.Embed(title=f"**Missing Permissions**",description=f"**I do not have enough permissions to run this command.**",color=0xff6161)
  embed3=nextcord.Embed(title=f"**Missing Permissions**",description=f"**You do not have enough permissions to run this command.**",color=0xff6161)
  embed4=nextcord.Embed(title=f"**Missing Argument**",description=f"**You have not entered the complete arguments to run this command.**",color=0xff6161)
  embed5=nextcord.Embed(title=f"**Disabled Command**",description=f"**This Command has been disabled. Please use /help**",color=0xff6161)
  if isinstance(error, commands.CommandNotFound):
        await ctx.send(embed=embed)
  elif isinstance(error, commands.BotMissingPermissions):
        await ctx.send(embed=embed2)
  elif isinstance(error, commands.MissingPermissions):
        await ctx.send(embed=embed3)
  elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(embed=embed4)
  elif isinstance(error, commands.DisabledCommand):
        await ctx.send(embed=embed5)
  else:
        raise error
        return

@bot.slash_command(name="purge", description="meme") # register bot commands using this decorator
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount: int=5):
        await ctx.channel.purge(limit=amount+1)
        embed1=nextcord.Embed(title=f"**Success**",description=f"Purged {amount} messages from {ctx.channel.mention}\n\n This message will delete in 5 seconds",color=0xffa980)
        embed2=nextcord.Embed(title=f"**Success**",description=f"Purged {amount} messages from {ctx.channel.mention}\n\n This message will delete in 4 seconds",color=0xffa980)
        embed3=nextcord.Embed(title=f"**Success**",description=f"Purged {amount} messages from {ctx.channel.mention}\n\n This message will delete in 3 seconds",color=0xffa980)
        embed4=nextcord.Embed(title=f"**Success**",description=f"Purged {amount} messages from {ctx.channel.mention}\n\n This message will delete in 2 seconds",color=0xffa980)
        embed5=nextcord.Embed(title=f"**Success**",description=f"Purged {amount} messages from {ctx.channel.mention}\n\n This message will delete in 1 second",color=0xffa980)

        message = await ctx.send(embed=embed1, delete_after=7)
        await asyncio.sleep(1)
        await message.edit(embed=embed2)
        await asyncio.sleep(1)
        await message.edit(embed=embed3)
        await asyncio.sleep(1)
        await message.edit(embed=embed4)
        await asyncio.sleep(1)
        await message.edit(embed=embed5)
        await asyncio.sleep(1)
        return

@bot.slash_command(name="kick", description="meme")
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : nextcord.Member,*,reason=None):
  await member.kick(reason=reason)
  embed=nextcord.Embed(title=f"**User was kicked**",description=f"{member.name} was kicked.\nFor Reason **{reason}**",color=0x61b3ff)
  await ctx.send(embed=embed)

@bot.slash_command(name="channelstats", description="meme")
@commands.bot_has_guild_permissions(manage_channels=True)
async def channelstats(ctx):
        """
        Sends a nice fancy embed with some channel stats
        !channelstats
        """
        channel = channel
        embed = nextcord.Embed(title=f"Stats for **{channel.name}**", description=f"{'Category: {}'.format(channel.category.name) if channel.category else 'This channel is not in a category'}", color=0xffa980)
        embed.add_field(name="Guild", value=ctx.guild.name, inline=False)
        embed.add_field(name="Id", value=channel.id, inline=False)
        embed.add_field(name="Topic", value=f"{channel.topic if channel.topic else 'No topic.'}", inline=False)
        embed.add_field(name="Position", value=channel.position, inline=False)
        embed.add_field(name="Slowmode Delay", value=channel.slowmode_delay, inline=False)
        embed.add_field(name="NSFW", value=channel.is_nsfw(), inline=False)
        embed.add_field(name="News", value=channel.is_news(), inline=False)
        embed.add_field(name="Creation Time", value=channel.created_at, inline=False)
        embed.add_field(name="Permissions Synced", value=channel.permissions_synced, inline=False)

        await ctx.send(embed=embed)
        return

@bot.command()
@commands.bot_has_guild_permissions(manage_channels=True)
async def channelstats(ctx):
        """
        Sends a nice fancy embed with some channel stats
        !channelstats
        """
        channel = channel
        embed = nextcord.Embed(title=f"Stats for **{channel.name}**", description=f"{'Category: {}'.format(channel.category.name) if channel.category else 'This channel is not in a category'}", color=0xffa980)
        embed.add_field(name="Guild", value=ctx.guild.name, inline=False)
        embed.add_field(name="Id", value=channel.id, inline=False)
        embed.add_field(name="Topic", value=f"{channel.topic if channel.topic else 'No topic.'}", inline=False)
        embed.add_field(name="Position", value=channel.position, inline=False)
        embed.add_field(name="Slowmode Delay", value=channel.slowmode_delay, inline=False)
        embed.add_field(name="NSFW", value=channel.is_nsfw(), inline=False)
        embed.add_field(name="News", value=channel.is_news(), inline=False)
        embed.add_field(name="Creation Time", value=channel.created_at, inline=False)
        embed.add_field(name="Permissions Synced", value=channel.permissions_synced, inline=False)

        await ctx.send(embed=embed)
        return

@bot.slash_command(name="serverinfo", description="Get a guild's information/stats.")
async def serverinfo(ctx):
    def format_time(time):
        return time.strftime("%m/%d/%Y")

    owner = str(ctx.guild.owner)
    roles = len(ctx.guild.roles)
    memberCount = str(ctx.guild.member_count)
    voice = len(ctx.guild.voice_channels)
    channel = len(ctx.guild.channels)
    category = len(ctx.guild.categories)
    id = str(ctx.guild.id)

    icon = str(ctx.guild.icon.url)

    embed = nextcord.Embed(color=nextcord.Colour.random()
    )
    embed.set_author(icon_url=icon, name=f'{ctx.guild.name}')
    embed.set_thumbnail(url=icon)
    embed.add_field(name="**Owner**", value=owner, inline=True)
    embed.add_field(name="**Categories**", value=category, inline=True)
    embed.add_field(name="**Text Channels**", value=channel, inline=True)
    embed.add_field(name="**Voice Channels**", value=voice, inline=True)
    embed.add_field(name="**Members**", value=memberCount, inline=True)
    embed.add_field(name="**Roles**", value=roles, inline=True)
    embed.set_footer(text=f"ID: {id} | Server created • {format_time(ctx.guild.created_at)}")

    await ctx.send(embed=embed)

@bot.slash_command(name="ban", description="Bans a member from the guild")
@commands.has_permissions(administrator=True)
async def ban(ctx, member : nextcord.Member,*,reason=None):
  await member.ban(reason=reason)
  embed=nextcord.Embed(title=f"**User was banned**",description=f"{member.name} was banned.\nFor Reason **{reason}**",color=0x61b3ff)
  await ctx.send(embed=embed)

@bot.slash_command(name = "poll", description="Poll command")
async def poll(ctx,*,message):

    emb=nextcord.Embed(title="❗Poll❗", description=f"{message}", timestamp = datetime.now(),color = 0x91fff2)
    emb.set_footer(text=f"Requested By {ctx.user.name}")
    msg=await ctx.channel.send(embed=emb)
    await msg.add_reaction('1️⃣')
    await msg.add_reaction('2️⃣')

bot.run(f'{TOKEN}')
