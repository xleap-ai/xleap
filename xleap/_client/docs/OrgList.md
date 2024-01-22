# OrgList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**name** | **str** |  | 

## Example

```python
from xleap._client.models.org_list import OrgList

# TODO update the JSON string below
json = "{}"
# create an instance of OrgList from a JSON string
org_list_instance = OrgList.from_json(json)
# print the JSON string representation of the object
print OrgList.to_json()

# convert the object into a dict
org_list_dict = org_list_instance.to_dict()
# create an instance of OrgList from a dict
org_list_form_dict = org_list.from_dict(org_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


