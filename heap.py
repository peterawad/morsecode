#===============worksheet2.2 task1==================

#array of letters.
letters = ['', 'E', 'T', 'I', 'A', 'N', 'M', 'S', 'U', 'R', 'W', 'D', 'K', 'G', 'O', 'H', 'V', 'F', '*', 'L', '*', 'P', 'J', 'B', 'X', 'C', 'Y', 'Z', 'Q', '*', '*',
           '5', '4', '*', '3', '*', '*', '*', '2', '*', '*', '+', '*', '*', '*', '*', '1', '6', '=', '/', '*', '*', '*', '*', '*', '7', '*', '*', '*', '8', '*', '9', '0']

#the function takes the massege and convert it by binary heap 
def decode_bt(Msg):
    ltr = ''
    morseCode = ''
    msg_split = Msg.split(' ')
    for ch in msg_split:
        index = 0
        for i in ch:
            if i=='/':
                ltr=' '
            else:
                if i == '.':
                    index = index*2
                else:
                    index = 2*index+1
                index += 1
                ltr = letters[index]
            
        morseCode += ltr
    print(morseCode)


decode_bt(".... . .-.. .-.. --- / .-- --- .-. .-.. -..")
