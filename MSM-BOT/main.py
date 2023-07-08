import modules as task
import discord
from discord.ext import commands

task.requireData()
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=['!!','!! ',',','msm','msm ',', ','/','/ '], intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command()
async def hello(ctx):
    userName = ctx.author.name
    user = discord.utils.get(ctx.guild.members, name=userName)
    await ctx.send(f'{user.mention} Hello, {userName} How Are You ?')

@bot.command()
async def start(ctx):
    userName = ctx.author.name
    user = discord.utils.get(ctx.guild.members, name=userName)
    defultBal = 5000
    if not task.isUserExist(userName):
        task.addAcc(userName,defultBal)
        await ctx.send("Congratulation "+userName+"\nYou Just Started Game\n"+"To get More Information type !!help")
    else:
        await ctx.send("You alrady started your game")


@bot.command()
async def bal(ctx):
    import os
    userName = ctx.author.name
    user = discord.utils.get(ctx.guild.members, name=userName)
    if not task.isUserExist(userName):
        message = f"Sorry, {user.mention}, \nYou are not register here,\nPlease Start your game with !!start"
        await ctx.send(message)
    else:
        await ctx.send(str(task.accdetail(userName)))


@bot.command()
async def work(ctx):
    userName = ctx.author.name
    user = discord.utils.get(ctx.guild.members, name=userName)
    file = f'{userName}.txt'
    if not task.isUserExist(userName):
        message = f"Sorry, {user.mention}, You are not register here,\nPlease Start your game with !!start"
        await ctx.send(message)
    else:
        workfile = f'{userName}_work.txt'
        from datetime import date
        if(str(date.today())==task.getLastTime(userName)):
           await ctx.send(f'Sorry, {user.mention}, \nyou can not work more than one time in one day')
        else:
            await ctx.send(f':tada:Congratulation, {user.mention}, \n You Worked Heard today and erned 250:money_with_wings:')
            bal = int(task.getBal(userName))+250
            task.editAcc(userName,bal=bal)
            task.editAcc(userName,checIn=str(date.today()))


@bot.command(name='all_names')
async def all_names(ctx):
    userName = ctx.author.name
    user = discord.utils.get(ctx.guild.members, name=userName)
    if user:
        await ctx.send('-------- All Stocks of India --------')
        stocksList =  task.allStocks()
        c=i=0
        strings = ["","","","",""]
        for stock in stocksList:
            strings[i] = strings[i] + '\n' + str(c+1) + '\t' + stock
            if (c+1)%100==0:
                i+=1
            c+=1
        # await ctx.send(string)   # this has 7185 charcters its over limit
        for string in strings:
            if string=="":
                empty+=1
                continue
            await ctx.send(string)
    else:
        await ctx.send("I think You are Hacker")

@bot.command()
async def price(ctx,stockName1="", stockName2="", stockName3=""):
    stockName = stockName1 + stockName2+stockName3
    if stockName=="" or stockName==" ":
        await ctx.send(f'Command is !!price <Your Stock Name Here>')
    else:
        stockPrice = task.givePrice(stock=stockName)
        if stockPrice == None:
            await ctx.send(f'{stockName} is not a Stock')
        else:
            await ctx.send(f'Price of {stockPrice}')

@bot.command()
async def buy(ctx,quntity="1",stockName1="", stockName2="", stockName3=""):
    StockName=stockName1+stockName2+stockName3
    userName = ctx.author.name
    name=StockName.lower().replace(' ','')
    bal = float(task.getBal(userName))
    Val = task.buy(bal,name,quntity,userName)
    await ctx.send(Val)

@bot.command()
async def sell(ctx,quntity="1",stockName1="", stockName2="", stockName3=""):
    StockName=stockName1 + stockName2+stockName3
    userName = ctx.author.name
    name=StockName.lower().replace(' ','')
    bal = float(task.getBal(userName))
    Val = task.sell(bal,name,quntity,userName)
    await ctx.send(Val)

@bot.command()
async def Stock_List(ctx,friend=""):
    userName = ctx.author.name
    if not (friend==""):
        userName=friend
    user = discord.utils.get(ctx.guild.members, name=userName)
    task.printAccStock(userName)
    image_path = "temp.jpg"  # Replace with the actual path to your image file

    with open(image_path, "rb") as f:
        image = discord.File(f)  # Create a discord.File object from the image file

    await ctx.send(file=image)
    await ctx.send(user.mention)

    
bot.run('MTA5NzIzNDQxNDA0MTMxNzM3Ng.Ga0Vgm.shbOsmE32QkR5cptQ-ba2BIapbuc-sOylmJpsc')