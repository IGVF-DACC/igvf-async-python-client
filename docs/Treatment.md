# Treatment

A protein or chemical treatment applied to samples such as lipopolysaccharide, interleukin-2, or leucine.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**preview_timestamp** | **str** | The date the object was previewed. | [optional] 
**release_timestamp** | **str** | The date the object was released. | [optional] 
**lab** | **str** | Lab associated with the submission. | [optional] 
**award** | **str** | Grant associated with the submission. | [optional] 
**sources** | **List[str]** | The originating lab(s) or vendor(s). | [optional] 
**lot_id** | **str** | The lot identifier provided by the originating lab or vendor. | [optional] 
**product_id** | **str** | The product identifier provided by the originating lab or vendor. | [optional] 
**documents** | **List[str]** | Documents that describe the treatment protocol details. | [optional] 
**status** | **str** | The status of the metadata object. | [optional] 
**schema_version** | **str** | The version of the JSON schema that the server uses to validate the object. | [optional] 
**uuid** | **str** | The unique identifier associated with every object. | [optional] 
**notes** | **str** | DACC internal notes. | [optional] 
**aliases** | **List[str]** | Lab specific identifiers to reference an object. | [optional] 
**creation_timestamp** | **str** | The date the object was created. | [optional] 
**submitted_by** | **str** | The user who submitted the object. | [optional] 
**submitter_comment** | **str** | Additional information specified by the submitter to be displayed as a comment on the portal. | [optional] 
**description** | **str** | A plain text description of the object. | [optional] 
**amount** | **float** | Specific quantity of the applied treatment (used in conjunction with amount_units). | [optional] 
**amount_units** | **str** | A unit for an amount other than those for time or temperature. | [optional] 
**duration** | **float** | Duration indicates the time elapsed between the start and end of the treatment. | [optional] 
**duration_units** | **str** | A unit of time. | [optional] 
**p_h** | **float** | Final pH of the solution containing a chemical compound (if applicable) | [optional] 
**purpose** | **str** | The intended purpose for treating the samples. | [optional] 
**post_treatment_time** | **float** | Post treatment time in conjunction with post treatment time units is used to specify the time that has passed between the point when biosamples were removed from the treatment solution before being sampled or treated with the next treatment. | [optional] 
**post_treatment_time_units** | **str** | A unit of time. | [optional] 
**temperature** | **float** | The temperature in Celsius to which the sample was exposed | [optional] 
**temperature_units** | **str** | A unit of temperature. | [optional] 
**treatment_type** | **str** | The classification of treatment agent that specifies its exact molecular nature.  | [optional] 
**treatment_term_id** | **str** | Ontology identifier describing a component in the treatment. | [optional] 
**treatment_term_name** | **str** | Ontology term describing a component in the treatment that is the principal component affecting the biosample being treated. Examples: interferon gamma, interleukin-4, Fibroblast growth factor 2, 20-hydroxyecdysone, 5-bromouridine etc. | [optional] 
**depletion** | **bool** | Treatment is depleted. | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**summary** | **str** |  | [optional] 
**biosamples_treated** | **List[str]** | The samples which have been treated using this treatment. | [optional] 

## Example

```python
from igvf_async_client.models.treatment import Treatment

# TODO update the JSON string below
json = "{}"
# create an instance of Treatment from a JSON string
treatment_instance = Treatment.from_json(json)
# print the JSON string representation of the object
print(Treatment.to_json())

# convert the object into a dict
treatment_dict = treatment_instance.to_dict()
# create an instance of Treatment from a dict
treatment_from_dict = Treatment.from_dict(treatment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


