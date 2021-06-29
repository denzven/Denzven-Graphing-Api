# Denzven-Graphing-Api
### Welcome! this is [Denzven-Graphing-Api](https://denzven.pythonanywhere.com/)

### 1. About the Api:

Denzven-Graphing-Api is my first flask project that plots graphs of formulas/Equations using python. i have also made and [Api-Wrapper](https://pypi.org/project/Denzven-Graphing-Api-Wrapper) (mostly for practice) to make life easy and to use this Api. Also an [Example Bot](https://github.com/denzven/Denzven-Graphing-Api-Bot) 

---

### 2. How to Use the API?

Using the API is as simple as sending a request to the [website](https://denzven.pythonanywhere.com/) with some params such as the formula, grid, plot_style, x_coord, y_coord (more configurable parameters is coming...) and the API will return an image of the plotted Graph.

#### Example of a requested URL:

> http://denzven.pythonanywhere.com/DenzGraphingApi/v1/flat_graph/test/plot?formula=x%2By&x%2By&grid=1&plot_style=3&x_coord=20&y_coord=20


![Graph Example in Firefox](https://cdn.discordapp.com/attachments/775096810963468288/859152862758961242/unknown.png)

Note:
- Base url:
    - http://denzven.pythonanywhere.com/DenzGraphingApi/v1/flat_graph/test/plot
- The Formula:
    - ?formula=x%2By&x%2By
    > Note that this url is "urlencoded" using urllib.

    - What can the formula contain?
        - trignometric functions:
        > sin() cos() tan() 
        - powers
        > x**2 = x²
        - Basic BODMAS           
        >   ()=Brackets,   
            /=Divide,   
            *=Mutiply,  
            +=Add,  
            -=Subtract  
        - Misc:
        >   pi=value of the const pi,  
            sqrt()=square root of the value,  
            %=modulos gives the remaider of the divsion  
            - eg: 13%3 returns 1
                  15%5 returns 0

- The Parameters: 
    - &grid=1
    > Grid refers to the presence of smaller grid lines, represent as boolean value with 1 is true, 0 is false

    - &plot_style=3
    > These are a list of the default plot_styles it can range from 0-25

    - &x_coord=20
    > The value of the x coordinate (horizontal)

    - &y_coord=20
    > The value of the y coordinate (vertical)

---

### 3. Limitations of the API

The API has several limitations in its use now, and is slowly getting patched/fixed.

Some known ones:
- Limitations in the formula usage: the formula must equate to zero. Like "x+y" as input will mean the graph of "x+y=0" and it must contain both x and y in the equation.  
- Limitations in usable functions: No Absolute function, Min, Max (yet!)
- Currently, the API uses Python's eval() function to evaluate the equations, this will be replaced in the future for the sake of performance and stability

---
### 4. Contributing to the API (if you want to add changes/neaten up the code)

- [Fork the repository](https://github.com/denzven/Denzven-Graphing-Api/fork)
- Clone your fork: `git clone https://github.com/denzven/Denzven-Graphing-Api.git`
- Create your feature branch: `git checkout -b my-new-feature`
- Commit your changes: `git commit -am 'Add some feature'`
- Push to the branch: `git push origin my-new-feature`
- Submit a pull request


### 5. Known Bugs and Issue reporting

- There was a bug by putting exit() or quit() in the formula that would turn off the api.. i have tried my best to patch it

I dont know of any other feel free to add them in!

### 6. About Me

I am a 17 years old wierdo that hops on with tons of hobbies and gets bored easily. Tried out a bunch of stuff like blender3D, voxel art, making discord bots and telegram bots, basic python programs, right now i am making an Graphing API and its wrapper.
you can find more info about me [here](https://denzven.pythonanywhere.com)

Thank you! Hope You can tribute much needed support and enjoy using the api as much i did making it 😁
