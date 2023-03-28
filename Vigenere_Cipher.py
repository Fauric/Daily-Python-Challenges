class VigenereCipher(object):
    # to use: type cipher = VigenereCipher(key, alphabet)
    # cipher.encode(text)
    # cipher.decode(text)
    
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet
    
    def encode(self, text):
        key2 = self.key   #makes key as long or longer than text
        if len(self.key) < len(text):
            for i in range(len(text)-len(self.key)):
                key2 += self.key
        
        encript = ''    #encripted message
        for count,value in enumerate(text):  #for loop encripts the message
            if value not in self.alphabet:   #checks if value is in the alphabet
                encript += value
                continue
            position = self.alphabet.index(value)
            alph = self.alphabet[position:] + self.alphabet[:position]
            encript += alph[self.alphabet.index(key2[count])]
        return encript
    
    def decode(self, text):
        key2 = self.key    #makes key as long or longer than text
        if len(self.key) < len(text):
            for i in range(len(text)-len(self.key)):
                key2 += self.key
                
        encript = ''    #decoded message
        for count,value in enumerate(text):    #for loop decodes the message
            if value not in self.alphabet:     #checks if value is in the alphabet
                encript += value
                continue
            digit = self.alphabet.index(value) - self.alphabet.index(key2[count])
            encript += self.alphabet[digit]
        return encript
