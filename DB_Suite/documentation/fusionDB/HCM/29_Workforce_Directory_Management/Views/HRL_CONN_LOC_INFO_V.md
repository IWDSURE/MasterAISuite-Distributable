# HRL_CONN_LOC_INFO_V

## Details

**Schema:** FUSION

**Object owner:** HRL

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrlconnlocinfov-4026.html#hrlconnlocinfov-4026](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrlconnlocinfov-4026.html#hrlconnlocinfov-4026)

## Columns

- PERSON_ID
- ASSIGNMENT_ID
- LOCATION_ID
- DIRECT_REPORTS_CNT
- ALL_REPORTS_CNT
- RDATE
- RTYPE

## Query

```sql
select "PERSON_ID","ASSIGNMENT_ID","LOCATION_ID","DIRECT_REPORTS_CNT","ALL_REPORTS_CNT","RDATE","RTYPE" from ( select person_id, assignment_id, df_information_number1 location_id, df_information_number2 DIRECT_REPORTS_CNT, df_information_number3 ALL_REPORTS_CNT, last_update_date rdate, 'PP' rtype from hrl_data_feed_information x where df_information_category = 'ORA_DF_MGR_LOC_COUNTS' UNION select person_id, assignment_id, location_id, DIRECT_REPORTS_CNT, ALL_REPORTS_CNT, sysdate rdate, 'RT' rtype from ( select manager_id person_id, manager_assignment_id assignment_id , 'ORA_DF_MGR_LOC_COUNTS' info_catg, paam.location_id , SUM(decode(manager_level, 1, 1, 0)) DIRECT_REPORTS_CNT, count(1) ALL_REPORTS_CNT from per_manager_hrchy_dn pmdh, hrl_conn_public_workers_v paam where 1=1 and not exists (select 1 from hrl_data_feed_information x where person_id = pmdh.manager_id and assignment_id = pmdh.manager_assignment_id and df_information_category = 'ORA_DF_MGR_LOC_COUNTS') and pmdh.person_id = paam.person_id and pmdh.assignment_id = paam.assignment_id and trunc(sysdate) between pmdh.effective_start_date and pmdh.effective_end_date and trunc(sysdate) between paam.effective_start_date and paam.effective_end_date and paam.effective_latest_change = 'Y' and paam.assignment_type IN ('E','C','N') and exists (select 1 from per_all_assignments_m where person_id = pmdh.manager_id and assignment_id = pmdh.manager_assignment_id and trunc(sysdate) between effective_start_date and effective_end_date and effective_latest_change = 'Y' and assignment_status_type != 'INACTIVE') group by pmdh.manager_id, pmdh.manager_assignment_id, paam.location_id ) )
```

---

[← Back to Index](../29_Workforce_Directory_Management_Views_Index.md)
