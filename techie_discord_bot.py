import discord
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont
import pyjokes
from quotes import Quotes
import wikipedia
from animals import Animals
import emojis
from covid import Covid
import pywhatkit as kit
import requests
from googletrans import Translator
from imdb import IMDb
import pyfiglet
import os
l=[]
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
def fig(text):
    word=pyfiglet.figlet_format(text)
    return word
from pycricbuzz import Cricbuzz
import json
c = Cricbuzz()
matches = c.matches()
#print (json.dumps(matches,indent=4))

def live_score(mid):
    c = Cricbuzz()
    lscore = c.livescore(mid)
    return (json.dumps(lscore,indent=1))

def scorecard1(mid):
    c = Cricbuzz()
    scard = c.scorecard(mid)
    #print(scard)
    return (scard)

def match_info(mid):
    c = Cricbuzz()
    minfo = c.matchinfo(mid)
    return(json.dumps(minfo,indent=1))
def commentary(mid):
    c = Cricbuzz()
    comm = c.commentary(mid)
    return(comm)
def covid(arg):
    case=str(arg)
    #covid=Covid(source="worldometers")
    covid=Covid()
    cases=covid.get_status_by_country_name(str(case))
    # for x in cases:
    #     k=x,":",cases[x]
    return(cases)
url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api_india"

headers = {
    'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com",
    'x-rapidapi-key': "051f196884mshb0072b49d1b1d36p1662d4jsn3677a45333ad"
    }

response = requests.request("GET", url, headers=headers).json()

def search_by_city(city_name):
    for each in response["state_wise"]:
        if int(response['state_wise'][each]['active'])!=0:
            for city in response['state_wise'][each]['district']:
                if city.lower()==city_name:
                    return(city,response['state_wise'][each]['district'][city]['active'])

def t1(ip):
    translator=Translator()
    n=translator.translate(ip)
    return n
def im1(m1):
    im=IMDb()
    s=im.get_top250_movies()
    if(m1<20):
        for i in range(m1):
            l.append(s[i])
    else:
        l.append(0)
    return l

def pyhton_exe(arg):
    with open('code.py','w') as code:
        arg = str(arg).replace('“','"')
        arg = str(arg).replace('”','"')
        arg = arg.replace('\n','\n    ')
        text = f"""
import sys
    
sys.stdout = open('output.txt', 'wt')
try:
    {arg}

except Exception as e: print(e)

            """
        code.write(text)

    os.system('python3 code.py')

    with open('output.txt') as output:
        l = output.readlines()
        arg=''
        for op in l:
            arg = arg + ''.join(op)

    return arg


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
async def py(ctx, *, arg):
    await ctx.send(pyhton_exe(arg))

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
@client.command()
async def covid_india(ctx,*,arg):
    await ctx.send(search_by_city(arg))
@client.command()
async def lang(ctx,*,arg):
    await ctx.send(t1(arg))
@client.command()
async def imdb_top(ctx,*,arg):
    await ctx.send(im1(int(arg)))
@client.command()
async def livescore(ctx,*,arg):
    await ctx.send(live_score(str(arg)))
@client.command()
async def score_card(ctx,*,arg):
    await ctx.send(scorecard1(str(arg)))
@client.command()
async def matchinfo(ctx,*,arg):
        await ctx.send(match_info(str(arg)))
@client.command()
async def comtry_box(ctx,*,arg):
    await ctx.send(commentary(str(arg)))
@client.command()
async def txt(ctx,*,arg):
    await ctx.send(fig(str(arg)))

## MEMEs SECTION ##    

@client.command(name='boss')
async def boss_meme(ctx, *users: discord.User):
    """
    >boss <mention_user_1> <mention_user_2>
    """
    users = list(users)
    template = Image.open(r'memes/meme_boss.jpg')
    boss = Image.open(requests.get(ctx.message.author.avatar_url, stream=True).raw).resize((120, 120))
    noob = Image.open(requests.get(users[0].avatar_url, stream=True).raw).resize((120, 120))
    challenger = Image.open(requests.get(users[1].avatar_url, stream=True).raw).resize((120, 120))
    Image.Image.paste(template, challenger, (335, 50))
    Image.Image.paste(template, noob, (500, 385))
    Image.Image.paste(template, boss, (355, 710))
    template.save('meme_boss.jpg')
    await ctx.send(file=discord.File('meme_boss.jpg'))
    os.remove('meme_boss.jpg')

@client.command(name='thakgayahu')
async def meme_vroo(ctx, *text):
    """
    >thakgayahu <message>
    """"
    message = ' '.join(list(text)).upper()
    if len(message) > 32:
        await ctx.send("``` Message Must Be Lower Than 32 Characters ```")
    else:
        template = Image.open(r'memes/meme_vro.jpg')
        user = Image.open(requests.get(ctx.message.author.avatar_url, stream=True).raw).resize((114, 114))
        Image.Image.paste(template, user, (321, 117))

        image = ImageDraw.Draw(template)
        font = ImageFont.truetype('memes/vroo_font.ttf', 50)
        # ADDS A SHADOW EFFECT TO THE TEXT
        image.text((5, 405), message, fill=(0, 0, 0), font=font)
        image.text((10, 410), message, fill=(255, 255, 255), font=font)
        template.save('meme_vroo.jpg')
        await ctx.send(file=discord.File('meme_vroo.jpg'))
        os.remove('meme_vroo.jpg')

@bot.command(name='nothisbut')
async def meme_vroo(ctx, user : discord.User, *message):
    """
    >nothisbut <mention_user> <message 1>, <message 2>
    """"
    message = ' '.join(list(message)).upper()
    up_txt = message.split(',')[0].replace(' ', '\n')
    dw_txt = message.split(',')[1].replace(' ', '\n')
    if message.split(',')[0] and message.split(',')[1] > 32:
        await ctx.send("``` Each Message Must Be Lower Than 32 Characters ```")
    else:
        template = Image.open(r'memes/meme_drake.jpg')
        user = Image.open(requests.get(user.avatar_url, stream=True).raw).resize((70, 70))
        Image.Image.paste(template, user, (23, 55))
        Image.Image.paste(template, user, (119, 267))

        image = ImageDraw.Draw(template)
        font = ImageFont.truetype('memes/vroo_font.ttf', 30)
        # ADDS A SHADOW EFFECT TO THE TEXT
        image.text((256, 0), up_txt, fill=(255, 255, 0), font=font)
        image.text((259, 3), up_txt, fill=(0, 0, 0), font=font)

        image.text((256, 251), dw_txt, fill=(255, 255, 0), font=font)
        image.text((259, 254), dw_txt, fill=(0, 0, 0), font=font)
        template.save('meme_drake.jpg')
        await ctx.send(file=discord.File('meme_drake.jpg'))
        os.remove('meme_drake.jpg')
    
client.run('api key')
