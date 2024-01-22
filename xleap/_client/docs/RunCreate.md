# RunCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**session_name** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**reference_example_id** | **str** |  | [optional] 
**start_time** | **str** |  | 
**end_time** | **str** |  | [optional] 
**extra** | **object** |  | [optional] 
**events** | **object** |  | [optional] 
**outputs** | **object** |  | [optional] 
**serialized** | **object** |  | [optional] 
**inputs** | **object** |  | [optional] 
**error** | **str** |  | [optional] 
**run_type** | **str** |  | [optional] 
**execution_order** | **int** |  | [optional] 
**child_execution_order** | **str** |  | [optional] 
**parent_run_id** | **str** |  | [optional] 

## Example

```python
from xleap._client.models.run_create import RunCreate

# TODO update the JSON string below
json = "{}"
# create an instance of RunCreate from a JSON string
run_create_instance = RunCreate.from_json(json)
# print the JSON string representation of the object
print RunCreate.to_json()

# convert the object into a dict
run_create_dict = run_create_instance.to_dict()
# create an instance of RunCreate from a dict
run_create_form_dict = run_create.from_dict(run_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


