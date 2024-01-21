from typing import List
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel

import tiktoken

app = FastAPI()

tokenizer = tiktoken.get_encoding("cl100k_base")

class EncodeRequest(BaseModel):
    text: str

class EncodeResponse(BaseModel):
    encoded: List[int]

class DecodeRequest(BaseModel):
    encoded: List[int]

@app.post("/encode")
async def encode(request: EncodeRequest):
    try:
        encoded_text = tokenizer.encode(request.text)
        return JSONResponse(content=encoded_text)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/decode")
async def decode(request: DecodeRequest):
    try:
        decoded_text = tokenizer.decode(request.encoded)
        return JSONResponse(content=decoded_text)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))