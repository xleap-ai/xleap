# ChartData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric** | **str** |  | 
**values** | **List[float]** |  | 

## Example

```python
from xleap._client.models.chart_data import ChartData

# TODO update the JSON string below
json = "{}"
# create an instance of ChartData from a JSON string
chart_data_instance = ChartData.from_json(json)
# print the JSON string representation of the object
print ChartData.to_json()

# convert the object into a dict
chart_data_dict = chart_data_instance.to_dict()
# create an instance of ChartData from a dict
chart_data_form_dict = chart_data.from_dict(chart_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


