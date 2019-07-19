import discord

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("동전줍는 징징이")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content.startswith("안녕"):
        await message.channel.send("반가워")
    if message.content.startswith("잘가"):
        await message.channel.send("또만나")
    if message.content.startswith("앙"):
        await message.channel.send("ANG?")
    if message.content.startswith("징징이"):
        await message.channel.send("사장님!")
    if message.content.startswith("이동윤은?"):
        await message.channel.send("해석 불가능한 명령어입니다...")
    if message.content.startswith("똥유이"):
        await message.channel.send("메이플하자!")






client.run("NTk0Mzk4MjgzNzY2NjkzODg4.XRb3bA.l_4pZ5259NDlfXjP9wix4h1dpJQ")





