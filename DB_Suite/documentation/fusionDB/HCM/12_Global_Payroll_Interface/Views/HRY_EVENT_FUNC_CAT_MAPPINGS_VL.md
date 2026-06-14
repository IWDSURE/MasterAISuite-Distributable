# HRY_EVENT_FUNC_CAT_MAPPINGS_VL

## Details

**Schema:** FUSION

**Object owner:** HRY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hryeventfunccatmappingsvl-3302.html#hryeventfunccatmappingsvl-3302](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hryeventfunccatmappingsvl-3302.html#hryeventfunccatmappingsvl-3302)

## Columns

- EVENT_FUNC_CAT_MAP_ID
- EVENT_CATEGORY_ID
- EVENT_FUNC_CAT_BASE_NAME
- ATTRIBUTE_CATEGORY
- ATTRIBUTE1
- ATTRIBUTE2
- ATTRIBUTE3
- ATTRIBUTE4
- ATTRIBUTE5
- ATTRIBUTE6
- ATTRIBUTE7
- ATTRIBUTE8
- ATTRIBUTE9
- ATTRIBUTE10
- LEGISLATION_CODE
- MODULE_ID
- ENTERPRISE_ID
- OBJECT_VERSION_NUMBER
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN
- SGUID
- SEED_DATA_SOURCE
- ORA_SEED_SET1
- ORA_SEED_SET2
- EVENT_FUNC_CAT_NAME
- DESCRIPTION

## Query

```sql
SELECT hry_event_func_cat_mappings_b.EVENT_FUNC_CAT_MAP_ID EVENT_FUNC_CAT_MAP_ID, hry_event_func_cat_mappings_b.EVENT_CATEGORY_ID EVENT_CATEGORY_ID, hry_event_func_cat_mappings_b.EVENT_FUNC_CAT_BASE_NAME EVENT_FUNC_CAT_BASE_NAME, hry_event_func_cat_mappings_b.ATTRIBUTE_CATEGORY ATTRIBUTE_CATEGORY, hry_event_func_cat_mappings_b.ATTRIBUTE1 ATTRIBUTE1, hry_event_func_cat_mappings_b.ATTRIBUTE2 ATTRIBUTE2, hry_event_func_cat_mappings_b.ATTRIBUTE3 ATTRIBUTE3, hry_event_func_cat_mappings_b.ATTRIBUTE4 ATTRIBUTE4, hry_event_func_cat_mappings_b.ATTRIBUTE5 ATTRIBUTE5, hry_event_func_cat_mappings_b.ATTRIBUTE6 ATTRIBUTE6, hry_event_func_cat_mappings_b.ATTRIBUTE7 ATTRIBUTE7, hry_event_func_cat_mappings_b.ATTRIBUTE8 ATTRIBUTE8, hry_event_func_cat_mappings_b.ATTRIBUTE9 ATTRIBUTE9, hry_event_func_cat_mappings_b.ATTRIBUTE10 ATTRIBUTE10, hry_event_func_cat_mappings_b.LEGISLATION_CODE LEGISLATION_CODE, hry_event_func_cat_mappings_b.MODULE_ID MODULE_ID, hry_event_func_cat_mappings_b.ENTERPRISE_ID ENTERPRISE_ID, hry_event_func_cat_mappings_b.OBJECT_VERSION_NUMBER OBJECT_VERSION_NUMBER, hry_event_func_cat_mappings_b.CREATED_BY CREATED_BY, hry_event_func_cat_mappings_b.CREATION_DATE CREATION_DATE, hry_event_func_cat_mappings_b.LAST_UPDATED_BY LAST_UPDATED_BY, hry_event_func_cat_mappings_b.LAST_UPDATE_DATE LAST_UPDATE_DATE, hry_event_func_cat_mappings_b.LAST_UPDATE_LOGIN LAST_UPDATE_LOGIN, hry_event_func_cat_mappings_b.SGUID SGUID, hry_event_func_cat_mappings_b.SEED_DATA_SOURCE SEED_DATA_SOURCE, hry_event_func_cat_mappings_b.ORA_SEED_SET1 ORA_SEED_SET1, hry_event_func_cat_mappings_b.ORA_SEED_SET2 ORA_SEED_SET2, hry_event_func_cat_mappings_tl.EVENT_FUNC_CAT_NAME, hry_event_func_cat_mappings_tl.DESCRIPTION DESCRIPTION FROM hry_event_func_cat_mappings_b, hry_event_func_cat_mappings_tl WHERE hry_event_func_cat_mappings_b.EVENT_FUNC_CAT_MAP_ID = hry_event_func_cat_mappings_tl.EVENT_FUNC_CAT_MAP_ID AND hry_event_func_cat_mappings_tl.LANGUAGE = USERENV('LANG')
```

---

[← Back to Index](../12_Global_Payroll_Interface_Views_Index.md)
