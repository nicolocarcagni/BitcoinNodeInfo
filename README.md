# BitcoinNodeInfo

This is a simple Python script that monitors the status of a Bitcoin node and provides information about its blockchain synchronization. The script can be integrated with a Telegram bot to allow users to quickly check the status of their node using a mobile device.

## Features
Check the status of a Bitcoin node (online/offline).
Display the number of headers and blocks in the Bitcoin blockchain.
Display the synchronization status of the Bitcoin blockchain.
Display the disk usage of the node.
Display the system uptime of the node.

## Prerequisites
Python 3.6 or later.
A running Bitcoin node.
The bitcoin-cli tool installed and available in the system's PATH.
The pytz and telepot Python packages installed.
Configuration
To use the script, you need to create a Telegram bot and obtain an access token. You can follow these instructions to create a new bot and obtain an access token.

Once you have obtained an access token, replace the TOKEN variable in the script with your own access token:

```python
TOKEN = 'your_bot_token_here'
```
## Usage
To start the script, simply run the following command:

```bash
python bot.py
```

## Commands
The bot recognizes the following commands:

``` /start ``` Displays the status of the Bitcoin node and blockchain synchronization.
``` /sync ``` Displays the synchronization status of the Bitcoin blockchain.
``` /uptime ``` Displays the system uptime of the node.
``` /disk ``` Displays the disk usage of the node.
``` /ping ``` Pings the script and receives a response.

## License
This script is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
