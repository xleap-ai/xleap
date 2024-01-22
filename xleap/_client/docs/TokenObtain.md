# TokenObtain


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | 
**password** | **str** |  | 

## Example

```python
from xleap._client.models.token_obtain import TokenObtain

# TODO update the JSON string below
json = "{}"
# create an instance of TokenObtain from a JSON string
token_obtain_instance = TokenObtain.from_json(json)
# print the JSON string representation of the object
print TokenObtain.to_json()

# convert the object into a dict
token_obtain_dict = token_obtain_instance.to_dict()
# create an instance of TokenObtain from a dict
token_obtain_form_dict = token_obtain.from_dict(token_obtain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


