import discord
import random
import asyncio
from discord.ext import commands
import datetime

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=';', intents=discord.Intents.all())

statuses = ["Çevrimiçi", "Rahatsız Etmeyin", "Boşta", "Görünmez"]


async def update_status():
  while True:
    status = random.choice(statuses)
    await bot.change_presence(status=discord.Status.online,
                              activity=discord.Game(name="Durum 1"))
    await asyncio.sleep(10)
    await bot.change_presence(status=discord.Status.online,
                              activity=discord.Game(name="Durum 2"))
    await asyncio.sleep(10)
    await bot.change_presence(status=discord.Status.online,
                              activity=discord.Game(name="Durum 3))
    await asyncio.sleep(10)


@bot.event
async def on_ready():
  print(f'{bot.user.name} Başarıyla açıldı!')
  bot.loop.create_task(update_status())


@bot.command()
async def ping(ctx):
  start = datetime.datetime.now()
  message = await ctx.send("Ölçüyorum")
  end = datetime.datetime.now()
  duration = (end - start).total_seconds() * 1000
  await message.edit(content=f"Gecikme süresi: {duration:.2f} ms")


bot.run('TOKEN KOYUN')
