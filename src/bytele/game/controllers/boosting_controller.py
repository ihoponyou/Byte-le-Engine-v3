from bytele.game.fnaacm.bots.bot import Bot
from bytele.game.fnaacm.bots.support_bot import SupportBot
from bytele.game.controllers.controller import Controller

class BoostingController(Controller):

    def __init__(self):
        super().__init__()
        self.supportBot = SupportBot()

    def boosting(self, bot : Bot, supportBot : SupportBot):
        if supportBot.turned_on:
            bot.boosting(True)
        else:
            bot.boosting(False)


