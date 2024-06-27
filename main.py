from typing import Optional

from fastapi import FastAPI

import os

app = FastAPI()


@app.get("/bluegreen")
def read_root():
    version="3.0"
    namespace = os.getenv('POD_NAMESPACE', default = 'ns-red')
    return {"Message": "DevOps Heroes - OCI Devops","Version":version,"Namespace":namespace}
