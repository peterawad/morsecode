# =======================worksheet2.2 task2=====================================
from curses import echo
import morse
# convert the massege, sende and receiver to morse code.  
def encode_ham(sender, receiver, msg):
    morseCode = ''
    txt = receiver+'de'+sender+'='+msg+"=("
    for character in txt.upper():
        dotsdashes = []
        morse.Conv_letter_to_Morse(morse.tree, character, dotsdashes)
        code = "".join(dotsdashes)
        morseCode = morseCode + code + " "
    return morseCode

# convert  morse code to receiver, sender and massege.
txtham = ""
def decode_ham(Msg):
    decodemsg = ""
    morseCode = "import morse; global txtham; txtham=morse.tree"
    for morse in range(len(Msg)):
        if Msg[morse] == '.':
            morseCode += ".dot"
        elif Msg[morse] == '-':
            morseCode += ".dash"
        if Msg[morse] == ' ' or morse == len(Msg)-1:
            morseCode += ".value"
            if morseCode != "import morse; global txtham; txtham=morse.tree.value":
                exec(morseCode)
                decodemsg += txtham
                morseCode = 'import morse; global txtham; txtham=morse.tree'
            else:
                morseCode = 'import morse; global txtham; txtham=morse.tree'
        if Msg[morse] == '/':
            txt += " "
    return decodemsg

def main():
    x = encode_ham('s1', 'r1', 'hi')
    print(x)
    
    decodemsg = decode_ham('.-. .---- -.. . ... .---- -...- .... .. -...- -.--. ')
    #the split separate the decoding massege to receiver, sender and massege
    reciver = decodemsg.split('DE')
    sender = reciver[1].split("=")
    msg = sender[1].split('=(')
    print("Message from :  {}\nMessage To: {}\nMessage content: {}".format(
        reciver[0], sender[0], msg[0]))
    asyncio.run(start())


#===========worksheet2.2 task3=========================
from datetime import datetime
import socket
import asyncio
import time
import websockets
import json
import base64

uri = "ws://localhost:10102"

async def start():
    eh=encode_ham('s','echo','hello world!')
    async with websockets.connect(uri) as s:
        msg = json.loads(await s.recv())
        print("Message", msg)
        await send_echo(s,msg)
        response = await recv_message(s)
        print("The Server Sent Back:")
        print(response)
        await send_time(s)

        
async def send_echo(websocket, message):
    if message['type'] == 'join_evt':
        client_id = message['client_id']
    outward_message = {
        'client_id': client_id,
        'payload': message
        }
    await websocket.send(json.dumps(outward_message))

async def send_time(websocket):
    time=datetime.now().strftime("%H: %M: %S")
    await websocket.send(time)

async def recv_message(websocket):
    message = await websocket.send('echo')
    print("Base64:", message)
    msg_bytes = base64.b64decode(message)
    payload = msg_bytes[8:].decode("utf-8")
    print("Payload:", payload)
    return message['payload']
    
if __name__ == '__main__':
    main()