import os
from discord.ext import commands
import discord
import urllib
import aiohttp

description = 'Description'
intents = discord.Intents.all()
intents.members = True
intents.presences = True
bot = commands.Bot(
    command_prefix=commands.when_mentioned_or('>'),
    intents=discord.Intents.all(),
    case_insensitive=True,
    strip_after_prefix=False,
    allowed_mentions=discord.AllowedMentions.none()
    )

@bot.event
async def on_connect():
    print("the bot is ready")

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}\n')

@bot.event
async def on_command_error(ctx, error):
    raise error

@bot.command(
    aliases = ['flatgraph','flatgr','fgraph','fgr'],
    help = ('Plot Flat graphs providing a formuala with x and y'),
    name = 'Flat_Graph',
    description = 'Plot Flat Graphs with this command',
)
async def flat_graph(self,ctx, *, input_params):
    WAITING_EMOJI = ''
    await ctx.message.add_reaction(WAITING_EMOJI)
    async with ctx.typing():
        API_BASE_LINK = 'https://denzven.pythonanywhere.com'
        ApiBaseUrl = API_BASE_LINK
        ApiBaseUrl_Flat = ApiBaseUrl + "/DenzGraphingApi/v1/flat_graph/test/plot" #Example of flat graphs
        params = input_params.split(' ')
        i = 0

        for e in params:
            if i == 0:
                e = urllib.parse.quote(e, safe='')
                ReqUrl_Flat = ApiBaseUrl_Flat + f"?formula={e}"
                i += 1

            else:
                ReqUrl_Flat = ReqUrl_Flat + f"&{e}"

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(ReqUrl_Flat) as r:
                    
                    if "image/png" in r.headers["Content-Type"]:
                        file = open("renders/flat_graph.png", "wb")
                        file.write(await r.read())
                        file.close()
                        await ctx.reply(file=discord.File('renders/flat_graph.png'))
                        pass
                        DONE_EMOJI = ''
                        await ctx.message.add_reaction(DONE_EMOJI)
                        
                    if "application/json" in r.headers["Content-Type"]:
                        json_out = await r.json()
                        await ctx.reply(f"**Error!** \n error = {json_out['error']} \n error_id = {json_out['error_id']} \n fix = {json_out['fix']}")
                        pass
                        ERROR_EMOJI = ''
                        await ctx.message.add_reaction(ERROR_EMOJI)
                        
        except Exception as e:
            print(str(e))
    
bot.run(os.environ['bottoken'])