# DataPointCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**question** | **str** |  | 
**answer** | **str** |  | 
**ground_truths** | **List[object]** |  | [optional] 
**contexts** | **List[str]** |  | [optional] 
**project** | **str** |  | [optional] 
**tags** | **object** |  | [optional] 

## Example

```python
from xleap._client.models.data_point_create import DataPointCreate

# TODO update the JSON string below
json = "{}"
# create an instance of DataPointCreate from a JSON string
data_point_create_instance = DataPointCreate.from_json(json)
# print the JSON string representation of the object
print DataPointCreate.to_json()

# convert the object into a dict
data_point_create_dict = data_point_create_instance.to_dict()
# create an instance of DataPointCreate from a dict
data_point_create_form_dict = data_point_create.from_dict(data_point_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


