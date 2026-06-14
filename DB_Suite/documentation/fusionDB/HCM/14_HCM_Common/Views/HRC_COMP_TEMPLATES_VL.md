# HRC_COMP_TEMPLATES_VL

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrccomptemplatesvl-7221.html#hrccomptemplatesvl-7221](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrccomptemplatesvl-7221.html#hrccomptemplatesvl-7221)

## Columns

- TEMPLATE_ID
- IKEY
- DATE_FROM
- DATE_TO
- NAME
- DESCRIPTION
- COMP_DEF_TYPE_ID
- COMP_DEF_VAL_ID
- PRODUCT_CODE
- LEGISLATION_CODE
- USE_GROUPS_FLAG
- USE_CAT_FLAG
- CAT_DEF_TYPE_ID
- USE_OPT_FLAG
- OPT_DEF_TYPE_ID
- USE_HD_FLAG
- HD_TYPE
- HD_CODE
- USE_SUGV_FLAG
- SUGV_DEF_TYPE_ID
- ENTERPRISE_ID
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
select temp.template_id ,temp.ikey ,temp.date_from ,temp.date_to ,tl.name ,tl.description ,temp.comp_def_type_id ,temp.comp_def_val_id ,temp.product_code ,temp.legislation_code ,temp.use_groups_flag ,temp.use_cat_flag ,temp.cat_def_type_id ,temp.use_opt_flag ,temp.opt_def_type_id ,temp.use_hd_flag ,temp.hd_type ,temp.hd_code ,temp.use_sugv_flag ,temp.sugv_def_type_id ,temp.enterprise_id ,temp.attr_char1 ,temp.attr_char2 ,temp.attr_char3 ,temp.attr_number1 ,temp.attr_number2 ,temp.attr_number3 ,temp.attr_date1 ,temp.attr_date2 ,temp.attr_date3 ,temp.created_by ,temp.creation_date ,temp.last_updated_by ,temp.last_update_date ,temp.last_update_login ,temp.object_version_number ,temp.module_id ,temp.sguid ,temp.seed_data_source FROM HRC_COMP_TEMPLATES_B temp, HRC_COMP_TEMPLATES_TL tl WHERE temp.template_id = tl.template_id(+) AND tl.LANGUAGE(+) = USERENV('LANG')
```

---

[← Back to Index](../14_HCM_Common_Views_Index.md)
