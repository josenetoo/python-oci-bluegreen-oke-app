from typing import Optional

from fastapi import FastAPI

import os

app = FastAPI()


@app.get("/")
def read_root():
    version="0.1"
    namespace = os.getenv('POD_NAMESPACE', default = 'ns-red')
    return {"Message": "OCI Devops ","Version":version,"Namespace":namespace}
