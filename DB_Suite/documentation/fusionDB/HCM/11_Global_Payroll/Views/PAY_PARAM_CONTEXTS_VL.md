# PAY_PARAM_CONTEXTS_VL

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payparamcontextsvl-3480.html#payparamcontextsvl-3480](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/payparamcontextsvl-3480.html#payparamcontextsvl-3480)

## Columns

- PARAM_CONTEXT_ID
- BASE_CONTEXT_NAME
- PERSIST_FLAG
- CREATED_BY
- CREATION_DATE
- LAST_UPDATE_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_LOGIN
- OBJECT_VERSION_NUMBER
- ENTERPRISE_ID
- MODULE_ID
- CONTEXT_NAME
- DESCRIPTION

## Query

```sql
SELECT B.PARAM_CONTEXT_ID, B.BASE_CONTEXT_NAME, B.PERSIST_FLAG, B.CREATED_BY, B.CREATION_DATE, B.LAST_UPDATE_DATE, B.LAST_UPDATED_BY, B.LAST_UPDATE_LOGIN, B.OBJECT_VERSION_NUMBER, B.ENTERPRISE_ID, B.MODULE_ID, TL.CONTEXT_NAME, TL.DESCRIPTION FROM PAY_PARAM_CONTEXTS_B B, PAY_PARAM_CONTEXTS_TL TL WHERE B.PARAM_CONTEXT_ID = TL.PARAM_CONTEXT_ID AND USERENV('LANG') = TL.LANGUAGE
```

---

[← Back to Index](../11_Global_Payroll_Views_Index.md)
