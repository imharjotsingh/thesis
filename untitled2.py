#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 03:07:18 2019

@author: harjot
"""

from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC31c3437cf6aa0dd70c3c07504be1e470"
# Your Auth Token from twilio.com/console
auth_token  = "6f7054f360026882a72176f2f8c85ec0"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+19282565551", 
    from_="+27818756921",
    body="Hello from Python!")

print(message.sid)