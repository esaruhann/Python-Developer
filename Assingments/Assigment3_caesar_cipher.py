'''
The Caesar cipher is an ancient encryption algorithm used by Julius Caesar. It 
encrypts letters by shifting them over by a 
certain number of places in the alphabet. We 
call the length of shift the key. For example, if the 
key is 3, then A becomes D, B becomes E, C becomes 
F, and so on. To decrypt the message, you must shift 
the encrypted letters in the opposite direction. This 
program lets the user encrypt and decrypt messages 
according to this algorithm.

When you run the code, the output will look like this:

Do you want to (e)ncrypt or (d)ecrypt?
> e
Please enter the key (0 to 25) to use.
> 4
Enter the message to encrypt.
> Meet me by the rose bushes tonight.
QIIX QI FC XLI VSWI FYWLIW XSRMKLX.


Do you want to (e)ncrypt or (d)ecrypt?
> d
Please enter the key (0 to 26) to use.
> 4
Enter the message to decrypt.
> QIIX QI FC XLI VSWI FYWLIW XSRMKLX.
MEET ME BY THE ROSE BUSHES TONIGHT.
'''
alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
encrypt = []
decrypt = []
ans = input("Do you want to (e)ncrypt or (d)ecrypt?")
if ans == "e": # for encrypt
    key = int(input("Please enter the key (0 to 25) to use."))
    if key > 25:
        raise Exception("Key should be lower than 25")
    message = input("Enter the message to decrypt.")

    words = message.split(" ") # I divide all the sentences according to' 'and obtain words
    for i in range(len(words)):
        for zet in range(len(words[i])):
            temp = words[i].upper() # to avoid uppercase lowercase differences
            if temp[zet] == ".": #speciacase for'.'
                encrypt.append(".")
            else:            
                for j in range(len(alphabet)): # I define a alphabet and then I am checking which is my letter
                    if temp[zet] == alphabet[j]: #after find a letter I also find index for go forward key times 
                        if (j + 4 )> 26: # if index exceed the 26 return to the beginning of the alphabet
                            encrypt.append(alphabet[j + 4 - 26])
                        else:
                            encrypt.append(alphabet[j + 4])
        encrypt.append(" ") # when we add encrypt version, we are adding ' ' after all words   
        
    encrypt_string = ' '.join(encrypt) # convert it to string
    print(encrypt_string)
        
elif ans == "d": # for decrypt
    key = int(input("Please enter the key (0 to 25) to use."))
    if key > 25:
        raise Exception("Key should be lower than 25")
    message = input("Enter the message to decrypt.")

    words = message.split(" ")
    for i in range(len(words)):
        for zet in range(len(words[i])):
            temp = words[i].upper()
            if temp[zet] == ".":
                decrypt.append(".")
            else:
                for j in range(len(alphabet)):
                    if temp[zet] == alphabet[j]:
                        if (j - 4 )<0:
                            decrypt.append(alphabet[j - 4 + 26])
                        else:
                            decrypt.append(alphabet[j - 4])
        decrypt.append(" ")    
        
    decrypt_string = ' '.join(decrypt)
    print(decrypt_string)
else:
    print("Invalid input")