# HWR_RESUME_VL

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrresumevl-4778.html#hwrresumevl-4778](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrresumevl-4778.html#hwrresumevl-4778)

## Columns

- RESUME_ID
- ORIGINAL_ID
- SOURCE_ID
- DOWNLOAD_DATE
- RESUME_TEXT
- RESUME
- MIME_TYPE
- RESUME_METADATA
- CHECKSUM
- GBL_PRFL_ID
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN

## Query

```sql
SELECT B.RESUME_ID, B.ORIGINAL_ID, B.SOURCE_ID, B.DOWNLOAD_DATE, B.RESUME_TEXT, B.RESUME, B.MIME_TYPE, B.RESUME_METADATA, B.CHECKSUM, X.GBL_PRFL_ID, B.CREATED_BY, B.CREATION_DATE, B.LAST_UPDATED_BY, B.LAST_UPDATE_DATE, B.LAST_UPDATE_LOGIN FROM HWR_RESUME B LEFT JOIN HWR_RESUME_GBL_PRFL_X X ON (B.RESUME_ID = X.RESUME_ID AND B.SOURCE_ID = X.SOURCE_ID)
```

---

[← Back to Index](../34_Workforce_Reputation_Management_Views_Index.md)
