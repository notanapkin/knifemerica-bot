from random import choice as randchoice
from discord.ext import commands

rules = {
	NUMBER : "FLOAVOURTEXT",
	
}

class Speak:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def speak(self, num: int=None): #edit to change command trigger
        """desc""" #edit this
		
		#remove surrounding triple quotes to enable number look ups)
		 """if num:
            if num < 1:
                await self.bot.say('errormsg')
                return
            if num > maxnum:
                await self.bot.say('errormsg')
                return
            await self.bot.say("PRETEXT {}: {}".format(num, rules[num]))
            return"""
        rule = randchoice(list(rules.keys()))
        await self.bot.say("PRETEXT {}: {}".format(rule, rules[rule])) #edit to change text that comes before
 #BE SURE BOTH PRETEXTS MATCH. Remove these comments in post if you wish!

def setup(bot):
    n = Speak(bot)
    bot.add_cog(n)