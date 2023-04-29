'''
This program can hack messages encrypted 
with the Caesar cipher from the previous project, even 
if you don’t know the key. There are only 26 
possible keys for the Caesar cipher, so a computer can easily try all possible decryptions and display the results to the user. In cryptography, we call 
this technique a brute-force attack.
'''

encyrpt_mass = "QIIX QI FC XLI VSWI FYWLIW XSRMKLX."
decyrpt_mass = "MEET ME BY THE ROSE BUSHES TONIGHT."
decrypt_est = []
alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]


def decrypt(message, key):
    words = encyrpt_mass.split(" ")
    decrypt_est = []
    for i in range(len(words)):
        for zet in range(len(words[i])):
            temp = words[i].upper()# to avoid uppercase lowercase differences
            if temp[zet] == ".":#speciacase for'.'
                decrypt_est.append(".")
            else:
                for j in range(len(alphabet)): # I define a alphabet and then I am checking which is my letter
                    if temp[zet] == alphabet[j]:#after find a letter I also find index for go forward key times 
                        if (j - key )<0: # if index exceed the 26 return to the beginning of the alphabet
                            decrypt_est.append(alphabet[j - key + 26])
                        else:
                            decrypt_est.append(alphabet[j - key])
        if i == len(words)-1:
            decrypt_est.append("")    
        else:
            decrypt_est.append(" ")  # when we add encrypt version, we are adding ' ' after all words   except last words  
        
        decrypt_string = ''.join(decrypt_est)
    return decrypt_string

for key in range(26):
    decrypted_string = decrypt(encyrpt_mass, key)
    if decrypted_string == decyrpt_mass:
        print("Correct decrypted message:", decrypted_string)
        break