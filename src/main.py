from mangum import Mangum
from terrahaxs_worker import app

def handler(event, context):  # pragma: no cover
    asgi_handler = Mangum(app)
    # Call the instance with the event arguments
    response = asgi_handler(event, context)

    return response