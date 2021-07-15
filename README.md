# PubnubMessageMover
PubNub Message Mover 

Message Mover is a Python(3) based script that lets you move messages from one PubNub SubKey/Channel to another SubKey/Channel.
This is used in situations where you need to clone or export a channels contents. 

## How to use

### Source
In order to grab messages from a channel you need: 
1. PubNub Subkey
2. Channel Name
3. PAM Token (Optional)

### Destination
Once you have the messages you need to do something with them. 
1. Write to a different Subkey and/or channel. 
2. Export to JSON file.

When writing to a new channel, you will need to provide both the Subkey, Pubkey and channel name. 
🛑 Important! In order to preserve the original timetokens for when you move messages to a new channel you MUST reach out to support to get them to enable PTTO (publish timetoken override) More info can be found at: <https://support.pubnub.com/hc/en-us/articles/360051973351-How-to-import-your-legacy-data-into-PubNub-Storage> 🛑

When writing to an export log the messages will be written into a JSON object and saved as a filename.json in the same directory as the script. 

## Usage
```python
python3 messageMover.py
```
- Message Mover will ask you for the origin SubKey, channel & time window (1 day, 30 days or all the messages)
- Message Mover will then ask you for a destination. 
- - If you are moving the messsages to another channel you will need to supply PubKey, Subkey, PAM token (if needed) and channel name. 
- - If you are exporting the data you will need to supply a file name. 

## CLI Usage & Command line arguments
Message Mover also supports CLI inputs, EG:
```python
python3 messageMover.py if=SubKey/Channel/Token of=SubKey/PubKey/Channel/Token || filename.json duration=1||30||all verbose=true
```
