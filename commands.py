from discord.ext import commands
import discord
import random
import pytz
from datetime import datetime

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

def horario_brasilia():
    fuso_horario_brasilia = pytz.timezone('America/Sao_Paulo')
    horario_atual_brasilia = datetime.now(fuso_horario_brasilia)
    horario_formatado = horario_atual_brasilia.strftime("%d-%m-%Y %H:%M:%S")
    return horario_formatado

@bot.command(name='prodígio', help='Roll de Prodígio.', aliases=["Prodígio", "Prod", "prod"])
async def prod(ctx):
    prod = random.randint(1, 10000)

    imgPlayer = ["https://64.media.tumblr.com/025aeae9e639fd300e3353993e1e3e84/b2c25907ead440a2-d4/s1280x1920/1ac0f2ea74df3faa6d5c4ecaa855d95d9a5c001f.gif", "https://i.pinimg.com/564x/b9/5c/d3/b95cd3429d971c1a9915485b347296de.jpg"]
    imgProd = ["https://64.media.tumblr.com/fe90fb11e31c84f26e1650d76404efe2/732812b37c31da07-34/s540x810/2ce9a0f1b17e89fdf1bcf9a0a58cd95d6a9577af.gif", "https://media.tenor.com/UfzsR3iHAOsAAAAM/ao-ashi-haruhisa-kuribayashi.gif"]

    if prod >= 9000:
        embed = discord.Embed(
            title="Um Gênio Desperta!",
            description="Parabéns. Acaba de tornar-se um prodígio.\nEstá pra nascer mais um craque mundial?",
            color=discord.Colour.red()
        )
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar),
        embed.set_image(url=(f"{imgProd}"))
        embed.set_footer(text=(f"{horario_brasilia()}"))
        await ctx.send(embed=embed)

    else:
        embed = discord.Embed(
            title="Um Jogador Comum",
            description="Você é apenas um jogador comum. Se quiser ter sucesso, melhor começar a treinar arduamente..."
        )
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar)
        embed.set_image(url=(f"{imgPlayer}"))
        embed.set_footer(text=(f"{horario_brasilia()}"))
        await ctx.send(embed=embed)


@bot.command(name="maestria", help="Roll de Maestria", aliases=["Maestria"])
async def maestria(ctx):
    maestria = ["Drible", "Chute", "Passe", "Dividida", "Bloqueio", "Interceptação", "Captura", "Espalme", "Previsão"]
    await ctx.send(f"Você recebeu maestria em {random.choice(maestria)}")


# Função para carregar os comandos
def setup(bot):
    bot.add_command(prod)
    bot.add_command(maestria)
