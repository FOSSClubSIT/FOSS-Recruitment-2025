import discord
from discord.ext import commands, tasks
import random
import asyncio
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

load_dotenv("key.env")  # load .env file
TOKEN = os.getenv("DISCORD_TOKEN")
PREFIX = "!"  # command prefix

# --- BOT SETUP ---
intents = discord.Intents.default()
intents.message_content = True
intents.members = True  # needed for moderation commands

bot = commands.Bot(command_prefix=PREFIX, intents=intents, help_command=None)

# --- EVENTS ---
@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

# --- BASIC COMMANDS ---
@bot.command()
async def ping(ctx):
    await ctx.send(f"🏓 Pong! Latency: {round(bot.latency * 1000)}ms")

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention}! 👋")

# --- FUN COMMANDS ---
@bot.command()
async def roll(ctx, sides: int = 6):
    result = random.randint(1, sides)
    await ctx.send(f"🎲 You rolled a {result}!")

@bot.command()
async def choose(ctx, *choices):
    if len(choices) < 2:
        await ctx.send("❌ Please provide at least 2 choices!")
    else:
        await ctx.send(f"🤔 I choose: {random.choice(choices)}")

@bot.command()
async def coinflip(ctx):
    await ctx.send(f"🪙 {random.choice(['Heads', 'Tails'])}")

@bot.command(aliases=["8ball", "eightball"])
async def _8ball(ctx, *, question: str):
    responses = [
        "Yes.", "No.", "Maybe.", "Definitely!", "Ask again later.",
        "I don’t think so.", "For sure!", "Unlikely."
    ]
    await ctx.send(f"🎱 {random.choice(responses)}")

@bot.command()
async def joke(ctx):
    jokes = [
        "Why don’t skeletons fight each other? Because they don’t have the guts.",
        "I told my computer I needed a break, and it said: 'No problem, I’ll go to sleep.'",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why don’t programmers like nature? Too many bugs.",
        "Why can’t you trust atoms? They make up everything!",
    ]
    await ctx.send(random.choice(jokes))

@bot.command()
async def roast(ctx, member: discord.Member = None):
    roasts = [
        "I'd explain it to you, but I don’t have any crayons.",
        "You're like a cloud. When you disappear, it’s a beautiful day.",
        "You have something on your chin… no, the third one down.",
        "I would agree with you, but then we’d both be wrong.",
        "You bring everyone so much joy… when you leave the room."
    ]
    target = member.mention if member else ctx.author.mention
    await ctx.send(f"{target}, {random.choice(roasts)}")

@bot.command()
async def hug(ctx, member: discord.Member):
    await ctx.send(f"🤗 {ctx.author.mention} hugs {member.mention}!")

@bot.command()
async def slap(ctx, member: discord.Member):
    await ctx.send(f"👋 {ctx.author.mention} slaps {member.mention}!")

@bot.command()
async def highfive(ctx, member: discord.Member):
    await ctx.send(f"🙌 {ctx.author.mention} high-fives {member.mention}!")

@bot.command()
async def ship(ctx, user1: discord.Member, user2: discord.Member):
    percentage = random.randint(0, 100)
    await ctx.send(f"💖 {user1.mention} + {user2.mention} = {percentage}% compatibility!")

@bot.command()
async def rps(ctx, choice: str):
    options = ["rock", "paper", "scissors"]
    bot_choice = random.choice(options)
    choice = choice.lower()
    if choice not in options:
        await ctx.send("❌ Choose rock, paper, or scissors!")
        return
    if choice == bot_choice:
        result = "It's a tie!"
    elif (choice == "rock" and bot_choice == "scissors") or \
         (choice == "scissors" and bot_choice == "paper") or \
         (choice == "paper" and bot_choice == "rock"):
        result = "You win!"
    else:
        result = "I win!"
    await ctx.send(f"🪨📄✂️ You chose {choice}, I chose {bot_choice}. {result}")

@bot.command()
async def guess(ctx, number: int):
    correct = random.randint(1, 10)
    if number == correct:
        await ctx.send(f"🎉 Correct! The number was {correct}.")
    else:
        await ctx.send(f"❌ Nope, it was {correct}.")

@bot.command()
async def trivia(ctx):
    questions = {
        "What’s the capital of France?": "paris",
        "2 + 2 * 2 = ?": "6",
        "What’s the largest planet in our solar system?": "jupiter"
    }
    q, a = random.choice(list(questions.items()))
    await ctx.send(f"❓ {q}")

    def check(m): return m.author == ctx.author and m.channel == ctx.channel
    try:
        msg = await bot.wait_for("message", check=check, timeout=15)
        if msg.content.lower() == a:
            await ctx.send("✅ Correct!")
        else:
            await ctx.send(f"❌ Wrong! The answer was {a}.")
    except asyncio.TimeoutError:
        await ctx.send("⌛ Too slow!")

@bot.command()
async def quote(ctx):
    quotes = [
        "Believe you can and you're halfway there.",
        "Stay positive, work hard, make it happen.",
        "Do what you can with what you have where you are.",
        "Happiness depends upon ourselves."
    ]
    await ctx.send(f"💡 {random.choice(quotes)}")

@bot.command()
async def fact(ctx):
    facts = [
        "Honey never spoils.",
        "Bananas are berries, but strawberries aren’t.",
        "Octopuses have three hearts.",
        "There are more stars in the universe than grains of sand on Earth."
    ]
    await ctx.send(f"📘 {random.choice(facts)}")

@bot.command()
async def wouldyourather(ctx):
    options = [
        "Would you rather fly or be invisible?",
        "Would you rather have unlimited money or unlimited time?",
        "Would you rather live without music or without movies?"
    ]
    await ctx.send(f"🤔 {random.choice(options)}")

