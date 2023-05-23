# iot worksheet2

# introduction about morsecode:

It is an encrypt method used in warworld2, it consists of dashes and dots its used to send message in format sound beep(dot) and long beep(dash).

## iot worksheet2.1

## task1
- Connect to server by using forward port 10105 link 
    http://localhost:10105 
- to understand the converting between text to morse code and morse code to text.

## task2 
We have two functions:

•	Encode: it is used to convert the letter to dot and dashes by convert the message to upper cases and make a recursive function called (Conv_letter_to_Morse) and checks on a character then returns the dot and dashes, group it then prints the morse code.
![encodedecode_task2](/uploads/dff900ef62747a1c34461faa8c3e58c4/encodedecode_task2.jpg)

•	Decode: it is used convert the morse code to letters by checking on dots and dashes then changes them to the branch of a tree and then print the letters. Note (/) changes to space.


![z-decode](/uploads/dcae02603ea5c4afebad253551273d84/z-decode.jpg)

•	Build the tree: 
- Define the root
    tree = Node("*")  
- define the first level of the tree
    tree.dot = Node("E")
    tree.dash = Node("T")

![z-tree](/uploads/864014237d8b1e473bd5e0acc5047e0e/z-tree.jpg)

•	main.py
first import morse.py then we can decode and encode and make an assert to this function.
![main.py](/uploads/bd715ae32d9ed942aa8d61d03d102506/main.py.jpg)

## task3
•	Assert_test.py 
the assert making of encode and decode is used as a function, if the test of the function is done show message “Everything is passed”

![task3_assert_failed](/uploads/354cbb67f1820f4918b0db9fd51585c6/task3_assert_failed.jpg)

![task3_assert_passed](/uploads/3524b164f2920a33fd289346f0720ddc/task3_assert_passed.jpg)
•	morseunit.py
It is small test case, used when tests are added to check that a fixed bug is not broken in a later release unittest  is a library built into the Python standard library.  import unittest -	we make 5 check of ecode using function assertequal on test_encode_us
-	we make 5 check of deecode using function assertequal on test_decode_us 
-	check if tree is empty by using test_Empty_tree(self)
-	that a tree is not empty by using test_tree(self)
-	the insert function test_insert
-	find by test_find(self)

![task3_encode_decode_fail](/uploads/5130fd201d724f76f3dcd3f7b2b85760/task3_encode_decode_fail.jpg)

![task3_encode_decode_ok](/uploads/54e3b66a4aa26c7800646d9486d32f34/task3_encode_decode_ok.jpg)

 ## task4
we are complete symbols by using tree.dot…… or tree.dash….. on level 5th and 6th and 7th level of tree

![test_task4](/uploads/ee010732b51a54c18bcbac13e0008003/test_task4.jpg)
# worksheet 2.2 

## Task1
We use binary heap, by use letter array sorted like binary tree an check by index 
If ch =”.” We calc index
index = index*2
and if ch =’-‘ we calc index by  = 2*index+1
and if =”/” we execute space letter 

## comparing between binary tree and head tree and dictionary
-	binary tree is take time O(log n ) when the tree is well balanced ,binary  heap Not ordered and so more time for search other elements. , dictionary take a long time and must visit each node if we want to get last.
-	binary tree used medium path to found letter or morse depend of depth of tree, heap tree used short paths, and dictionary used long path to reach requirement letter.

## Worksheet 2 - Task 2
Ham conversion has many abbreviations like “ de  “ is used like “from- to-“
-	To make encode we using:
encode_ham(sender,reciver, msg)
  that concatenate (name of receiver + de  + Sender+ “= “+msg+”=(”)
and convert each letter to morse code. 
-	Decode_ham(msg)
-	First convert morse code to letters and the split the message 
    - From start to de is receiver  
    - From de to =  is sender 
    - From = to =( is message
    
    ![worksheet2.2_task2](/uploads/9a3e0efb09a588ab78741bccbb9b7027/worksheet2.2_task2.jpg)
## task 3
-	We create websocket as s and using uri= "ws://localhost:10102" to connect server
-	Wre make encoded ham using calling function encode_ham(s,'echo', msg) 
-	We use send_echo(sender, msg) to send message to server and then return decoded message 
-	And we make same things to time encode_ham(s,'time', 'hello world')
-	We use send_time(sender) to send message to server and then return decoded message


