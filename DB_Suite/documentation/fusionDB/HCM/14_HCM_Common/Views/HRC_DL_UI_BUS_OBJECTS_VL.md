# HRC_DL_UI_BUS_OBJECTS_VL

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdluibusobjectsvl-6252.html#hrcdluibusobjectsvl-6252](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdluibusobjectsvl-6252.html#hrcdluibusobjectsvl-6252)

## Columns

- UI_BUSINESS_OBJECT_ID
- UI_BUSINESS_OBJECT_GUID
- MODULE_ID
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN
- OBJECT_VERSION_NUMBER
- ENTERPRISE_ID
- UI_NAME
- UI_DESCRIPTION

## Query

```sql
SELECT B.UI_BUSINESS_OBJECT_ID , B.UI_BUSINESS_OBJECT_GUID , B.MODULE_ID , B.CREATED_BY , B.CREATION_DATE , B.LAST_UPDATED_BY , B.LAST_UPDATE_DATE , B.LAST_UPDATE_LOGIN , B.OBJECT_VERSION_NUMBER , B.ENTERPRISE_ID, T.UI_NAME , T.UI_DESCRIPTION FROM HRC_DL_UI_BUS_OBJECTS_B B , HRC_DL_UI_BUS_OBJECTS_TL T WHERE B.UI_BUSINESS_OBJECT_ID = T.UI_BUSINESS_OBJECT_ID AND T.LANGUAGE = userenv('LANG')
```

---

[← Back to Index](../14_HCM_Common_Views_Index.md)
