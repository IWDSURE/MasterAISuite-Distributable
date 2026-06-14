# HWR_DI_ADAPTER_VL

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrdiadaptervl-7395.html#hwrdiadaptervl-7395](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrdiadaptervl-7395.html#hwrdiadaptervl-7395)

## Columns

- ADAPTER_ID
- SOURCE_ID
- UUID
- ADAPTER_NAME
- ADAPTER_QUERY
- SOURCE_OBJECT_DEF
- TARGET_OBJECT_DEF
- QUERY_NAME
- DESCRIPTION
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN
- OBJECT_VERSION_NUMBER

## Query

```sql
SELECT B.ADAPTER_ID, B.SOURCE_ID, B.UUID, B.ADAPTER_NAME, B.ADAPTER_QUERY, B.SOURCE_OBJECT_DEF, B.TARGET_OBJECT_DEF, B.QUERY_NAME, T.DESCRIPTION, B.CREATED_BY, B.CREATION_DATE, B.LAST_UPDATED_BY, B.LAST_UPDATE_DATE, B.LAST_UPDATE_LOGIN, B.OBJECT_VERSION_NUMBER FROM HWR_DI_ADAPTER_B B, HWR_DI_ADAPTER_TL T WHERE B.ADAPTER_ID = T.ADAPTER_ID AND T.LANGUAGE = USERENV('LANG')
```

---

[← Back to Index](../34_Workforce_Reputation_Management_Views_Index.md)
