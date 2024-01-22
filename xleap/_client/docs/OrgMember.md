# OrgMember


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**username** | **str** |  | 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 

## Example

```python
from xleap._client.models.org_member import OrgMember

# TODO update the JSON string below
json = "{}"
# create an instance of OrgMember from a JSON string
org_member_instance = OrgMember.from_json(json)
# print the JSON string representation of the object
print OrgMember.to_json()

# convert the object into a dict
org_member_dict = org_member_instance.to_dict()
# create an instance of OrgMember from a dict
org_member_form_dict = org_member.from_dict(org_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


