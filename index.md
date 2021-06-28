# Denzven-Graphing-Api
### Welcome! this is [Denzven-Graphing-Api](https://denzven.pythonanywhere.com/)

### 1. About the Api:

Denzven-Graphing-Api is my first flask project that plots graphs of formulas/Equations using python. i have also made and [Api-Wrapper](https://pypi.org/project/Denzven-Graphing-Api-Wrapper) (mostly for practice) to make life easy and to use this Api. also an [Example Bot](https://github.com/denzven/Denzven-Graphing-Api-Bot) 

---

### 2. How to Use the Api?

Using the Api is as simple as sending a request to the [website](https://denzven.pythonanywhere.com/) with some params such as the fourmula ,grid ,plot_stylee ,x_coord ,y_coord (and more params coming..) and the Api will return an image of the plotted Graph.

#### Example of a requested url:

> http://denzven.pythonanywhere.com/DenzGraphingApi/v1/flat_graph/test/plot?formula=x%2By&x%2By&grid=1&plot_style=3&x_coord=20&y_coord=20


![Graph Example in Firefox](https://cdn.discordapp.com/attachments/775096810963468288/859152862758961242/unknown.png)

Note:
- Base url:
    - http://denzven.pythonanywhere.com/DenzGraphingApi/v1/flat_graph/test/plot
- the formula:
    - ?formula=x%2By&x%2By
    > Note that this url is "urlencoded" using urllib.

    - what can the formula contain?
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
            - eg: 2%6=0 and 2%(10)=0

- the params: 
    - &grid=1
    > grid refers to the presence of smaller grid lines, 1 is true and 0 is false

    - &plot_style=3
    > these are a list of the default plot_styles it can range from 0-25

    - &x_coord=20
    > the value ot the x coordinate (horizontal)

    - &y_coord=20
    > the value ot the y coordinate (vertical)

---

### 3. Limitations of the Api

The api has several limitations in its use now, and is slowly getting patched/fixed.

Some Known ones:
- limitations in the formula usage: the formula must equate to zero.  
like "x+y" as input will mean the graph of "x+y=0" and it must contain bot x and y in the equation.  

I dont know of any other feel free to add them in!

---
### 4. Contributing to the Api (if you want to add changes/neaten up the code)

- [Fork the repository](https://github.com/denzven/Denzven-Graphing-Api/fork)
- Clone your fork: `git clone https://github.com/denzven/Denzven-Graphing-Api.git`
- Create your feature branch: `git checkout -b my-new-feature`
- Commit your changes: `git commit -am 'Add some feature'`
- Push to the branch: `git push origin my-new-feature`
- Submit a pull request


### 5. Known Bugs and Issue reporting

- there was a bug by putting exit() or quit() in the formula that would turn off the api.. i have tried my best to patch it

I dont know of any other feel free to add them in!

### 6. About Me

I am a 17 year old wierdo that hops on with tons of hobbies and gets bored easily. Tried out a bunch of stuff like blender3D, voxel art, making discord bots and telegram bots, basic python programs, right now i am making an Graphing API and its wrapper.
you can find more info about me [here](https://denzven.pythonanywhere.com)

Thank you! Hope You can tribute much needed support and enjoy using the api as much i did making it 😁