# IndexFileResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graph** | [**List[IndexFile]**](IndexFile.md) |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**total** | **int** |  | [optional] 
**facets** | [**List[SearchFacet]**](SearchFacet.md) |  | [optional] 

## Example

```python
from igvf_async_client.models.index_file_results import IndexFileResults

# TODO update the JSON string below
json = "{}"
# create an instance of IndexFileResults from a JSON string
index_file_results_instance = IndexFileResults.from_json(json)
# print the JSON string representation of the object
print(IndexFileResults.to_json())

# convert the object into a dict
index_file_results_dict = index_file_results_instance.to_dict()
# create an instance of IndexFileResults from a dict
index_file_results_from_dict = IndexFileResults.from_dict(index_file_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


