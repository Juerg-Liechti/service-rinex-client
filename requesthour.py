import time
import openapi_client
from openapi_client.api import rinex_api
from openapi_client.model.error import Error
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
    station_code = "AIGE" # str | Station code
    time = "2020-12-12T12:00G" # str | Requesting hour starting at (e.g. yyyy-MM-ddThh:00G or yyyyMMddThh00G)

    # example passing only required values which don't have defaults set
    try:
        # Request an existing hour RINEX file for a station code.
        api_response = api_instance.request_hour(station_code, time)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RINEXApi->request_hour: %s\n" % e)