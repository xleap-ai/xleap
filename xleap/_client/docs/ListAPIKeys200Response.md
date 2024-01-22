# ListAPIKeys200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[APIKey]**](APIKey.md) |  | [optional] 

## Example

```python
from xleap._client.models.list_api_keys200_response import ListAPIKeys200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListAPIKeys200Response from a JSON string
list_api_keys200_response_instance = ListAPIKeys200Response.from_json(json)
# print the JSON string representation of the object
print ListAPIKeys200Response.to_json()

# convert the object into a dict
list_api_keys200_response_dict = list_api_keys200_response_instance.to_dict()
# create an instance of ListAPIKeys200Response from a dict
list_api_keys200_response_form_dict = list_api_keys200_response.from_dict(list_api_keys200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