@bot.command()
async def truthordare(ctx):
    options = [
        "Truth: What's your biggest fear?",
        "Truth: What's the most embarrassing thing you've done?",
        "Dare: Send a random emoji in the chat.",
        "Dare: Compliment the person above you."
    ]
    await ctx.send(f"🎲 {random.choice(options)}")

@bot.command()
async def reverse(ctx, *, text: str):
    await ctx.send(text[::-1])

@bot.command()
async def mock(ctx, *, text: str):
    result = "".join(c.upper() if i % 2 else c.lower() for i, c in enumerate(text))
    await ctx.send(result)

# --- UTILITY COMMANDS ---
@bot.command()
async def userinfo(ctx, member: discord.Member = None):
    member = member or ctx.author
    embed = discord.Embed(title=f"User Info - {member}", color=discord.Color.blue())
    embed.add_field(name="ID", value=member.id, inline=False)
    embed.add_field(name="Joined", value=member.joined_at.strftime("%Y-%m-%d"), inline=False)
    embed.add_field(name="Account Created", value=member.created_at.strftime("%Y-%m-%d"), inline=False)
    embed.add_field(name="Roles", value=", ".join([r.name for r in member.roles if r.name != "@everyone"]) or "None", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def serverinfo(ctx):
    guild = ctx.guild
    embed = discord.Embed(title=f"Server Info - {guild.name}", color=discord.Color.green())
    embed.add_field(name="ID", value=guild.id, inline=False)
    embed.add_field(name="Owner", value=guild.owner, inline=False)
    embed.add_field(name="Members", value=guild.member_count, inline=False)
    embed.add_field(name="Created", value=guild.created_at.strftime("%Y-%m-%d"), inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def avatar(ctx, member: discord.Member = None):
    member = member or ctx.author
    embed = discord.Embed(title=f"Avatar - {member}", color=discord.Color.purple())
    embed.set_image(url=member.avatar.url if member.avatar else member.default_avatar.url)
    await ctx.send(embed=embed)

@bot.command()
async def remindme(ctx, time: int, *, reminder: str):
    await ctx.send(f"⏰ Reminder set! I'll remind you in {time} seconds.")
    await asyncio.sleep(time)
    await ctx.send(f"🔔 Reminder: {reminder}")

@bot.command()
async def poll(ctx, question: str, *options):
    if len(options) < 2:
        await ctx.send("❌ Provide at least 2 options!")
        return
    if len(options) > 10:
        await ctx.send("❌ Max 10 options allowed!")
        return
    embed = discord.Embed(title=f"📊 {question}", color=discord.Color.orange())
    emojis = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]
    description = ""
    for i, option in enumerate(options):
        description += f"{emojis[i]} {option}\n"
    embed.description = description
    message = await ctx.send(embed=embed)
    for i in range(len(options)):
        await message.add_reaction(emojis[i])

# --- MODERATION COMMANDS ---
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason="No reason provided"):
    await member.kick(reason=reason)
    await ctx.send(f"👢 Kicked {member.mention} for {reason}.")

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason="No reason provided"):
    await member.ban(reason=reason)
    await ctx.send(f"🔨 Banned {member.mention} for {reason}.")

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int = 5):
    deleted = await ctx.channel.purge(limit=amount)
    await ctx.send(f"🧹 Cleared {len(deleted)} messages.", delete_after=5)

@bot.command()
@commands.has_permissions(manage_roles=True)
async def mute(ctx, member: discord.Member, time: int = 60):
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    if not role:
        role = await ctx.guild.create_role(name="Muted")
        for channel in ctx.guild.channels:
            await channel.set_permissions(role, send_messages=False, speak=False)
    await member.add_roles(role)
    await ctx.send(f"🔇 Muted {member.mention} for {time} seconds.")
    await asyncio.sleep(time)
    await member.remove_roles(role)
    await ctx.send(f"🔊 Unmuted {member.mention}!")

@bot.command()
@commands.has_permissions(manage_roles=True)
async def unmute(ctx, member: discord.Member):
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    if role in member.roles:
        await member.remove_roles(role)
        await ctx.send(f"🔊 Unmuted {member.mention}!")

@bot.command()
@commands.has_permissions(manage_messages=True)
async def warn(ctx, member: discord.Member, *, reason="No reason provided"):
    await ctx.send(f"⚠️ {member.mention} has been warned: {reason}")

# --- MENU / HELP COMMAND ---
@bot.command(name="menu")
async def menu(ctx):
    embed = discord.Embed(title="📜 Helix Command Menu", color=discord.Color.gold())
    embed.set_thumbnail(url=bot.user.avatar.url if bot.user.avatar else None)
    embed.add_field(name="⚙️ Basic", value="`!ping` • `!hello`", inline=False)
    embed.add_field(
        name="🎲 Fun & Games",
        value=("`!roll` • `!choose` • `!coinflip` • `!eightball` • `!joke` • `!roast`\n"
               "`!hug` • `!slap` • `!highfive` • `!ship` • `!rps` • `!guess` • `!trivia`"),
        inline=False
    )
    embed.add_field(
        name="🌟 Interactive / Cool",
        value=("`!quote` • `!fact` • `!wouldyourather` • `!truthordare`\n"
               "`!reverse` • `!mock`"),
        inline=False
    )
    embed.add_field(name="🛠 Utility", value="`!userinfo` • `!serverinfo` • `!avatar` • `!remindme` • `!poll`", inline=False)
    embed.add_field(name="🔧 Moderation", value="`!kick` • `!ban` • `!clear` • `!mute` • `!unmute` • `!warn`", inline=False)
    embed.set_footer(text="Helix Bot • Type a command to get started!")
    await ctx.send(embed=embed)

# --- RUN BOT ---
bot.run(TOKEN)
