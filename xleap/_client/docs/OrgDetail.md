# OrgDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**members** | [**List[OrgDetailMembersInner]**](OrgDetailMembersInner.md) |  | 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**name** | **str** |  | 

## Example

```python
from xleap._client.models.org_detail import OrgDetail

# TODO update the JSON string below
json = "{}"
# create an instance of OrgDetail from a JSON string
org_detail_instance = OrgDetail.from_json(json)
# print the JSON string representation of the object
print OrgDetail.to_json()

# convert the object into a dict
org_detail_dict = org_detail_instance.to_dict()
# create an instance of OrgDetail from a dict
org_detail_form_dict = org_detail.from_dict(org_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


