import discord
from discord.ext import commands
import io
import subprocess

TOKEN = "{insert your token here}"
PREFIX = "!"

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.event
async def on_ready():
    print(f'Connected to {bot.user.name}')

@bot.command(name='ocr')
async def ocr_command(ctx):
    if len(ctx.message.attachments) == 0:
        await ctx.send("Please attach an image.")
        return

    ocr_results = []

    for attachment in ctx.message.attachments:
        image_bytes = await attachment.read()

        process = subprocess.Popen(['node', 'ocr.js'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate(input=image_bytes)

        ocr_results.append(stdout.decode())

    combined_text = "\n\n".join(f"OCR Result for Image {i + 1}:\n{text}" for i, text in enumerate(ocr_results))
    await ctx.send(combined_text)

bot.run(TOKEN)