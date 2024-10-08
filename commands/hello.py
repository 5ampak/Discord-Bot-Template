import discord
from discord import app_commands

# Discord slash command for say hello
async def setup(tree: app_commands.CommandTree, guild_id: int):
    @tree.command(
        name="hello",
        description="Say Hello",
        guild=discord.Object(id=guild_id)
    )
    async def hello(interaction: discord.Interaction):
        await interaction.response.send_message("Hello!")