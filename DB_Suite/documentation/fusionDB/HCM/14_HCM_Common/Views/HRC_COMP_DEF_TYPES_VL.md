# HRC_COMP_DEF_TYPES_VL

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrccompdeftypesvl-8206.html#hrccompdeftypesvl-8206](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrccompdeftypesvl-8206.html#hrccompdeftypesvl-8206)

## Columns

- DEF_TYPE_ID
- IKEY
- NAME
- DESCRIPTION
- PRODUCT_CODE
- LEGISLATION_CODE
- DEF_TYPE_CODE
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
select deftype.def_type_id ,deftype.ikey ,tl.name ,tl.description ,deftype.product_code ,deftype.legislation_code ,deftype.def_type_code ,deftype.enterprise_id ,deftype.attr_char1 ,deftype.attr_char2 ,deftype.attr_char3 ,deftype.attr_number1 ,deftype.attr_number2 ,deftype.attr_number3 ,deftype.attr_date1 ,deftype.attr_date2 ,deftype.attr_date3 ,deftype.created_by ,deftype.creation_date ,deftype.last_updated_by ,deftype.last_update_date ,deftype.last_update_login ,deftype.object_version_number ,deftype.module_id ,deftype.sguid ,deftype.seed_data_source FROM HRC_COMP_DEF_TYPES_B deftype, HRC_COMP_DEF_TYPES_TL tl WHERE deftype.def_type_id = tl.def_type_id(+) AND tl.LANGUAGE(+) = USERENV('LANG')
```

---

[← Back to Index](../14_HCM_Common_Views_Index.md)
