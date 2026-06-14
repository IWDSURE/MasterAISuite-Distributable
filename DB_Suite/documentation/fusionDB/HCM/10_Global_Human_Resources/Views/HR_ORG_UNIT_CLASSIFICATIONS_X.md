# HR_ORG_UNIT_CLASSIFICATIONS_X

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrorgunitclassificationsx-5358.html#hrorgunitclassificationsx-5358](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrorgunitclassificationsx-5358.html#hrorgunitclassificationsx-5358)

## Columns

- ORG_UNIT_CLASSIFICATION_ID
- EFFECTIVE_START_DATE
- EFFECTIVE_END_DATE
- ORGANIZATION_ID
- CLASSIFICATION_CODE
- STATUS
- SET_ID
- OBJECT_VERSION_NUMBER
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN

## Query

```sql
SELECT ORG_UNIT_CLASSIFICATION_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, ORGANIZATION_ID, CLASSIFICATION_CODE, STATUS, SET_ID, OBJECT_VERSION_NUMBER, CREATED_BY, CREATION_DATE, LAST_UPDATED_BY, LAST_UPDATE_DATE, LAST_UPDATE_LOGIN FROM HR_ORG_UNIT_CLASSIFICATIONS_F WHERE TRUNC(sysdate) BETWEEN EFFECTIVE_START_DATE AND EFFECTIVE_END_DATE
```

---

[← Back to Index](../10_Global_Human_Resources_Views_Index.md)
