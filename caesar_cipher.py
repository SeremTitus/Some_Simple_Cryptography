Alfabets = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

shift_key:int = int(input('Enter your shift value: '))

def encrypt(data:str):
    encrypted_data =''
    for char in data:
        shift_num = Alfabets.index(char.upper()) + shift_key
        while shift_num > 36 : shift_num = shift_num - 36
        encrypted_data += Alfabets[shift_num]
    return encrypted_data

def decrypt(data:str):
    decrypted_data =''
    for char in data:
        shift_num = Alfabets.index(char.upper()) - shift_key
        while shift_num < 0 : shift_num = shift_num + 36
        decrypted_data += Alfabets[shift_num] 
    return decrypted_data

yourEncrypt = input('Your Data to encrypt: ')

print('encryted form:',encrypt(yourEncrypt))
print('decrypted form:',decrypt(encrypt(yourEncrypt)))