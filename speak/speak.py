from random import choice as randchoice
from discord.ext import commands

rules = {
	1 : "In sims 4 i have a house with a side shed designated specifically for us to fuck in",
	2 : "I went to KFC at 3 AM and now i can never come home.",
	3 : "Maybe the real Resurgemus was the friends I made along the way.",
	4 : "What if you wanted to go to heaven but God said you have to fuck Colonel Sanders.",
	5 : "..chinkin nunget....",
	6 : "dio brando copied me in stardust crusaders im suing",
	7 : ":3"
	8 : "I'm going to take this blade, see, and shove it right up your ass."
	9 : "Nat, when is my other mommy coming home...?"
	10 : "The American Dream is dead, its blood on my hands.",
	11 : "When Nat kills herself, just know I'm all 13 of the reasons why",
	12 : "I'd say im pretty finger-lickin' good, ain't I Mr. Colonel?",
	13 : "Hey Siri call the suicide hotline.",
	14 : "Mr. Colonel do you remember where you put the lube grease?",
	15 : "Fuck you",
	16 : "This is a CLOWN-FREE zone",
	17 : "Will eat ass 4 KFC.",
	18 : "I killed God and all I got was this stupid tshirt.",
	19 : "Your eBay code is KFCJEW",
	20 : "Swooce Swooce",
	21 : "UwU...OwO",
	22 : "I came, I saw, I fucked you raw,",
	23 : "Can that bitch William say he gets as much pussy as me?",
	24 : "Can flextape seal my broken heart?",
	25 : "I don't have a soul but I do have: knives, a sugar colonel, guy fieri's toes,",
	26 : "What in the Kentucky Fried Fuck",
	27 : "H-Hey wanna see my beybade collection it's in the back behind the grease vat-",
	28 : "I showed you my tendies please respond,",
	29 : "Why yes Colonel, I HAVE been naughty,",
	30 : "H",
	
	
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
