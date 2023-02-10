import os
import sys

from typing import List
from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
INPUT_DIR = os.path.join(BASE_DIR, "serving/input")
OUTPUT_DIR = os.path.join(BASE_DIR, "serving/output")

count = 1

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

@app.post("/upload")
async def upload(file: UploadFile = Form()):
    '''
    local 서버에서 파일을 받음
    sc 서버 input 경로에 파일 저장
    '''
    global count
    video = await file.read()  # 파일 읽기
    
    file_name = "video_" + str(count) + ".mp4" # 파일 이름 저장
    file_path = os.path.join(INPUT_DIR, file_name) # input 경로
    
    with open(file_path, "wb") as f: # Upload된 input 데이터 저장
        f.write(video)
    
    count += 1
    
    return "OK"