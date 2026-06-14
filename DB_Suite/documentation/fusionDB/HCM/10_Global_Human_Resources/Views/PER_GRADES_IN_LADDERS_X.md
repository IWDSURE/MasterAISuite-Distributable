# PER_GRADES_IN_LADDERS_X

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/pergradesinladdersx-7571.html#pergradesinladdersx-7571](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/pergradesinladdersx-7571.html#pergradesinladdersx-7571)

## Columns

- GRADES_IN_LADDER_ID
- EFFECTIVE_START_DATE
- EFFECTIVE_END_DATE
- ACTION_OCCURRENCE_ID
- GRADE_LADDER_ID
- GRADE_ID
- SEQUENCE
- OBJECT_VERSION_NUMBER
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN

## Query

```sql
SELECT GRADES_IN_LADDER_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, ACTION_OCCURRENCE_ID, GRADE_LADDER_ID, GRADE_ID, SEQUENCE, OBJECT_VERSION_NUMBER, CREATED_BY, CREATION_DATE, LAST_UPDATED_BY, LAST_UPDATE_DATE, LAST_UPDATE_LOGIN FROM PER_GRADES_IN_LADDERS_F WHERE TRUNC(sysdate) BETWEEN EFFECTIVE_START_DATE AND EFFECTIVE_END_DATE
```

---

[← Back to Index](../10_Global_Human_Resources_Views_Index.md)
