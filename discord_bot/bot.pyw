
import os , sys , subprocess , discord , token_data
py_filepath = 'discord_bot/opener.pyw'
bot = discord.Client(intents=discord.client.Intents.default())
def opener():
    args = '"%s" "%s" "%s"' % (sys.executable,                  # command
								py_filepath,                     # argv[0]
								os.path.basename(py_filepath))   # argv[1]

    proc = subprocess.run(args)

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