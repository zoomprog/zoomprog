import asyncio
from typing import Dict
import os
import discord
from discord.ext import commands
import random
import youtube_dl



bot = commands.Bot(command_prefix='$')  # префикс
bot.remove_command('help')


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

    await bot.change_presence(status=discord.Status.online, activity=discord.Game('Компилирую свои сосочки'))


@bot.command()
async def inf(ctx, arg=None):
    author = ctx.message.author
    if arg == None:
        await ctx.send(f' Введите:\n$inf общая\n$inf command')
    elif arg == 'общая':
        await ctx.send(f' Я твое будущее')
    elif arg == 'command':
        await ctx.send(f'\n$hello-приветсвие')
        await ctx.send(f'$inf-информация')
        await ctx.send(f'$inf command-команды')
        await ctx.send(f'$flip- орел или решка')
        await ctx.send(f'!(введи название города или облости) - игра в города')

    else:
        await ctx.send(f' Eror твоего мозга')


# CLEAAR COMMAND################################################################################

@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def clear(ctx, amount=100):
    await ctx.channel.purge(limit=amount)


# CLEAR HELLO
@bot.command(pass_context=True)
async def hello(ctx, amount=1):
    await ctx.channel.purge(limit=amount)

    author = ctx.message.author
    await ctx.send(f'Привет,{author.mention}! Ты бот.')


# CLEAR FLIP
@bot.command(pass_context=True)
async def flip(ctx, amount=1):
    await ctx.channel.purge(limit=amount)
    author = ctx.message.author

    await ctx.send(random.choice(['орел', 'решка']))  # игра в орла и решку


###################################################################################

# Command help##################################################################
@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def help(ctx):
    emb = discord.Embed(title='Навигация по командам')

    emb.add_field(name='{}help'.format('$'), value='Помощь по командам')
    emb.add_field(name='{}clear'.format('$'), value='Очистка чата')
    emb.add_field(name='{}inf'.format('$'), value='Информация')
    emb.add_field(name='{}flip'.format('$'), value='GAMES:орел или решка')
    emb.add_field(name='{}user_mute'.format('$'), value='мьют в чате')
    emb.add_field(name='{}play'.format('$'), value='воиспроизвести')
    emb.add_field(name='{}stop'.format('$'), value='остановить')
    emb.add_field(name='{}resume'.format('$'), value='продолжить')
    emb.add_field(name='{}leave'.format('$'), value='выгнать')
    emb.add_field(name='{}pause'.format('$'), value='пауза')
    emb.add_field(name='{}tictactoe'.format('$'), value='GAMES:в крестики и нолики')
    emb.add_field(name='{}place'.format('$'), value='ход в крестики и нолики')

    await ctx.send(embed=emb)


################################################################################
@bot.command()
@commands.has_permissions(administrator=True)
async def user_mute(ctx, member: discord.Member):
    mute_role = discord.utils.get(ctx.message.guild.roles, name='mute')

    await member.add_roles(mute_role)
    await ctx.send(f'У{member.mention},ограничение чата, за нарушение прав!')


# новым участникам выдача ролей
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(775841125298339891)

    role = discord.utils.get(member.guild.roles, id=774943995189002250)

    await member.add_roles(role)
    await channel.send(
        embet=discord.Embed(description=f'Пользователь{member.name},присоединился к нам!', color=0x0c0c0c))


# отправка личных сообщений

@bot.command()
async def sikret(ctx, member: discord.Member):
    await member.send(f'{member._name},го мм ')


# Music
@bot.command()
async def play(ctx, url : str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current playing music to end or use the 'stop' command")
        return

    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name=ctx.author.voice.channel.name)
    await voiceChannel.connect()
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))


@bot.command()
async def leave(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")


@bot.command()
async def pause(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Currently no audio is playing.")


@bot.command()
async def resume(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("The audio is not paused.")


@bot.command()
async def stop(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    voice.stop()




player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

@bot.command()
async def tictactoe(ctx, p1: discord.Member, p2: discord.Member):
    global count
    global player1
    global player2
    global turn
    global gameOver

    if gameOver:
        global board
        board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:"]
        turn = ""
        gameOver = False
        count = 0

        player1 = p1
        player2 = p2

        # print the board
        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]

        # determine who goes first
        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            await ctx.send("It is <@" + str(player1.id) + ">'s turn.")
        elif num == 2:
            turn = player2
            await ctx.send("It is <@" + str(player2.id) + ">'s turn.")
    else:
        await ctx.send("Игра уже идет! Закончите его, прежде чем начинать новый.")

@bot.command()
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver

    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:" :
                board[pos - 1] = mark
                count += 1

                # print the board
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winningConditions, mark)
                print(count)
                if gameOver == True:
                    await ctx.send(mark + " wins!")
                elif count >= 9:
                    gameOver = True
                    await ctx.send("Это галстук!")

                # switch turns
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.send("Обязательно выберите целое число от 1 до 9 (включительно) и неотмеченную плитку.")
        else:
            await ctx.send("Это не твоя очередь.")
    else:
        await ctx.send("Пожалуйста, начните новую игру, используя команду !tictactoe.")


def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True

@tictactoe.error
async def tictactoe_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please mention 2 players for this command.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to mention/ping players (ie. <@688534433879556134>).")

@place.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please enter a position you would like to mark.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to enter an integer..")

bot.run('')