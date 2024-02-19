# ProjectCreateConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric_name_map** | **object** |  | 
**transformer_name** | **str** |  | 
**topics** | **List[str]** |  | 
**nlp_scores** | **List[str]** |  | 
**rouge_type** | **str** |  | 
**scores** | **List[str]** |  | 

## Example

```python
from xleap._client.models.project_create_config import ProjectCreateConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectCreateConfig from a JSON string
project_create_config_instance = ProjectCreateConfig.from_json(json)
# print the JSON string representation of the object
print ProjectCreateConfig.to_json()

# convert the object into a dict
project_create_config_dict = project_create_config_instance.to_dict()
# create an instance of ProjectCreateConfig from a dict
project_create_config_form_dict = project_create_config.from_dict(project_create_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


