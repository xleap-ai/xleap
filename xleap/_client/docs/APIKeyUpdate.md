# APIKeyUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 

## Example

```python
from xleap._client.models.api_key_update import APIKeyUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of APIKeyUpdate from a JSON string
api_key_update_instance = APIKeyUpdate.from_json(json)
# print the JSON string representation of the object
print APIKeyUpdate.to_json()

# convert the object into a dict
api_key_update_dict = api_key_update_instance.to_dict()
# create an instance of APIKeyUpdate from a dict
api_key_update_form_dict = api_key_update.from_dict(api_key_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


