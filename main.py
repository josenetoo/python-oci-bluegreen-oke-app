from typing import Optional

from fastapi import FastAPI

import os

app = FastAPI()


@app.get("/bluegreen")
def read_root():
    version="1.0"
    namespace = os.getenv('POD_NAMESPACE', default = 'ns-red')
    return {"Message": "Oracle DevOps Day - OCI Devops","Version":version,"Namespace":namespace}
