# ExchangeTokenRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | 
**provider** | **str** |  | 
**api_key** | **str** |  | [optional] [readonly] 
**access_token** | **str** |  | [optional] [readonly] 
**refresh_token** | **str** |  | [optional] [readonly] 
**user** | [**ExchangeTokenRequestUser**](ExchangeTokenRequestUser.md) |  | [optional] 

## Example

```python
from xleap._client.models.exchange_token_request import ExchangeTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangeTokenRequest from a JSON string
exchange_token_request_instance = ExchangeTokenRequest.from_json(json)
# print the JSON string representation of the object
print ExchangeTokenRequest.to_json()

# convert the object into a dict
exchange_token_request_dict = exchange_token_request_instance.to_dict()
# create an instance of ExchangeTokenRequest from a dict
exchange_token_request_form_dict = exchange_token_request.from_dict(exchange_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


