# HWM_EVENT_ATRB_FLDS_VL

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmeventatrbfldsvl-7941.html#hwmeventatrbfldsvl-7941](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmeventatrbfldsvl-7941.html#hwmeventatrbfldsvl-7941)

## Columns

- TM_EVENT_ID
- TM_ATRB_FLD_ID
- ENTERPRISE_ID
- NAME
- DISPLAY_NAME
- CLASS
- ATTRIBUTE_CATEGORY
- ATTRIBUTE_TYPE
- ATTRIBUTE_GROUP
- ALLOWED_SCOPE

## Query

```sql
SELECT EventPEO.TM_EVENT_ID, AttrFieldVLPEO.TM_ATRB_FLD_ID, AttrFieldVLPEO.ENTERPRISE_ID, AttrFieldVLPEO.NAME, AttrFieldVLPEO.DISPLAY_NAME, AttrFieldVLPEO.CLASS, AttrFieldVLPEO.ATTRIBUTE_CATEGORY, AttrFieldVLPEO.ATTRIBUTE_TYPE, AttrFieldVLPEO.ATTRIBUTE_GROUP, AttrFieldVLPEO.ALLOWED_SCOPE FROM fusion.HWM_TM_EVENTS EventPEO, fusion.HWM_TM_ATRB_FLDS_VL AttrFieldVLPEO
```

---

[← Back to Index](../31_Workforce_Management_Views_Index.md)
