import discord
from discord.ext import commands
from commands import setup
import pytz
from datetime import datetime

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} está conectado(a) ao Discord!')

setup(bot)

def horario_brasilia():
    fuso_horario_brasilia = pytz.timezone('America/Sao_Paulo')
    horario_atual_brasilia = datetime.now(fuso_horario_brasilia)
    horario_formatado = horario_atual_brasilia.strftime("%d-%m-%Y %H:%M:%S")
    return horario_formatado

@bot.command(name='teste', help='test', aliases=["Teste", "Test", "test"])
async def test(ctx):
    embed = discord.Embed(
        title="Estou Funcionando!",
        description="Tudo normal por aqui, eu acho... Estou funcionando!",
        color=0xEB459F
    )
    embed.set_author(name=(f"{bot.user.name} Maravilhita"), icon_url=bot.user.avatar)
    embed.set_thumbnail(url="https://i.pinimg.com/564x/71/8c/82/718c82058e01ddfd846562fb973f5060.jpg")
    embed.set_image(url="https://i.pinimg.com/originals/f8/d9/17/f8d917dd4dd4f21fb3f6f72d814afca4.gif")
    embed.set_footer(text=(f"{horario_brasilia()}"), icon_url=bot.user.avatar)
    await ctx.send(embed=embed)

bot.run('')