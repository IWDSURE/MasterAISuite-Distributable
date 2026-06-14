# HWM_RULE_TM_REC_PERSON_V

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmruletmrecpersonv-8756.html#hwmruletmrecpersonv-8756](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmruletmrecpersonv-8756.html#hwmruletmrecpersonv-8756)

## Columns

- TM_REC_GRP_ID
- TM_REC_GRP_VERSION
- START_DATE
- END_DATE
- RESOURCE_ID
- LATEST_VERSION
- DELETE_FLAG
- DISPLAY_NAME
- NAME_AND_DATE
- PERSON_ID
- BUSINESS_GROUP_ID
- ENTERPRISE_ID

## Query

```sql
select th.tm_rec_grp_id , th.tm_rec_grp_version ,trunc(th.start_time) start_date ,trunc(th.stop_time) as end_date ,th.resource_id , th.latest_version , th.delete_flag ,nm.LIST_NAME as display_name ,cast( CASE WHEN (length(nm.LIST_NAME ) = null) THEN 'null' WHEN (length(nm.LIST_NAME ) <35) THEN nm.LIST_NAME ELSE CONCAT(SUBSTR (nm.LIST_NAME ,0,32),'...') end || ' (' || TO_CHAR(th.start_time , 'YYYY-MON-DD') || ' - ' || TO_CHAR(th.stop_time , 'YYYY-MON-DD') || ' ) ' as varchar2(280 CHAR) ) name_and_date ,nm.person_id ,nm.business_group_id ,th.enterprise_id from hwm_tm_rec_grp th , per_person_names_f_v nm where nm.person_id = th.resource_id and th.parent_tm_rec_grp_id is null and trunc(sysdate) between nm.effective_start_date and nm.effective_end_date
```

---

[← Back to Index](../31_Workforce_Management_Views_Index.md)
