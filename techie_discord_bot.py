import discord
from discord.ext import commands
import os
def hellow():
    return "print('hello world')"
def binodw():
    return ("binod\n")

client = commands.Bot(command_prefix=">")

@client.event

async def on_ready():
    print("bot is ready")

@client.command()
async def hello(ctx):
    await ctx.send("hey pythoneer how are you :)")
@client.command()
async def fine(ctx):
    await ctx.send("that is really good :):)")
@client.command()
async def dsa_course(ctx):
    await ctx.send("https://drive.google.com/drive/mobile/folders/1ndpfnGW4ed-hxqFuyZ2aMyuc6MseOdCx/1szZmcER2CjAFbcqCLitTn_4nyv0wxUjn?sort=13&direction=a")
@client.command()
async def drive(ctx):
    await ctx.send("https://drive.google.com/drive/folders/1TjR6Hj9uontTLk9B-ZB8Ib_rTnz8XuPA?usp=sharing ")
@client.command()
async def python_basic(ctx):
    await ctx.send(hellow())
@client.command()
async def binod(ctx):
    await ctx.send(binodw())
    await ctx.send(binodw())
    await ctx.send(binodw())
    await ctx.send(binodw())
    await ctx.send(binodw())
    await ctx.send(binodw())

@client.command()
async def script(ctx, *, arg):
    with open('code.py','w') as code:
        arg = str(arg).replace('“','"')
        arg = str(arg).replace('”','"')
        text = f"""
import sys
    
sys.stdout = open('output.txt', 'wt')
{arg}
            """
        code.write(text)

    os.system('python3 code.py')

    with open('output.txt') as output:
        l = output.readlines()
        arg=''
        for op in l:
            arg = arg + ''.join(op)
        await ctx.send(arg)

client.run('api key')
