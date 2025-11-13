def caesar_cipher(text: str, offset: int, mode: str):
    text=text.lower()
    abc="abcdefghijklmnopqrstuvwxyz"
    if mode=="decrypt": offset=-offset
    out=""
    for ch in text:
        if ch==" ": out+=" "; continue
        i=abc.index(ch)
        out+=abc[(i+offset)%26]
    return out
