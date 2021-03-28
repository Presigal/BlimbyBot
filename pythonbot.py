
#using the Discord.py API, can be found in the following link
#https://discordpy.readthedocs.io/en/latest/index.html
#Created by Alejandro Cespedes, 3/15/2021

import discord

client = discord.Client()

commandString = ""

@client.event 
async def on_ready():

    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    #To prevent recursion, this line prevents the bot from responding to itself
    if message.author == client.user:
        return
        
    #If someone sends a bot command in the wrong discord, the bot deletes it and will paste the command in the appropiate channel
    if (message.content.startswith('!')):
        await message.delete()
        await message.channel.send("Ahahah, you didnt type the magic word")
        return

    #Testing returning name of guild, to then return the channel names
    #This section will create a music channel if one does not exist already
    if (message.content == "post in music"):
        try:
            await guild.get_channel("music")
        except NameError:
            await message.channel.send("Music channel does not exist")
        except:
            await message.channel.send("unknown error has occured. Please try again")

        
        

#discord token goes here
client.run('')
