# HRC_COMP_DEF_VALS_VL

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrccompdefvalsvl-7111.html#hrccompdefvalsvl-7111](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrccompdefvalsvl-7111.html#hrccompdefvalsvl-7111)

## Columns

- DEF_VAL_ID
- IKEY
- DEF_TYPE_ID
- DISPLAY_SEQUENCE
- ENTERPRISE_ID
- NAME
- DESCRIPTION
- ATTR_CHAR1
- ATTR_CHAR2
- ATTR_CHAR3
- ATTR_NUMBER1
- ATTR_NUMBER2
- ATTR_NUMBER3
- ATTR_DATE1
- ATTR_DATE2
- ATTR_DATE3
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN
- OBJECT_VERSION_NUMBER
- MODULE_ID
- SGUID
- SEED_DATA_SOURCE

## Query

```sql
select defvals.def_val_id ,defvals.ikey ,defvals.def_type_id ,defvals.display_sequence ,defvals.enterprise_id ,tl.name ,tl.description ,defvals.attr_char1 ,defvals.attr_char2 ,defvals.attr_char3 ,defvals.attr_number1 ,defvals.attr_number2 ,defvals.attr_number3 ,defvals.attr_date1 ,defvals.attr_date2 ,defvals.attr_date3 ,defvals.created_by ,defvals.creation_date ,defvals.last_updated_by ,defvals.last_update_date ,defvals.last_update_login ,defvals.object_version_number ,defvals.module_id ,defvals.sguid ,defvals.seed_data_source FROM HRC_COMP_DEF_VALS_B defvals, HRC_COMP_DEF_VALS_TL tl WHERE defvals.def_val_id = tl.def_val_id(+) AND tl.LANGUAGE(+) = USERENV('LANG')
```

---

[← Back to Index](../14_HCM_Common_Views_Index.md)
