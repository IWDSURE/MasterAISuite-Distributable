# PAY_DATED_TABLES

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paydatedtables-3681.html#paydatedtables-3681](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paydatedtables-3681.html#paydatedtables-3681)

## Columns

- DATED_TABLE_ID
- TABLE_NAME
- ENTITY_NAME
- SURROGATE_KEY_NAME
- START_DATE_NAME
- END_DATE_NAME
- ENTERPRISE_ID

## Query

```sql
select heso.source_object_id dated_table_id, heso.table_name table_name, heso.name entity_name, max(decode(hesoa.primary_key,'Y', hesoa.column_name,null)) surrogate_key_name, max(decode(hesoa.date_effective_start_date,'Y', hesoa.column_name,decode( hesoa.column_name,'DATE_FROM','DATE_FROM','DATE_START','DATE_START','START_DATE','START_DATE',null))) start_date_name, max(decode(hesoa.date_effective_end_date,'Y', hesoa.column_name,decode( hesoa.column_name,'DATE_TO','DATE_TO','ACTUAL_TERMINATION_DATE','ACTUAL_TERMINATION_DATE','END_DATE','END_DATE',null))) end_date_name, heso.enterprise_id from hrc_evt_source_objects heso, hrc_evt_src_obj_attributes hesoa where heso.source_object_id=hesoa.source_object_id and table_name is not null and hesoa.column_name is not null and ((hesoa.primary_key='Y' and pk_sequence=1) or hesoa.date_effective_start_date='Y' or hesoa.date_effective_end_date='Y' or hesoa.column_name in ('DATE_FROM','DATE_TO','DATE_START','ACTUAL_TERMINATION_DATE','START_DATE','END_DATE')) group by heso.source_object_id, heso.table_name, heso.name, heso.enterprise_id
```

---

[← Back to Index](../11_Global_Payroll_Views_Index.md)
