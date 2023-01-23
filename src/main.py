import rollbar
from mangum import Mangum
from terrahaxs_worker import app
from src.settings import settings

rollbar.init(
    settings.rollbar_key,
    'prod',
    handler='blocking',
    include_request_body=True)

@rollbar.lambda_function
def handler(event, context):  # pragma: no cover
    try:
        asgi_handler = Mangum(app)
        # Call the instance with the event arguments
        response = asgi_handler(event, context)

        return response
    except BaseException:
        rollbar.report_exc_info()
        rollbar.wait()
        raise