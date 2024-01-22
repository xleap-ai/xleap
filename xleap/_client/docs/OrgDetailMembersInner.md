# OrgDetailMembersInner


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
from xleap._client.models.org_detail_members_inner import OrgDetailMembersInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrgDetailMembersInner from a JSON string
org_detail_members_inner_instance = OrgDetailMembersInner.from_json(json)
# print the JSON string representation of the object
print OrgDetailMembersInner.to_json()

# convert the object into a dict
org_detail_members_inner_dict = org_detail_members_inner_instance.to_dict()
# create an instance of OrgDetailMembersInner from a dict
org_detail_members_inner_form_dict = org_detail_members_inner.from_dict(org_detail_members_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


