# HWR_RCMNDTN_VL

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrrcmndtnvl-6463.html#hwrrcmndtnvl-6463](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrrcmndtnvl-6463.html#hwrrcmndtnvl-6463)

## Columns

- RECOMMENDATION_ID
- SOURCE_ID
- RECOMMENDATION_TEXT
- RECOMMENDATION_TYPE
- RECOMMENDER_ID
- RECOMMENDER_URI
- PRFL_ID
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN

## Query

```sql
SELECT B.RECOMMENDATION_ID , B.SOURCE_ID , B.RECOMMENDATION_TEXT , B.RECOMMENDATION_TYPE , B.RECOMMENDER_ID , B.RECOMMENDER_URI , X.PRFL_ID , B.CREATED_BY , B.CREATION_DATE , B.LAST_UPDATED_BY , B.LAST_UPDATE_DATE , B.LAST_UPDATE_LOGIN FROM HWR_RCMNDTN_B B LEFT JOIN HWR_RCMNDTN_PRFL_X X ON (B.RECOMMENDATION_ID = X.RECOMMENDATION_ID AND B.SOURCE_ID = X.SOURCE_ID)
```

---

[← Back to Index](../34_Workforce_Reputation_Management_Views_Index.md)
