# WorkflowResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graph** | [**List[Workflow]**](Workflow.md) |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**total** | **int** |  | [optional] 
**facets** | [**List[SearchFacet]**](SearchFacet.md) |  | [optional] 

## Example

```python
from igvf_async_client.models.workflow_results import WorkflowResults

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowResults from a JSON string
workflow_results_instance = WorkflowResults.from_json(json)
# print the JSON string representation of the object
print(WorkflowResults.to_json())

# convert the object into a dict
workflow_results_dict = workflow_results_instance.to_dict()
# create an instance of WorkflowResults from a dict
workflow_results_from_dict = WorkflowResults.from_dict(workflow_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


