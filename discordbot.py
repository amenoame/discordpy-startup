import discord
import urllib.request
import json
import re

client = discord.Client()

citycodes = {
    "土浦": '080020',
    "水戸": '080010',
    "札幌": '016010',
    "仙台": '040010',
    "東京": '130010',
    "横浜": '140010',
    "名古屋": '230010',
    "大阪": '270000',
    "広島": '340010',
    "福岡": '400010',
    "鹿児島": '460010',
    "那覇": '471010',
    "嶺南": '180020',
    "嶺北": '180010',
    "静岡": '220010'
}

@client.event

async def on_ready():
    print('ログインしました')
    print('ログ中:')
    print(f'Botの名前: {client.user.name}')
    print(f'Botのid: {client.user.id}')
    print('------')

@client.event
async def on_message(message):
  if client.user != message.author:


      reg_res = re.compile("(.+)の天気は？").search(message.content)
      if reg_res:

       if reg_res.group(1) in citycodes.keys():

        citycode = citycodes[reg_res.group(1)]
        resp = urllib.request.urlopen('http://weather.livedoor.com/forecast/webservice/json/v1?city=%s'%citycode).read()
        resp = json.loads(resp.decode('utf-8'))
       
        reply = resp['location']['city']
        reply += "の天気は、\n"
        for f in resp['forecasts']:
          reply += f['dateLabel'] + "が" + f['telop'] + "\n"
        reply += "です。"


        await message.channel.send(reply)  


       else:
          reply = 'そこの天気はわかりません'
          await message.channel.send(reply)  

    
      if message.content.startswith('おはよ'):
       reply = 'おはようございます！今日も頑張ろう！'
       await message.channel.send(reply)  

      if message.content.startswith('/amazon sale'):
       reply = 'https://www.amazon.co.jp/gp/goldbox?ref_=nav_cs_gb'
       await message.channel.send(reply)

      if message.content.startswith('こんにちわ'):
       reply = 'おはようございます！今日も頑張ろう！'
       await message.channel.send(reply)

      if message.content.startswith('おはござ'):
       reply = '''おはござぁ～！'''
       await message.channel.send(reply) 

      if message.content.startswith('おやすみ'):
       reply = 'また明日ね～！おやすみ～。'
       await message.channel.send(reply)

      if message.content.startswith('こんにちは'):
       reply = 'こんにちは！'
       await message.channel.send(reply)

      if message.content.startswith('ねむい'):
       reply = 'はよねろぉおお'
       await message.channel.send(reply)
           
      if message.content.startswith('/think'):
       reply = "https://cdn.discordapp.com/attachments/557808021946761218/599519095515381781/f051.png"
       await message.channel.send(reply)

      if message.content.startswith('/comm'):
       reply = '''```       
      　「おはよう」 Botが挨拶を返す
        「こんにちは」 Botが挨拶を返す
        「ねむい」 Botが挨拶を返す（キレ気味)
        「おやすみ」 Botが挨拶を返す
        「おはござ」　Botが挨拶を返す
        上の挨拶系のものはユーザーがそのワードを言うことによって反応します
        /think 絵文字「thinking」の簡略版
        ```'''
       await message.channel.send(reply)     

client.run('NTU4MTgzNDAxODI4NjQ2OTMy.XJM2zQ.6JfgMak590dHJ66NPn9C3Iv5StA')
