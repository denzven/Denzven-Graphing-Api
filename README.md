# Denz-Graphing-Api
##### An awesome, **free** and open-source API for plotting graphs for any formula/equation with a wide variety of customizations and daily updates! Made with ❤️ by Denzven
# Docs 
### Install the API [Use any ONE]


* ``pip install Denzven-Graphing-Api-Wrapper``



* `pip install DenzGraphingApiWrapper-py`



* ```pip install git+https://github.com/denzven/DenzGraphingApiWrapper_py.git```

### Import it into your code
* `import DenzGraphingApiWrapper_py` | *You might want to add an `as` statement after this for better readability*

### What you **can** do with the API as of now
- [X] Create beautiful graphs using `heroku_graph(formula)` and the `py_anywhere_graph(formula)` functions 
-  *`formula`* takes a mathematical equation(say, `"2+2+5"`) in `String` object type
    #### A Sample Code
    - For General Python:
        ```py
        import DenzGraphingApiWrapper_py as api
        
        formula=input("Formula here: ")
        graph_heroku=api.heroku_graph(formula) #Returns a url
        graph_py_anywhere=api.py_anywhere_graph(formula) #Returns a url
        print(graph_heroku)
        print(graph_py_anywhere)
        ```
   - For Discord Bot development in Python:
        ```py
        import discord
        from discord.ext import commands
        bot=commands.Bot(command_prefix=">")
        
        @bot.command()
        async def creategraph(formula:str)#explicitly setting formula is a string 
            embed=discord.Embed(title="A graph") #creating a variable embed of type Discord.Embed
            embed.set_image(url=graph_heroku=api.heroku_graph(formula)) #Using graph_heroku here, you can use py_anywhere_graph as well | embed.set_image takes url as an argument which is provided by graph_heroku=api.heroku_graph(formula)
            await ctx.reply(content="Here's the graph you wanted", embed=embed, mention_author=False) #No one likes to get pinged lol | ctx.reply will make the bot reply to the trigger message, in this case ">creategraph <formula>"
            
#### Well, what are you waiting for? Start coding!

> more info at https://www.denzven.tk/Denzven-Graphing-Api/
