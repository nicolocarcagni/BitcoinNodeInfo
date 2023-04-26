from datetime import datetime
import subprocess
import requests
import telepot
import json
import pytz

TOKEN = '6119835218:AAHMKgxQhjDcaN0Jyf0lj0l99wd-a0b7AxM' # Insert your token here
USERID = 736164023 # Insert your UserID here

def check_node_status():
    try:
        # Run 'bitcoin-cli getblockchaininfo'
        subprocess.check_output(['bitcoin-cli', 'getblockchaininfo'])
        return "online"
    except Exception:
        return "offline"

def get_blockchain_info():
    # Run 'bitcoin-cli getblockchaininfo'
    output = subprocess.check_output(['bitcoin-cli', 'getblockchaininfo']).decode('utf-8')

    # JSON parsing
    blockchain_info = json.loads(output)

    # Get value of 'headers', 'blocks', 'mediantime' and 'verificationprogress' from JSON
    headers = blockchain_info['headers']
    blocks = blockchain_info['blocks']
    mediantime = blockchain_info['mediantime']
    progress = blockchain_info['verificationprogress']

    # Timestamp UNIX to human readable date.
    synced_time = datetime.fromtimestamp(mediantime, pytz.timezone('Europe/Rome')) # Timezone

    return headers, blocks, synced_time, progress

def disk(): # Disk usage from df
    command = "df -h /dev/sdb"
    output = subprocess.check_output(command, shell=True)
    output = output.decode("utf-8")
    output = output.split("\n")[1]  # get useful infos
    output = output.replace("  ", " ")  # replace space
    return output

def get_btc_price():
    response = requests.get('https://api.binance.com/api/v3/ticker/price', params={'symbol': 'BTCUSDT'}) # GET request to Binance for BTC value in USD
    if response.status_code == 200:
        price = float(response.json()['price'])
        return price
    else:
        return None

def handle_command(msg, bot):
    chat_id = msg['chat']['id']
    user_id = msg['from']['id']
    command = msg['text']
    if USERID != user_id:
        bot.sendMessage(chat_id, f"⚠️*You can't use this bot*, make sure your UserID match the one declared in the source code.", parse_mode="Markdown")
        print(f"Access denied to {user_id}")
    else:
        if command == '/status':
            
            # Check node status
            node_status = check_node_status()

            if node_status == "offline":
                message = "*Here is your ₿itcoin node!*\n\n🔴 Your node is *offline*.\n"
            else:
                # Get blockchain syncing status
                headers, blocks, synced_time, progress = get_blockchain_info()

                # Welcome message using markdown
                message = "*Here is your ₿itcoin node!*\n\n🟢 Your node is *{0}*.\n\n🔗 Successfully synced until the block *{1}* / *{2}*.\n\n📅 Last Block Time: *{3}*.\n\n🔄 Sync Status: *{4:.2%}*".format(node_status, blocks, headers, synced_time.strftime("%d-%m-%Y %H:%M:%S"), progress)

            # Invia il messaggio al bot Telegram
            bot.sendMessage(chat_id, message, parse_mode="Markdown")

        elif command == '/start':
            message = f"📍 *Welcome, use /status to check your node*"
            bot.sendMessage(chat_id, message, parse_mode='Markdown')

        elif command == '/uptime':
            output = subprocess.check_output(['uptime']).decode('utf-8')
            message = f"⏰ *Uptime:* {output.strip()}"
            bot.sendMessage(chat_id, message, parse_mode='Markdown')
        
        elif command == '/disk':
            output = disk()
            message = f"💾 *Disk:* {output}\n                                  Size|Used|Avail|Use%|Mounted on"
            bot.sendMessage(chat_id, message, parse_mode='Markdown')
        
        elif command == '/price':
            price = get_btc_price()
            if price is not None:
                message = f"💰 BTC/USD price on Binance: *{price:.2f}$*."
            else:
                message = f"⚠️ *An error occurred!*"
            bot.sendMessage(chat_id, message, parse_mode="Markdown")

        elif command == '/ping':
            message = "🏓 *PONG!*"
            bot.sendMessage(chat_id, message, parse_mode="Markdown")
def main():
    bot = telepot.Bot(TOKEN)
    bot.message_loop({'chat': lambda msg: handle_command(msg, bot)})
    
    while True:
        pass

if __name__ == '__main__':
    main()
