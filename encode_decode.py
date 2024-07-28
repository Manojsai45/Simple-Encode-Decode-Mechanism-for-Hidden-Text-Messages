def encode_text(cover_text, secret_text):
    encoded_text = ""
    for i in range(len(cover_text)):
        if i < len(secret_text):
            encoded_text += secret_text[i]
        encoded_text += cover_text[i]
    if len(secret_text) > len(cover_text):
        encoded_text += secret_text[len(cover_text):]
    return encoded_text

def decode_text(encoded_text):
    secret_text = ""
    for i in range(0, len(encoded_text), 2):
        secret_text += encoded_text[i]
    return secret_text

cover_text = "hero to a dfrctd njihjdf"
secret_text = "This is a secret message"
encoded_text = encode_text(cover_text, secret_text)
print("Encoded text: ", encoded_text)
decoded_text = decode_text(encoded_text)
print("Decoded text: ", decoded_text)
