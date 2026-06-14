# CMP_TCS_STMT_CAT_VL

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcsstmtcatvl-8387.html#cmptcsstmtcatvl-8387](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmptcsstmtcatvl-8387.html#cmptcsstmtcatvl-8387)

## Columns

- STMT_CAT_ID
- DISPLAY_NAME
- STMT_ID
- CAT_ID
- ORDR_NUM
- BUSINESS_GROUP_ID
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN
- OBJECT_VERSION_NUMBER

## Query

```sql
SELECT STMT.STMT_CAT_ID , STMT_TL.DISPLAY_NAME, STMT.STMT_ID , STMT.CAT_ID , STMT.ORDR_NUM , STMT.BUSINESS_GROUP_ID , STMT.CREATED_BY , STMT.CREATION_DATE , STMT.LAST_UPDATED_BY , STMT.LAST_UPDATE_DATE , STMT.LAST_UPDATE_LOGIN, STMT.OBJECT_VERSION_NUMBER FROM CMP_TCS_STMT_CAT STMT , CMP_TCS_STMT_CAT_TL STMT_TL WHERE STMT.STMT_CAT_ID = STMT_TL.STMT_CAT_ID AND STMT_TL.LANGUAGE = USERENV('LANG') AND STMT.BUSINESS_GROUP_ID = STMT_TL.BUSINESS_GROUP_ID
```

---

[← Back to Index](../7_Compensation_Views_Index.md)
