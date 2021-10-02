import asyncio
import discord
from discord import channel
from discord import colour
from discord.embeds import Embed
import requests
import json
import random
client = discord.Client()

# get random anime facts
def get_fax():
    url = "https://airi1.p.rapidapi.com/fact"

    headers = {
        'auth': "182720a05a3766ca59d00c5ec46e8a3cd793d0aee852",
        'x-rapidapi-key': "4fdebbade4msh8568e7f28f6d9acp1d7b97jsn66f10976032e",
        'x-rapidapi-host': "airi1.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers)
    print(response.json())

    return response.json()


# get random anime cute characters
def get_waifu():
    url = "https://airi1.p.rapidapi.com/waifu"

    headers = {
        'auth': "182720a05a3766ca59d00c5ec46e8a3cd793d0aee852",
        'x-rapidapi-key': "4fdebbade4msh8568e7f28f6d9acp1d7b97jsn66f10976032e",
        'x-rapidapi-host': "airi1.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers)

    return response.json()



#get random anime quotes
def get_quote():
    

    url = "https://airi1.p.rapidapi.com/quote"

    headers = {
        'auth': "182720a05a3766ca59d00c5ec46e8a3cd793d0aee852",
        'x-rapidapi-key': "4fdebbade4msh8568e7f28f6d9acp1d7b97jsn66f10976032e",
        'x-rapidapi-host': "airi1.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers)

    print(response.json())
    return response.json()
    
#get naruto chracter details
def nrt_character(name):
    _name = name
    print(str(_name))
    query = '''
    {
    characters(filter: {name:" ''' +str(_name) +'''"}) {
        info {
        count
        pages
        next
        prev
        }    
        results {
        _id
        name
        avatarSrc
        description
        rank
        village
        }
    }
    }
    '''
    print(query)
    url = 'http://narutoql.com/graphql?query='+ query
    # print(query)
    r = requests.get(url)
    print(r.status_code)
    print(r.text)
    resp = r.json()
    if resp["data"]["characters"]["info"]["count"] == 0:
        return False
    else:
        return resp



#get naruto village details
def nrt_village(name):
    _name = name
    print(str(_name))
    query = '''
    {
  characters(filter: {village:"''' +str(_name) + '''"}) {
    info {
      count
      pages
      next
      prev
    }
    results {
      _id
      name
      avatarSrc
      description
      rank
      village
    }
  }
}
    '''
    print(query)
    url = 'http://narutoql.com/graphql?query='+ query
    # print(query)
    r = requests.get(url)
    print(r.status_code)
    print(r.text)
    resp = r.json()
    if resp["data"]["characters"]["info"]["count"] == 0:
        return False
    else:
        return resp


#get naruto rank details
def nrt_rank(rank, village):
   
    print(str(rank))
    query = '''
    {
  characters(filter: {village:"''' +str(village)+ '''",''' +'''rank:"''' + str(rank) +'''"}) {
    info {
      count
      pages
      next
      prev
    }
    results {
      _id
      name
      avatarSrc
      description
      rank
      village
    }
  }
}
    '''
    print(query)
    url = 'http://narutoql.com/graphql?query='+ query
    # print(query)
    r = requests.get(url)
    print(r.status_code)
    print(r.text)
    resp = r.json()
    if resp["data"]["characters"]["info"]["count"] == 0:
        return False
    else:
        return resp



@client.event
async def on_message(message):
    if message.author == client.user :
        return 
    if message.content.startswith('$waifu'):
        rsp = get_waifu()
        print(rsp)

        embed = discord.Embed(
            title = rsp["names"]["en"],
            colour= discord.Colour.blue()
        )

        embed.set_footer(text ="from Animo")
        embed.set_thumbnail(url =rsp["images"][0])
        embed.set_image(url = rsp["images"][-1])
        embed.add_field(name="From", value=rsp["from"]["name"])
        embed.add_field(name="Type", value=rsp["from"]["type"])

        await message.channel.send(embed = embed)
        
     
    elif message.content.startswith('$fax'):
        rsp = get_fax()
    
        await message.channel.send(  "❗Fact ahead❗\n" +"**" + rsp['fact'] + "**")
    elif message.content.startswith("$quote"):
        rsp = get_quote()
        embed = discord.Embed(
            title= rsp["said"] + ":",
            description= rsp["quote"],
            colour = discord.Colour.orange()

        )
        embed.add_field(name="Anime",value=rsp["anime"])
        embed.set_footer(text="from Animo")
        await message.channel.send(embed=embed)
    elif message.content.startswith("$nrt character"):
        await message.channel.send("**" +"Please Enter Character's name :" + "**")
        def check(m):
            return m.author == message.author
        try:
            guess = await client.wait_for('message', check=check, timeout=10.0)
        except asyncio.TimeoutError:
            return  await message.channel.send("Sorry, You Took Too Long")
        rsp = nrt_character(guess.content)
        if rsp== False:
            return await message.channel.send("Sorry No Character Found")
        else:
            embed = discord.Embed(
                title = rsp["data"]["characters"]['results'][0]["name"],
                description = rsp["data"]["characters"]['results'][0]["description"],
                colour = discord.Colour.blue()
            )
            embed.set_footer(text ="from Animo")
            embed.set_thumbnail(url =rsp["data"]["characters"]['results'][0]['avatarSrc'])
            embed.set_image(url = rsp["data"]["characters"]['results'][0]['avatarSrc'])
            embed.add_field(name="Rank", value=rsp["data"]["characters"]['results'][0]["rank"])
            embed.add_field(name="Village", value=rsp["data"]["characters"]['results'][0]["village"])
            await message.channel.send(embed=embed)
    elif message.content.startswith("$nrt village"):
        await message.channel.send("**" +"Please Enter Village's name :" + "**")
        def check(m):
            return m.author == message.author
        try:
            guess = await client.wait_for('message', check=check, timeout=10.0)
        except asyncio.TimeoutError:
            return  await message.channel.send("Sorry, You Took Too Long")
        rsp = nrt_village(guess.content)
        if rsp== False:
            return await message.channel.send("Sorry No Clan Found")
        else:
            d = rsp["data"]["characters"]['results']
           
            random.shuffle(d)
            

            for item in d[:5]:
                embed = discord.Embed(
                    title = item["name"],
                    description = item["description"],
                    colour = discord.Colour.blue()
                )
                embed.set_footer(text ="from Animo")
                embed.set_thumbnail(url =item['avatarSrc'])
                embed.set_image(url = item['avatarSrc'])
                await message.channel.send(embed=embed)
    elif message.content.startswith("$nrt rank"):
        await message.channel.send("**" +"Please Enter Rank's name :" + "**")
        def check(m):
            return m.author == message.author
        try:
            rank = await client.wait_for('message', check=check, timeout=10.0)
        except asyncio.TimeoutError:
            return  await message.channel.send("Sorry, You Took Too Long")
        await message.channel.send("**" +"Please Enter Village's name :" + "**")
        try:
            village = await client.wait_for('message', check=check, timeout=10.0)
        except asyncio.TimeoutError:
            return  await message.channel.send("Sorry, You Took Too Long")


        rsp = nrt_rank(rank.content ,village.content)
        if rsp== False:
            return await message.channel.send("Sorry No Clan Found")
        else:
            d = rsp["data"]["characters"]['results']
           
            random.shuffle(d)
            

            for item in d:
                embed = discord.Embed(
                    title = item["name"],
                    description = item["description"],
                    colour = discord.Colour.blue()
                )
                embed.set_footer(text ="from Animo")
                embed.set_thumbnail(url =item['avatarSrc'])
                embed.set_image(url = item['avatarSrc'])
                
                await message.channel.send(embed=embed)
        


# get discord bot token from developer portal of discord
client.run('YOUR BOT TOKEN')