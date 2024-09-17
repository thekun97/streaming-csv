from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

from stream_file import process_csv_file

app = FastAPI()


class File(BaseModel):
    path: str | None = None
    topic: str | None = None
    batch_size: int = 1


@app.get("/")
def health_check():
    return {"Hello World": "Health Check OK !"}


@app.post("/process-file/")
def process_file(file: File):
    file_path = file.path
    topic = file.topic
    batch_size = file.batch_size
    process_csv_file(file_path, topic, batch_size)
    return {"Process": "Done !"}