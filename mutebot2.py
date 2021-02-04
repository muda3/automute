import discord
from discord.ext import commands
from discord.utils import get

client = discord.Client()


@client.event
async def on_ready():
    print('Logined')


@client.event
async def on_message(message):
    global voich

    # 接続
    if message.content.startswith('.s'):
        voich = await discord.VoiceChannel.connect(message.author.voice.channel)
        await message.channel.send('joined')

    # 切断
    if message.content.startswith('.d'):
        await voich.disconnect()
        await message.channel.send('ByeBye')

    # ミュート
    if message.content == ".m":
        bot_vc = message.guild.me.voice.channel  # botのいるボイスチャンネルを取得
        for member in bot_vc.members:
            await member.edit(mute=True)  # チャンネルの各参加者をミュートする
            await message.channel.send('Member muted')

    # ミュート解除
    if message.content == ".um":
        bot_vc = message.guild.me.voice.channel  # botのいるボイスチャンネルを取得
        for member in bot_vc.members:
            await member.edit(mute=False)  # チャンネルの各参加者をアンミュートする
            await message.channel.send('Member unmuted')
client.run('TOKEN')
