# EEC_CONTEST_TEMPLATE_HDR_VL

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/eeccontesttemplatehdrvl-8283.html#eeccontesttemplatehdrvl-8283](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/eeccontesttemplatehdrvl-8283.html#eeccontesttemplatehdrvl-8283)

## Columns

- ROW_ID
- TEMPLATE_ID
- TEMPLATE_LOGO
- ACTIVE_FLAG
- TEMPLATE_NAME
- TEMPLATE_DESC
- LAST_UPDATE_DATE
- LAST_UPDATED_BY
- CREATION_DATE
- CREATED_BY
- LAST_UPDATE_LOGIN
- OBJECT_VERSION_NUMBER

## Query

```sql
SELECT B.ROWID ROW_ID, B.TEMPLATE_ID, B.TEMPLATE_LOGO, B.ACTIVE_FLAG, T.TEMPLATE_NAME, T.TEMPLATE_DESC, B.LAST_UPDATE_DATE, B.LAST_UPDATED_BY, B.CREATION_DATE, B.CREATED_BY, B.LAST_UPDATE_LOGIN, B.OBJECT_VERSION_NUMBER FROM EEC_CONTEST_TEMPLATE_HDR_TL T, EEC_CONTEST_TEMPLATE_HDR_B B WHERE B.TEMPLATE_ID = T.TEMPLATE_ID AND T.LANGUAGE = userenv('LANG')
```

---

[← Back to Index](../10_Global_Human_Resources_Views_Index.md)
