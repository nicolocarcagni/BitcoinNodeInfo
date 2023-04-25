# BitcoinNodeInfo

This is a simple Python script that monitors the status of a Bitcoin node and provides information about its blockchain synchronization. The script can be integrated with a Telegram bot to allow users to quickly check the status of their node using a mobile device.

### Features
Check the status of a Bitcoin node (online/offline).
Display the number of headers and blocks in the Bitcoin blockchain.
Display the synchronization status of the Bitcoin blockchain.
Display the disk usage of the node.
Display the system uptime of the node.

### Prerequisites
* Python 3.6 or later.
* A running Bitcoin node.
* The bitcoin-cli tool installed and available in the system's PATH.
* Python modules in ```requirements.txt``` 

```bash
pip install -r requirements.txt
```

### Configuration
To use the script, you need to create a Telegram bot in [BotFather](https://t.me/BotFather) and obtain an access token.

```python
TOKEN = 'your_bot_token_here'
USERID = YOURUSERID
```
## Usage
To start the script, simply run the following command:

```bash
python bot.py
```

### Commands
The bot recognizes the following commands:

``` /start ``` Displays the status of the Bitcoin node and blockchain synchronization.

``` /sync ``` Displays the synchronization status of the Bitcoin blockchain.

``` /uptime ``` Displays the system uptime of the node.

``` /disk ``` Displays the disk usage of the node.

``` /ping ``` Pings the script and receives a response.

### Optional: Add commands list in BotFather

![IMG_EE7FDAF6F4E5-1](https://user-images.githubusercontent.com/64737169/234252279-75c5066a-9e15-41d7-9ef4-c35bb9cdde89.jpeg)

If you want a list of command like this 👆, use `/setcommands` in Bot Father and send the following list:


```
start - ▶️ Start the bot
status - 🔄 Sync status
uptime - ⏰ Node uptime
disk - 💾 Disk usage
```

## License
This script is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
