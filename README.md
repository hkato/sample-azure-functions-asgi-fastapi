# Azure Functions + ASGI + FastAPI sample

ref. [Azure Functions + WSGI + Flask sample](https://github.com/hkato/sample-azure-functions-wsgi-flask) WSGI + Flask version. 

## Directory Structure

```
.
├── fastapi_app         # FastAPI/ASGI WebApp
│   ├── __init__.py
│   └── app.py
├── functions_asgi      # Functions entry -> ASGI
│   ├── __init__.py
│   └── function.json
├── host.json
└── requirements.txt
```

## Key point

```python
import azure.functions as func

from fastapi_app.app import app   # app = FastAPI()


def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    # ASGI Application
    return func.AsgiMiddleware(app).handle(req, context)
    #           ^^^^^^^^^^^^^^ ^^^
```
