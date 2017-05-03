#!/usr/bin/python3
from telethon import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.utils import get_input_peer

api_id = your_id
api_hash = 'your_hash'
phone_number = 'your_number'

print ("setting up")

client = TelegramClient('username', api_id, api_hash)
client.connect()

print ("connected")

print ("authorizing")

if not client.is_user_authorized():
    client.send_code_request(phone_number)
    client.sign_in(phone_number, input('Enter the code: '))

print ("authorized")

print ("getting dialogs")

dialogs, entities = client.get_dialogs(10)
entity = entities[0]

print ("invoking GetHistoryRequest")


result = client.invoke(
    GetHistoryRequest(
        get_input_peer(entity),
        limit=20,
        offset_date=None,
        offset_id=0,
        max_id=0,
        min_id=0,
        add_offset=0))

messages = result.messages

print (str(messages[0]))
