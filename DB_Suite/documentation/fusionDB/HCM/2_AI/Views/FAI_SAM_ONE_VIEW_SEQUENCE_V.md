# FAI_SAM_ONE_VIEW_SEQUENCE_V

## Details

**Schema:** FUSION

**Object owner:** FAI

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faisamoneviewsequencev-5412.html#faisamoneviewsequencev-5412](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faisamoneviewsequencev-5412.html#faisamoneviewsequencev-5412)

## Columns

- POD
- TYPE
- PARENT_SEQUENCE_ID
- PARENT_SEQUENCE
- SEQUENCE_ID
- SEQUENCE
- SEQUENCER
- ONE_VIEW_PROCESS_ID
- OBJECT_KEY
- PROCESS_TYPE
- PROCESS_NAME
- ID_METRIC
- PARENT_ID_METRIC
- PROCESS_STATUS
- LOAD
- LOAD_SUCCESS
- LOAD_ERROR
- PROCESSING_TIME
- THREAD_COUNT
- DAY
- START_TIME
- STOP_TIME
- PARAMETER
- PARAMETER_COMBINE
- PRODUCT

## Query

```sql
(select child.pod, child.type, parent.SEQUENCE_ID parent_sequence_id, parent.sequence parent_sequence, child.sequence_id, child.sequence, child.SEQUENCER , object.ONE_VIEW_PROCESS_ID, oneview.OBJECT_KEY, oneview.PROCESS_TYPE, oneview.PROCESS_NAME, ID_METRIC, PARENT_ID_METRIC, PROCESS_STATUS , LOAD, LOAD_SUCCESS, LOAD_ERROR, PROCESSING_TIME, THREAD_COUNT, DAY, START_TIME, STOP_TIME , PARAMETER , PARAMETER_COMBINE, oneview.product from fai_sam_sequence_object object, fai_sam_one_view_process oneview , fai_sam_sequence child, fai_sam_sequence parent where object.ONE_VIEW_PROCESS_ID = oneview.ONE_VIEW_PROCESS_ID and child.sequence_id = object.sequence_id and parent.sequence_id = object.PARENT_SEQUENCE_ID)
```

---

[← Back to Index](../2_AI_Views_Index.md)
