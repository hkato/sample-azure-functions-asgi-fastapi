import logging

import azure.functions as func

from fastapi_app.app import app


def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # ASGI Application
    return func.AsgiMiddleware(app).handle(req, context)
