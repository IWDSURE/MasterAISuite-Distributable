# HWR_PUBLICATION_VL

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrpublicationvl-7961.html#hwrpublicationvl-7961](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrpublicationvl-7961.html#hwrpublicationvl-7961)

## Columns

- PUBLICATION_ID
- SOURCE_ID
- AUTHORS
- PUBLICATION_DATE
- DESCRIPTION
- TITLE
- PUBLICATION_TYPE
- URL
- PRFL_ID
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN

## Query

```sql
SELECT B.PUBLICATION_ID , B.SOURCE_ID , B.AUTHORS , B.PUBLICATION_DATE , B.DESCRIPTION , B.TITLE , B.PUBLICATION_TYPE , B.URL , X.PRFL_ID , B.CREATED_BY , B.CREATION_DATE , B.LAST_UPDATED_BY , B.LAST_UPDATE_DATE , B.LAST_UPDATE_LOGIN FROM HWR_PUBLICATION_B B LEFT JOIN HWR_PUBLICATION_PRFL_X X ON (B.PUBLICATION_ID = X.PUBLICATION_ID AND B.SOURCE_ID = X.SOURCE_ID)
```

---

[← Back to Index](../34_Workforce_Reputation_Management_Views_Index.md)
