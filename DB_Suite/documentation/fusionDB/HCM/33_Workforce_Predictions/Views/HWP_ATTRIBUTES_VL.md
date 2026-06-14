# HWP_ATTRIBUTES_VL

## Details

**Schema:** FUSION

**Object owner:** HWP

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwpattributesvl-7980.html#hwpattributesvl-7980](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwpattributesvl-7980.html#hwpattributesvl-7980)

## Columns

- ENTERPRISE_ID
- ATTRIBUTE_ID
- ATTR_CODE
- ATTR_CATEGORY
- ATTR_NAME
- ATTR_DESCRIPTION
- DATA_TYPE
- DEFAULT_VALUE
- DBI_GROUP_ID
- FUNCTION_KEY
- RANGE_TYPE
- MIN_VALUE
- MAX_VALUE
- INCR_VALUE
- ATTR_UNIT
- UI_DISPLAY_TYPE
- UI_VALUE_TYPE
- UI_VALUE_DETAIL
- UI_ID_ATTR
- UI_VALUE_ATTR
- UI_WHATIF_FLAG
- MODULE_ID
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN
- OBJECT_VERSION_NUMBER

## Query

```sql
select ha.enterprise_id, ha.attribute_id, ha.ATTR_CODE, ha.attr_category, hat.attr_name, hat.attr_description, ha.DATA_TYPE, ha.DEFAULT_VALUE, ha.DBI_GROUP_ID, ha.FUNCTION_KEY, ha.RANGE_TYPE, ha.MIN_VALUE, ha.MAX_VALUE, ha.INCR_VALUE, ha.ATTR_UNIT, ha.UI_DISPLAY_TYPE, ha.UI_VALUE_TYPE, ha.UI_VALUE_DETAIL, ha.UI_ID_ATTR, ha.UI_VALUE_ATTR, ha.UI_WHATIF_FLAG, ha.MODULE_ID, ha.CREATED_BY, ha.CREATION_DATE, ha.LAST_UPDATED_BY, ha.LAST_UPDATE_DATE, ha.LAST_UPDATE_LOGIN, ha.OBJECT_VERSION_NUMBER FROM HWP_ATTRIBUTES_b HA, hwp_attributes_tl hat where ha.attribute_id = hat.attribute_id AND hat.LANGUAGE = USERENV('LANG')
```

---

[← Back to Index](../33_Workforce_Predictions_Views_Index.md)
