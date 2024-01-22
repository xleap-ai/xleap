# ListRuns200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Run]**](Run.md) |  | [optional] 

## Example

```python
from xleap._client.models.list_runs200_response import ListRuns200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListRuns200Response from a JSON string
list_runs200_response_instance = ListRuns200Response.from_json(json)
# print the JSON string representation of the object
print ListRuns200Response.to_json()

# convert the object into a dict
list_runs200_response_dict = list_runs200_response_instance.to_dict()
# create an instance of ListRuns200Response from a dict
list_runs200_response_form_dict = list_runs200_response.from_dict(list_runs200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


