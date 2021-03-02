import time
import openapi_client
from pprint import pprint
from openapi_client.api import rinex_api
from openapi_client.model.base_station import BaseStation
from openapi_client.model.error import Error
from openapi_client.model.nearest_station import NearestStation
from openapi_client.model.request_data import RequestData
from openapi_client.model.scheduled_request import ScheduledRequest
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
    
    try:
        # Returns a list of all AGNES stations.
        api_response = api_instance.list()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RINEXApi->list: %s\n" % e)