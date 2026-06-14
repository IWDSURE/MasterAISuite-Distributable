# HWR_VLTR_COMMENT_VL

## Details

**Schema:** FUSION

**Object owner:** HHR

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrvltrcommentvl-7374.html#hwrvltrcommentvl-7374](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrvltrcommentvl-7374.html#hwrvltrcommentvl-7374)

## Columns

- COMMENT_ID
- ENTITY_ID
- ENTITY_TYPE
- ENTITY_STATE
- ENTITY_COMMENT
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN

## Query

```sql
SELECT A.COMMENT_ID COMMENT_ID, A.ENTITY_ID ENTITY_ID, A.ENTITY_TYPE ENTITY_TYPE, A.ENTITY_STATE ENTITY_STATE, B.ENTITY_COMMENT ENTITY_COMMENT, A.CREATED_BY CREATED_BY, A.CREATION_DATE CREATION_DATE, A.LAST_UPDATED_BY LAST_UPDATED_BY, A.LAST_UPDATE_DATE LAST_UPDATE_DATE, A.LAST_UPDATE_LOGIN LAST_UPDATE_LOGIN FROM HWR_VLTR_COMMENT_B A, HWR_VLTR_COMMENT_TL B WHERE A.COMMENT_ID = B.COMMENT_ID AND B.LANGUAGE= USERENV('LANG')
```

---

[← Back to Index](../8_Corporate_Social_Responsibility_Views_Index.md)
