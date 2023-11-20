import nextcord
from nextcord.ext import commands

GUILD_ID = "1176264237153275954"
TOKEN = "MTE3NjI2MDY1MTQwOTIyMzc0Mg.GRLgkk.7f6jcxc-t-kBDBUle5Vc1K_6kx2IzWeA-A3BZw"

bot = commands.Bot()

@bot.event 
async def on_ready():
    print(f"Je me suis connecté en temps que {bot.user}")

@bot.slash_command(description="Permet d'avoir de l'aide", guild_ids=[GUILD_ID])
async def help(interaction: nextcord.Interaction):
    await interaction.send("Voici toutes les commandes du bot :")

bot.run(TOKEN)