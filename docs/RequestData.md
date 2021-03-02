# RequestData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**station_code** | **str** | A valid 4-character base station code in capital letters. | 
**time_from** | **str** | An ISO 8601 timestamp that defines start of desired period. | 
**duration** | **str** | An ISO 8601 period that defines length of desired period. Minimum duration must be 5 minutes (PT5M) | 
**time_to** | **str** | An ISO 8601 timestamp that defines end of desired period. | [optional] 
**callback_url** | **str** | This url will be triggered with a POST request with CallbackAnswer in body. | [optional] 
**include_log** | **str** | If there is a value like ‘true’, ‘1’, ‘yes’, ‘y’, case insensitive, resulting archive will contain logs from merge process. | [optional] 
**observation_only** | **str** | If there is a value like ‘true’, ‘1’, ‘yes’, ‘y’, case insensitive, resulting archive will not contain NAV files. In case &#39;include_log&#39; is false, the resulting file will be a single observation rinex file. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


