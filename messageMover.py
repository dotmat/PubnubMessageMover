#!/usr/bin/python3

# PubNub Message Mover, written by Mathew Jenkinson - MIT License. 
# This script is designed to help PubNub customers move or export data from longterm storage on PubNub. 

# Manage Script Inputs
import sys, getopt

# This script supports both CLI inputs and command line arguments. 
# Check to see if command line arguments have been supplied. 

if len(sys.argv) > 2:
 
else: 
  print('Welcome to PubNub Message Mover, lets get started...')
  print('We need to gather the input paramters.')
  inputSubkey = string(input("What Subkey are we getting data from? "))
  inputChannelName = string(input("What is the channel name to get data from? "))
  inputSecretKey = string(input("What is the secret key for this Subkey? "))
  inputDateOfRecords = string(input("What time period is needed? Please provide the answer between 1 day, 30 days or ALL eg 10 "))
  outputEndpoint = string(input("Where are we putting the data? If back into PubNub type pubnub, if we are saving to a file please type the file name."))
  
  # If we are writing back to PubNub, its basically a publish for each log line, as there is no bulk publish event.
  if outputEndpoint == "pubnub": 
   outputSubkey = string(input("What Subkey are we writing to? "))
   outputChannelName = string(input("What channel name are we writing to? "))
   outputSecretkey = string(input("What is the secret key for the SubKey? "))
   
  else:
   # If we are writing to an output file then use the endpoint name as the file name, with a .json extension.
   outputFileName = outputEndpoint
   
   
   
