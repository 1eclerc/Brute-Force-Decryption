import string
import pandas as pd

def rot13(text):
    result = []
    for char in text:
        if 'a' <= char <= 'z':
            result.append(chr((ord(char) - ord('a') + 13) % 26 + ord('a')))
        elif 'A' <= char <= 'Z':
            result.append(chr((ord(char) - ord('A') + 13) % 26 + ord('A')))
        else:
            result.append(char)
    return ''.join(result)

def caesar_decrypt(text, key):
    decrypted = []
    for char in text:
        if char.isalpha():
            base = 'A' if char.isupper() else 'a'
            decrypted.append(chr((ord(char) - ord(base) - key) % 26 + ord(base)))
        else:
            decrypted.append(char)
    return ''.join(decrypted)

def reverse(text):
    return text[::-1]

def transposition_decrypt(ciphertext, key_len):
    num_cols = key_len
    num_rows = -(-len(ciphertext) // num_cols)  # Ceiling division
    num_shaded_boxes = (num_cols * num_rows) - len(ciphertext)

    plaintext = [''] * num_rows
    col = 0
    row = 0

    for symbol in ciphertext:
        plaintext[row] += symbol
        row += 1
        if (row == num_rows) or (row == num_rows - 1 and col >= num_cols - num_shaded_boxes):
            row = 0
            col += 1

    return ''.join(plaintext)

# Replace this with your actual encrypted message
encrypted_message = "YmxpbGFuZ2VtIGVyaXRlIGl1c3JvbSBuZWUgZG5hIGx1Y2Fk"

candidates = []

for trans_key in range(2, 11):  # Transposition keys 2–10
    try:
        trans_decrypted = transposition_decrypt(encrypted_message, trans_key)
    except Exception:
        continue

    reversed_text = reverse(trans_decrypted)

    for caesar_key in range(1, 26):  # Caesar keys 1–25
        caesar_decrypted = caesar_decrypt(reversed_text, caesar_key)
        final_text = rot13(caesar_decrypted)
        candidates.append((trans_key, caesar_key, final_text))

# Output all candidates
for trans_key, caesar_key, result in candidates:
    print(f"[Transposition Key: {trans_key}] [Caesar Key: {caesar_key}] → {result}")
