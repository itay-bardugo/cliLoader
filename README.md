# cliLoader

cliLoader is a simple command line progress bar
all you need to do is:
  - set the config for your progress bar, including text's, color's, width, etc..
  - locate the progress bar inside your process
  - update the component with the number of your completed steps (see the examples)

![alt text](https://raw.githubusercontent.com/itay-bardugo/cliLoader/master/cliloader.png)


### Installation

`` pip install cliLoader ``


### config class
before initiate the Loader class, you should perform some config rules:

| Field | Usage | Default Value| comments
| ------ | ------ | -----------| --------
| ``color`` | set the color of the progress bar | `white` | you can choose from the confg `COLORS` dict
| ``width`` | set the width of your progress bar| `0` | -
|``progress_char``| the main character of the progress bar | `█` | -
|``destination`` | the number that will represents the 100% process | `0` | -
|``border``| the characters at the left border and the right border | \| | -

### example for config initiating:
```
from cliLoader.components.loader.config import Config #import

config = Config(destination=500, width=100, color=Config.COLORS["GREEN"])
```
### loader class
after setting the config class, just init the loader component
 ```
 from cliLoader.components.loader.loader import Loader #import

 loader = Loader(config)
```

### display the loader
assuming our for loop is our process, and every single iteration increments our process by 1
`loader.show("progress_bar_text", 1)` method like that:
```
for x in range(0, config.destination+1):
        loader.show(f"Completed: {x}/{config.destination}", 1) # 1 = the expressions of the process progress 
```

# finally code
```
from cliLoader.components.loader.loader import Loader
from cliLoader.components.loader.config import Config


config = Config(destination=500, width=100, color=Config.COLORS["GREEN"])
loader = Loader(config)

for x in range(0, config.destination+1):
        loader.show(f"Completed: {x}/{config.destination}", 1)

```
