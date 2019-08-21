import discord as dc
from discord.ext import commands
import re
import random as rng

token = 'NjEwNjg0MDkxNTQ0ODk1NDg5.XVzFUw.r6BerXhW1KJPhACiNvSM5SQ6kc8'

client = commands.Bot(command_prefix = '$')

@client.event
async def on_ready():
    print('Inicie sesion como {0.user}'.format(client))
    

@client.event
async def on_member_update(before, after):
    lala = '377319672632180736'
    gigi = '611776954823344128'
    
    
    if str(after.status) is 'online':
        if after.id is lala:
            return await message.channel.send('Hola, <@'+str(lala)+'>! Recuerda que JRZ te quiere mucho. \:3')
        if after.id is gigi:
            return await message.channel.send('Hola, mama <@'+str(gigi)+'>! Te doy la bienvenida de vuelta al servidor. \:3')
        
    return


@client.event
async def on_message(message):
    #Ignora los mensajes que envia el mismo bot
    if message.author == client.user:
        return
    
    await client.process_commands(message)


#Limite de mensajes a borrar: 100, mensajes mas viejos a 14 dias no se pueden borrar
@client.command(pass_context = True)
async def limpiar(ctx, numero = 100):
    canal = ctx.message.channel
    mensajes = [] #Una lista vacia para poner todos los mensajes en el log
    async for x in canal.history(limit = int(numero)):
        mensajes.append(x)
        
    await canal.delete_messages(mensajes)
    
    
@client.command(pass_context = True)
async def di(ctx, *args): # *args significa que puede recibir n cantidad de argumentos
    canal = ctx.message.channel #obtenemos de cual canal fue empleado el comando
    
    frase = ' '.join(args) #Agrega un espacio entre cada uno de los argumentos recibidos. Cada palabra es tratada como un argumento
    
    #Inicio del codigo para borrar el mensaje con el comando
    mensajes = [] #Una lista vacia para poner todos los mensajes en el log
    async for x in canal.history(limit = int(1)):
        mensajes.append(x)
        
    await canal.delete_messages(mensajes)
    #Fin del codigo
    
    if args is None: #Si no hay argumentos (palabras), la funcion termina prematuramente
        return
    
    else: #De lo contrario manda el mensaje escrito hacia el canal en el que fue utilizado.
        return await ctx.send(frase)
    
@client.command(pass_context = True)
async def verfoto(ctx, arg=None):
    usuario = None #Inicializamos la variable usuario
    if arg is None: #Si no recibimos como argumento algun usuario, utilizamos al autor del mensaje como el usuario
        usuario = ctx.message.author
    else: #De lo contrario, convertimos el usuario al que se menciono en un objeto del tipo Member
        try:
            #arg es el id de usuario, no el username
            usuario = await commands.MemberConverter().convert(ctx, arg)
        except commands.BadArgument:
            await ctx.send('Por favor especifique un usuario valido')
            
    if arg == '<@371733271542759424>':
        await ctx.send('Nel, prro')
        return
    
    #Codigo para obtener y encapsular la foto de perfil en un mensaje embebido
    url_fotoUsuario = re.sub('.webp', '.png', str(usuario.avatar_url))
    embed_msg = dc.Embed(title = str(usuario), description = '[Enlace Directo]('+url_fotoUsuario+')')
    embed_msg.set_image(url=url_fotoUsuario)
    await ctx.send(embed = embed_msg)


#Comando sencillo para apagar el bot en caso de que se requiera
@client.command()
async def apagar(ctx):
    if ctx.message.author.id in [371733271542759424, 611776954823344128]:
        await ctx.send('```Apagando...```')
        await client.logout()
    else:
        await ctx.send('Tu no me mandas, al chile.')
    
client.run(token)