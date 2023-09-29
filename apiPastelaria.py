from fastapi import FastAPI
from settings import HOST, PORT, RELOAD
app = FastAPI()
if __name__ == "__main__":
import uvicorn
uvicorn.run('apiPastelaria:app', host=HOST, port=int(PORT), reload=RELOAD)