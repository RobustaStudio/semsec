import os
import subprocess
import requests
from fastapi import APIRouter, Depends, FastAPI
from flask import Flask, send_file

api = FastAPI()
router = APIRouter()
app = Flask(__name__)


@api.get("/run")
def run(cmd: str):
    # ruleid: robusta-py-cmdi-taint
    os.system("ls " + cmd)


@router.get("/fetch")
async def fetch(url: str):
    # ruleid: robusta-py-ssrf-taint
    return requests.get(url).text


@router.post("/read")
async def read(path: str):
    # ruleid: robusta-py-pathtraver-taint
    return open(path).read()


@app.route("/file/<path:p>")
def download(p):
    # ruleid: robusta-py-pathtraver-taint
    return send_file(p)


@router.get("/user/{uid}")
async def user(uid: int, db=Depends(get_db)):
    # ok: robusta-py-cmdi-taint
    db.execute("select * from users where id = %s", (uid,))
    # ok: robusta-py-cmdi-taint
    subprocess.run(["ls", "-l"])


@celery.task
def job(cmd):
    # ok: robusta-py-cmdi-taint
    os.system(cmd)
