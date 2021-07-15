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
