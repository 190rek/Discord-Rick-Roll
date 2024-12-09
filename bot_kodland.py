import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Cześć, jestem bot{bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 10):
    await ctx.send("he" * count_heh)

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def odejmowanie(ctx, left: int, right: int):
    """Odejmowanie two numbers together."""
    await ctx.send(left - right)

@bot.command()
async def mem(ctx):
    with open('memy/pobrane.jpg', 'rb') as f:
        # Zapiszmy przekonwertowany plik biblioteki Discord w tej zmiennej!
        picture = discord.File(f)
    await ctx.send(file=picture)


@bot.command()
async def sigma(ctx):
    await ctx.send("🗿"*random.randint(1,100))



@bot.event
async def on_ready():
    print(f"Zalogowano jako {bot.user}")

@bot.command()
async def rickroll(ctx, user: discord.User):
    """Wysyła link do Rickrolla do wybranego użytkownika."""
    try:
        await user.send("🎶 Nigdy Cię nie porzucę! 🎶 https://youtu.be/dQw4w9WgXcQ")
        await ctx.reply(f"Rickroll wysłany do {user.name}!")
    except discord.Forbidden:
        await ctx.reply(f"Nie mogę wysłać wiadomości do {user.name}. Użytkownik może mieć wyłączone DM.")


bot.run("MTMxMTAwMTQ5Mzg4ODgzMTU0OQ.GHOG7K.Huw4OAFvI6ySn6BCnsBKbrYx2noaGmQIiw6xKY")