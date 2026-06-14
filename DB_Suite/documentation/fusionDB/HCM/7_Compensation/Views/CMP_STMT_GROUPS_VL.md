# CMP_STMT_GROUPS_VL

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpstmtgroupsvl-6496.html#cmpstmtgroupsvl-6496](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpstmtgroupsvl-6496.html#cmpstmtgroupsvl-6496)

## Columns

- STMT_GROUP_ID
- BUSINESS_GROUP_ID
- GROUP_TYPE
- NAME
- LANGUAGE
- SOURCE_LANG
- OBJECT_VERSION_NUMBER
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN

## Query

```sql
SELECT B.STMT_GROUP_ID, B.BUSINESS_GROUP_ID, B.GROUP_TYPE, T.NAME, T.LANGUAGE, T.SOURCE_LANG, B.OBJECT_VERSION_NUMBER, B.CREATED_BY, B.CREATION_DATE, B.LAST_UPDATED_BY, B.LAST_UPDATE_DATE, B.LAST_UPDATE_LOGIN FROM CMP_STMT_GROUPS_B B, CMP_STMT_GROUPS_TL T WHERE B.STMT_GROUP_ID = T.STMT_GROUP_ID AND T.LANGUAGE = USERENV('LANG') AND B.BUSINESS_GROUP_ID = T.BUSINESS_GROUP_ID
```

---

[← Back to Index](../7_Compensation_Views_Index.md)
