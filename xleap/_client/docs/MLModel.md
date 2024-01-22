# MLModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**name** | **str** |  | 
**url** | **str** |  | 
**requests_count** | **int** |  | 
**cost** | **decimal.Decimal** |  | 
**status** | **str** |  | 

## Example

```python
from xleap._client.models.ml_model import MLModel

# TODO update the JSON string below
json = "{}"
# create an instance of MLModel from a JSON string
ml_model_instance = MLModel.from_json(json)
# print the JSON string representation of the object
print MLModel.to_json()

# convert the object into a dict
ml_model_dict = ml_model_instance.to_dict()
# create an instance of MLModel from a dict
ml_model_form_dict = ml_model.from_dict(ml_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


