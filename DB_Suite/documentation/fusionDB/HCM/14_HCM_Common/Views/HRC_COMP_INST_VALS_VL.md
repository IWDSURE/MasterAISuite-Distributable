# HRC_COMP_INST_VALS_VL

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrccompinstvalsvl-5555.html#hrccompinstvalsvl-5555](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrccompinstvalsvl-5555.html#hrccompinstvalsvl-5555)

## Columns

- INSTANCE_VALUE_ID
- IKEY
- INSTANCE_ID
- TEMPLATE_ID
- ITEM_ID
- ENTERPRISE_ID
- CAT_DEF_VAL_ID
- OPT_DEF_VAL_ID
- VALUE_TYPE
- VALUE_NAME
- VALUE_DATATYPE
- VALUE_SUPPLIED
- VALUE_VARCHAR2
- VALUE_CLOB
- VALUE_BLOB
- VALUE_DATE
- VALUE_TIMESTAMP
- VALUE_NUMBER
- SUGV_FLAG
- VALUE_SKID
- FOOTNOTE_REFS
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

## Query

```sql
select inst.instance_value_id ,inst.ikey ,inst.instance_id ,inst.template_id ,inst.item_id ,inst.enterprise_id ,inst.cat_def_val_id ,inst.opt_def_val_id ,inst.value_type ,inst.value_name ,inst.value_datatype ,tl.value_supplied ,inst.value_varchar2 ,inst.value_clob ,inst.value_blob ,inst.value_date ,inst.value_timestamp ,inst.value_number ,inst.sugv_flag ,inst.value_skid ,inst.footnote_refs ,inst.attr_char1 ,inst.attr_char2 ,inst.attr_char3 ,inst.attr_number1 ,inst.attr_number2 ,inst.attr_number3 ,inst.attr_date1 ,inst.attr_date2 ,inst.attr_date3 ,inst.created_by ,inst.creation_date ,inst.last_updated_by ,inst.last_update_date ,inst.last_update_login ,inst.object_version_number FROM HRC_COMP_INST_VALS_B inst, HRC_COMP_INST_VALS_TL tl WHERE inst.instance_value_id = tl.instance_value_id(+) AND tl.LANGUAGE(+) = USERENV('LANG')
```

---

[← Back to Index](../14_HCM_Common_Views_Index.md)
