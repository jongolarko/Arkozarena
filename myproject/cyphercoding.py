import pyperclip
message='this is my secret message'
key = 13
mode='encrypt'
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
decryptedmsg=''
for symbol in message:
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)

        if mode == 'encrypt':
           decryptedmsgIndex = symbolIndex + key
        elif mode =='decrypt':
           decryptedmsgIndex = symbolIndex - key
        if decryptedmsg>=len(SYMBOLS):
               decryptedmsgIndex = decryptedmsg - len(SYMBOL)
        elif decryptedmsg<0:
               decryptedmsgIndex = decryptedmsgIndex + len(SYMBOL)
               decryptedmsg = decryptedmsg = SYMBOLS[decryptedmsgIndex]
    else:
        decryptedmsg = decryptedmsg + symbol

print(decryptedmsg)
pyperclip.copy(decryptedmsg)
               

           
    
