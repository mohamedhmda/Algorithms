def caesar_cipher(message, key):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    message_lenght = len(message)
    cypher = list(message)
    for i in range(message_lenght):
        enc_i = (alphabet.index(cypher[i]) + key) % 26
        cypher[i] = alphabet[enc_i]
    return "".join(cypher)


