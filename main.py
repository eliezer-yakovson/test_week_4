from fastapi import FastAPI
from pathlib import Path
import uvicorn
from ciphers.caesar import caesar_cipher
from ciphers.fence import fence_encrypt, fence_decrypt
from moduls.class_moduls import CaesarRequest, FenceDecryptRequest

app = FastAPI()

filePache = Path(__file__).resolve().parent


@app.get("/test")
def test():
    return {"msg": "hi from test"}


@app.get("/test/{name}")
def save_name(name: str):
    with open(f'{filePache}/data/names.txt', "a", encoding="utf-8") as f:
        f.write(name + "\n")
    return {"msg": "saved user"}


@app.post("/caesar")
def caesar_endpoint(body: CaesarRequest):
    result=caesar_cipher(body.text, body.offset, body.mode)
    if body.mode=="encrypt":
        return {"encrypted_text": result}
    return {"decrypted_text": result}


@app.get("/fence/encrypt/{text}")
def fence_encrypt_endpoint(text: str):
    result=fence_encrypt(text)
    return {"encrypted_text": result}


@app.post("/fence/decrypt")
async def fence_decrypt_endpoint(body: FenceDecryptRequest):
    result=fence_decrypt(body.text)
    return {"decrypted": result}

if __name__ == "__main__":
        uvicorn.run(app, host="localhost", port=8000)
