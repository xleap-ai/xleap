# ListDataPoints200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[DataPoint]**](DataPoint.md) |  | [optional] 

## Example

```python
from xleap._client.models.list_data_points200_response import ListDataPoints200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListDataPoints200Response from a JSON string
list_data_points200_response_instance = ListDataPoints200Response.from_json(json)
# print the JSON string representation of the object
print ListDataPoints200Response.to_json()

# convert the object into a dict
list_data_points200_response_dict = list_data_points200_response_instance.to_dict()
# create an instance of ListDataPoints200Response from a dict
list_data_points200_response_form_dict = list_data_points200_response.from_dict(list_data_points200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


