import discord
from discord.ext import commands
import pyjokes
from quotes import Quotes
import wikipedia
from animals import Animals
import emojis
from covid import Covid
import os

def hellow():
    return "print('hello world')"
def binodw():
    return ("binod\n")
def img1():
    an=Animals('dog')
    return (an.image())
def wiki1(query):
    result=wikipedia.summary(query,sentences=2)
    return result
def jokes1():
    k=emojis.encode(":smile:")
    return (pyjokes.get_joke()+k*3)
def quotes1():
    quotes = Quotes()
    persons = quotes.random()
    l=str(persons[1])
    k=emojis.encode(":sunny:")
    return l+k*2


def covid(arg):
    case=str(arg)
    #covid=Covid(source="worldometers")
    covid=Covid()
    cases=covid.get_status_by_country_name(str(case))
    # for x in cases:
    #     k=x,":",cases[x]
    return(cases)
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

@client.command()
async def img(ctx):
    await ctx.send(img1())
@client.command()
async def quotes(ctx):
    await ctx.send(quotes1())
@client.command()
async def jokes(ctx):
    await ctx.send(jokes1())
@client.command()
async def wiki(ctx,*,arg):
    await ctx.send(wiki1(arg))
@client.command()
async def covid_news(ctx,*,arg):
    await ctx.send(covid(arg))
client.run('api key')
