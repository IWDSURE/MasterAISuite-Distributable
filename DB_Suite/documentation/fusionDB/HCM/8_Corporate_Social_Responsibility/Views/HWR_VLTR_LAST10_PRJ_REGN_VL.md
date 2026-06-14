# HWR_VLTR_LAST10_PRJ_REGN_VL

## Details

**Schema:** FUSION

**Object owner:** HHR

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrvltrlast10prjregnvl-6836.html#hwrvltrlast10prjregnvl-6836](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrvltrlast10prjregnvl-6836.html#hwrvltrlast10prjregnvl-6836)

## Columns

- VOLUNTEERSPERPROJECT
- PROJECTID
- ORGANIZATIONID

## Query

```sql
select count(distinct(B.HCM_PERSON_ID)) as VOLUNTEERSPERPROJECT, B.PROJECT_ID as PROJECTID, A.ORGANIZATIONID as ORGANIZATIONID from HWR_VLTR_VOL_PROJ_REL_VL B, (select PROJECT_ID, ORGANIZATION_ID as ORGANIZATIONID from HWR_VLTR_PROJECT_VL where TO_TIMESTAMP(END_DATE) < CURRENT_TIMESTAMP and rownum < 11 order by END_DATE DESC) A where B.PROJECT_ID = A.PROJECT_ID and B.STATUS = 'VOLUNTEERED' and A.ORGANIZATIONID in (select ENTITY_ID from HWR_VLTR_ADDRESS_VL where ENTITY_TYPE='Organization' ) group by B.PROJECT_ID, A.ORGANIZATIONID
```

---

[← Back to Index](../8_Corporate_Social_Responsibility_Views_Index.md)
