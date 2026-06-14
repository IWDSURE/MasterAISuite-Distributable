# HWR_VLTR_EMPL_PER_CAT_VL

## Details

**Schema:** FUSION

**Object owner:** HHR

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrvltremplpercatvl-4259.html#hwrvltremplpercatvl-4259](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrvltremplpercatvl-4259.html#hwrvltremplpercatvl-4259)

## Columns

- PROJ_ID
- SUBSCRIBED_VOLUNTEERS
- AREAS_OF_INTEREST

## Query

```sql
SELECT A.PROJECT_ID PROJ_ID, COUNT(A.HCM_PERSON_ID) SUBSCRIBED_VOLUNTEERS, B.AREAS_OF_INTEREST AREAS_OF_INTEREST FROM HWR_VLTR_VOL_PROJ_REL_B A, HWR_VLTR_PROJECT_B B, HWR_VLTR_VOL_PROJ_REL_TL C WHERE A.PROJECT_ID = B.PROJECT_ID AND B.STATUS = 'ACTIVE' AND A.ID = C.ID AND C.STATUS = 'SUBSCRIBED' AND C.LANGUAGE = USERENV('LANG') GROUP BY A.PROJECT_ID, B.AREAS_OF_INTEREST ORDER BY PROJ_ID
```

---

[← Back to Index](../8_Corporate_Social_Responsibility_Views_Index.md)
