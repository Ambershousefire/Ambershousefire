
import discord , token_data , webbrowser ,win32api, win32con , time , keyboard 
bot = discord.Client(intents=discord.client.Intents.default())
def opener():
	webbrowser.open('https://aternos.org/server/',2,True)
	time.sleep(15)
	win32api.SetCursorPos((700,550))
	time.sleep(5)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,700,550,0,0)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,700,550,0,0)
	time.sleep(5)
	keyboard.press('alt')
	keyboard.press('f4')
	keyboard.release('f4')
	keyboard.release('alt')


@bot.event
async def on_ready():
	guild_count = 0

	for guild in bot.guilds:
		print(f"- {guild.id} (name: {guild.name})")

		guild_count = guild_count + 1

	print("DiscordBot is in " + str(guild_count) + " survers.")


@bot.event
async def on_message(message):
	if message.content =="*start":
		opener()
	elif message.content =="* Start":
		opener()
	elif message.content =="*Start":
		opener()
	elif message.content =="*Start ":
		opener
	if message.content =="*start ":
		opener()

bot.run(token_data.bot_token)