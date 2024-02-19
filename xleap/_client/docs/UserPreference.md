# UserPreference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selected_project** | **str** | the last selected project of the user | [optional] 

## Example

```python
from xleap._client.models.user_preference import UserPreference

# TODO update the JSON string below
json = "{}"
# create an instance of UserPreference from a JSON string
user_preference_instance = UserPreference.from_json(json)
# print the JSON string representation of the object
print UserPreference.to_json()

# convert the object into a dict
user_preference_dict = user_preference_instance.to_dict()
# create an instance of UserPreference from a dict
user_preference_form_dict = user_preference.from_dict(user_preference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


