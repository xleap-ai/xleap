# DataPointResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | **object** |  | [optional] 
**reasons** | **object** |  | [optional] 

## Example

```python
from xleap._client.models.data_point_result import DataPointResult

# TODO update the JSON string below
json = "{}"
# create an instance of DataPointResult from a JSON string
data_point_result_instance = DataPointResult.from_json(json)
# print the JSON string representation of the object
print DataPointResult.to_json()

# convert the object into a dict
data_point_result_dict = data_point_result_instance.to_dict()
# create an instance of DataPointResult from a dict
data_point_result_form_dict = data_point_result.from_dict(data_point_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


