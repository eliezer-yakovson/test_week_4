def fence_encrypt(text: str):
    text=text.replace(" ","").lower()
    return text[0::2] + text[1::2]



def fence_decrypt(text: str):
    text=text.lower()
    half=(len(text)+1)//2
    even=text[:half]
    odd=text[half:]
    res=[]
    for i in range(len(text)):
        if i%2==0: res.append(even[i//2])
        else: res.append(odd[(i-1)//2])
    return "".join(res)
