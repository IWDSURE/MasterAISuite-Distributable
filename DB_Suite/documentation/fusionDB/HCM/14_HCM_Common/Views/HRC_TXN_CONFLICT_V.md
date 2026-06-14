# HRC_TXN_CONFLICT_V

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrctxnconflictv-4101.html#hrctxnconflictv-4101](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrctxnconflictv-4101.html#hrctxnconflictv-4101)

## Columns

- CHILD_ID
- TRANSACTION_ID
- PARENT_OBJ_ID
- OBJECT_NAME
- OBJECT_ID
- CREATED_BY
- CREATION_DATE

## Query

```sql
SELECT CHD. CHILD_ID CHILD_ID, CHD.PARENT_TXN_ID TRANSACTION_ID, CHD.PARENT_OBJ_ID PARENT_OBJ_ID, CHD.CHILD_OBJ OBJECT_NAME, CHD.CHILD_OBJ_ID OBJECT_ID, CHD.CREATED_BY CREATED_BY, CHD.CREATION_DATE CREATION_DATE FROM HRC_TXN_CHILD_OBJECTS CHD, HRC_TXN_DATA TXDT where 1 = 1 And TXDT.TRANSACTION_ID = CHD.PARENT_TXN_ID AND ( STATUS = 'PENDING' )
```

---

[← Back to Index](../14_HCM_Common_Views_Index.md)
