#!/usr/bin/python3

# PubNub Message Mover, written by Mathew Jenkinson - MIT License. 
# This script is designed to help PubNub customers move or export data from longterm storage on PubNub. 

# Manage Script Inputs
import sys, getopt
import time
from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNStatusCategory, PNOperationType
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub

pnconfig = PNConfiguration()

historyObject = {}

# This script supports both CLI inputs and command line arguments. 
# Check to see if command line arguments have been supplied.

def my_fetch_messages_callback(envelope, status):
    if not status.is_error():
        # Messages successfully retrieved from the specified channel.

        print("Fetch Messages Result:\n")
        for message in envelope.channels["my_channel"]:
            print("Message: %s \n" % message)
    else:
        # Handle fetch messages error.
        pass

def getHistoryForAChannel(subkey, channelName, secretKey, dateRange):
  print('Getting PubNub History Now.')
  pnconfig.subscribe_key = subkey
  pnconfig.publish_key = 'IAmTheMatBot'
  pnconfig.secret_key = secretKey
  pnconfig.uuid = 'IAmTheMessageBot'
  pubnub = PubNub(pnconfig)

  # Get the time now in seconds
  timeNow = int(time.time())
  # print('Time Now '+str(timeNow))
  if dateRange == 'ALL' or 'All' or 'all':
    print('Getting All Messages for channel '+channelName)

  else:
    print('Getting Messages from the last '+dateRange+' days.') 
    # Calculate the timestamp of the 'start' time range - because the script works back through time rather than linearly.. its a bit 
    # Wibbly Wobbly Timey Wimey
    startTimeStamp = (timeNow - (86400 * int(dateRange))) * 10000000
  
  pubnub.fetch_messages().channels([channelName]).maximum_per_channel(25).include_message_actions(True).include_meta(True).pn_async(my_fetch_messages_callback)

  

if len(sys.argv) > 2:
 print('Nothing yet.')
else:
  print('Welcome to PubNub Message Mover, lets get started...')
  print('We need to gather the input paramters.')
  inputSubkey = input("What Subkey are we getting data from? ")
  #inputPubkey = input("What Pubkey are we getting data from? ")
  inputSecretKey = input("What is the secret key for this Subkey? ")
  inputChannelName = input("What is the channel name to get data from? ")
  inputDateOfRecords = input("What time period is needed? Please provide the answer between 1 day, 30 days or ALL eg 10 ")
  outputEndpoint = input("Where are we putting the data? If back into PubNub type pubnub, if we are saving to a file please type the file name: ")
  
  # If we are writing back to PubNub, its basically a publish for each log line, as there is no bulk publish event.
  if outputEndpoint == "pubnub": 
   outputSubkey = input("What Subkey are we writing to? ")
   outputChannelName = input("What channel name are we writing to? ")
   outputSecretkey = input("What is the secret key for the SubKey? ")
   
  else:
   # If we are writing to an output file then use the endpoint name as the file name, with a .json extension.
   outputFileName = outputEndpoint

getHistoryForAChannel(inputSubkey, inputChannelName, inputSecretKey, inputDateOfRecords)


