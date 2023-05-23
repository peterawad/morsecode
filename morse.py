# ====================task2(worksheet2.1)================================
#create the tree
class Node:
    def __init__(self, value):
        self.value = value
        self.dash = None
        self.dot = None

#collects the dot and dash and convert them.
def Conv_letter_to_Morse(node, character, code):
    if node == None:
        return False
    elif node.value == character:
        return True
    else:
        if Conv_letter_to_Morse(node.dash, character, code) == True:
            code.insert(0, "-")
            return True
        elif Conv_letter_to_Morse(node.dot, character, code) == True:
            code.insert(0, ".")
            return True

#encode takes letters convert to morse code
def encode(msg):
    morseCode = ''
    for character in msg.upper():
        dotsdashes = []
        Conv_letter_to_Morse(tree, character, dotsdashes)
        code = "".join(dotsdashes)
        morseCode = morseCode + code + " "
        # print(morseCode)
    return morseCode

#decode takes morse convert to massege
def decode(Msg):
    morseCode = 'print(tree'
    for morse in range(len(Msg)):
        if Msg[morse] == '.':
            morseCode += '.dot'
        elif Msg[morse] == '-':
            morseCode += '.dash'

        if Msg[morse] == ' ' or morse == len(Msg)-1:
            morseCode += '.value,end ="")'
            if morseCode != 'print(tree.value,end ="")':
                exec(morseCode)
                morseCode = 'print(tree'
            else:
                morseCode = 'print(tree'
        if Msg[morse] == '/':
            print(" ", end="")

tree = Node("*")  # The root

# 1st Level
tree.dot = Node("E")
tree.dash = Node("T")

# 2nd Level
tree.dot.dot = Node("I")
tree.dot.dash = Node("A")
tree.dash.dot = Node("N")
tree.dash.dash = Node("M")

# 3rd Level
tree.dot.dot.dot = Node("S")
tree.dot.dot.dash = Node("U")
tree.dot.dash.dot = Node("R")
tree.dot.dash.dash = Node("W")

tree.dash.dot.dot = Node("D")
tree.dash.dot.dash = Node("K")
tree.dash.dash.dot = Node("G")
tree.dash.dash.dash = Node("O")

# 4th Level
tree.dot.dot.dot.dot = Node("H")
tree.dot.dot.dot.dash = Node("V")
tree.dot.dot.dash.dot = Node("F")
tree.dot.dot.dash.dash = Node("")
tree.dot.dash.dot.dot = Node("L")
tree.dash.dash.dash.dash = Node("")
tree.dot.dash.dash.dash = Node("")
tree.dash.dash.dot.dot = Node("")
tree.dash.dot.dot.dot = Node("")
tree.dash.dash.dash.dot = Node("")
tree.dash.dot.dash.dash = Node("")
tree.dot.dash.dot.dash = Node("")
tree.dash.dot.dash.dot = Node("")


# 5th Level
tree.dot.dash.dash.dash.dash = Node("1")
tree.dot.dot.dash.dash.dash = Node("2")
tree.dot.dot.dot.dash.dash = Node("3")
tree.dot.dot.dot.dot.dash = Node("4")
tree.dot.dot.dot.dot.dot = Node("5")
tree.dash.dot.dot.dot.dot = Node("6")
tree.dash.dash.dot.dot.dot = Node("7")
tree.dash.dash.dash.dot.dot = Node("8")
tree.dash.dash.dash.dash.dot = Node("9")
tree.dash.dash.dash.dash.dash = Node("0")
tree.dash.dot.dot.dot.dash = Node("=")

# ===========================task4(worksheet2.1)===========================

tree.dash.dot.dash.dash.dot = Node("(")
tree.dot.dash.dot.dash.dot = Node("+")
tree.dot.dot.dash.dot.dash = Node("¿")
tree.dot.dot.dash.dash.dot = Node("?")
tree.dot.dash.dot.dot.dot = Node("&")
tree.dash.dash.dot.dot.dash = Node("")
tree.dot.dash.dot.dot.dash = Node("")
tree.dash.dot.dash.dot.dash = Node("")
tree.dot.dot.dot.dash.dot = Node("")
tree.dash.dot.dash.dot.dash = Node("")

# 6th Level
tree.dot.dash.dot.dash.dot.dash = Node(".")
tree.dash.dash.dot.dot.dash.dash = Node(",")
tree.dash.dot.dash.dash.dot.dash = Node(")")
tree.dash.dot.dot.dot.dot.dash = Node("-")
tree.dash.dash.dot.dot.dot.dash = Node("|")
tree.dot.dot.dash.dash.dot.dash = Node("_")
tree.dot.dash.dash.dash.dash.dot = Node("'")
tree.dash.dash.dash.dot.dot.dot = Node(":")
tree.dot.dash.dot.dot.dash.dot = Node('"')
tree.dash.dot.dash.dot.dash.dash = Node('!')
tree.dash.dot.dash.dot.dash.dot = Node(";")
tree.dot.dot.dot.dash.dot.dot = Node("")

tree.dot.dot.dot.dash.dot.dot.dash = Node("$")

def main():
    msg = "A"
    txt=''
    txt += tree.dot.dash.dot.value
    print(txt)
    encode(msg)
    decode('.... . .-.. .-.. --- / .-- --- .-. .-.. -..')
    print("\n")
    print(encode(",.()-;"))
    decode('--..-- .-.-.- -.--. -.--.- -....-')
    print("\n")

if __name__ == '__main__':
    main()