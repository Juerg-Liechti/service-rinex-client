import time
import openapi_client
from openapi_client.api import rinex_api
from openapi_client.model.scheduled_request import ScheduledRequest
from openapi_client.model.error import Error
from openapi_client.model.request_data import RequestData
from pprint import pprint
# Defining the host is optional and defaults to https://api.swipos-dev.ch/acacia
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.swipos.ch/acacia"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = openapi_client.Configuration(
    username = 'rinex',
    password = ''
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rinex_api.RINEXApi(api_client)
    request_data = RequestData(
        station_code="AIGE",
        time_from="2020-12-17T13:00G",
        duration="PT23M",
        callback_url="https://webhook.site/36c10db1-6bd3-4eb9-8742-1f92fb113661"
    ) # RequestData |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Request up to 6 hours of rinex data from one AGNES station.
        api_response = api_instance.request_data(request_data)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RINEXApi->request_data: %s\n" % e)