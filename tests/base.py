from cliLoader.components.loader.loader import Loader
from cliLoader.components.loader.config import Config


config = Config(destination=500, width=100, color=Config.COLORS["GREEN"])
loader = Loader(config)

for x in range(0, config.destination+1):
        loader.show(f"Completed: {x}/{config.destination}", 1)
