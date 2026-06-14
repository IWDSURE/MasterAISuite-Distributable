# HRA_PF_TASK_DEFNS_VL

## Details

**Schema:** FUSION

**Object owner:** HRA

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrapftaskdefnsvl-6672.html#hrapftaskdefnsvl-6672](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrapftaskdefnsvl-6672.html#hrapftaskdefnsvl-6672)

## Columns

- TASK_ID
- TASK_CODE
- ACTIVE_FLAG
- MODULE_ID
- BUSINESS_GROUP_ID
- TASK_NAME
- OBJECT_VERSION_NUMBER
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN

## Query

```sql
SELECT TDB.TASK_ID, TDB.TASK_CODE, TDB.ACTIVE_FLAG, TDB.MODULE_ID, TDB.BUSINESS_GROUP_ID, TDTL.TASK_NAME, TDB.OBJECT_VERSION_NUMBER, TDB.CREATED_BY, TDB.CREATION_DATE, TDB.LAST_UPDATED_BY, TDB.LAST_UPDATE_DATE, TDB.LAST_UPDATE_LOGIN FROM HRA_PF_TASK_DEFNS_B TDB, HRA_PF_TASK_DEFNS_TL TDTL WHERE TDB.TASK_ID = TDTL.TASK_ID AND TDB.BUSINESS_GROUP_ID = TDTL.BUSINESS_GROUP_ID AND TDTL.LANGUAGE = USERENV('LANG')
```

---

[← Back to Index](../19_Performance_Management_Views_Index.md)
