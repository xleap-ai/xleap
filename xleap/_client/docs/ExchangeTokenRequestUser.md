# ExchangeTokenRequestUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. | 
**id** | **int** |  | [optional] [readonly] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**date_joined** | **datetime** |  | [optional] [readonly] 

## Example

```python
from xleap._client.models.exchange_token_request_user import ExchangeTokenRequestUser

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangeTokenRequestUser from a JSON string
exchange_token_request_user_instance = ExchangeTokenRequestUser.from_json(json)
# print the JSON string representation of the object
print ExchangeTokenRequestUser.to_json()

# convert the object into a dict
exchange_token_request_user_dict = exchange_token_request_user_instance.to_dict()
# create an instance of ExchangeTokenRequestUser from a dict
exchange_token_request_user_form_dict = exchange_token_request_user.from_dict(exchange_token_request_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


