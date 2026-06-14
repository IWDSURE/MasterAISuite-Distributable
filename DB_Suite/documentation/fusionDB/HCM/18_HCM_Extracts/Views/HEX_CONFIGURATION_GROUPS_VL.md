# HEX_CONFIGURATION_GROUPS_VL

## Details

**Schema:** FUSION

**Object owner:** HEX

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hexconfigurationgroupsvl-4693.html#hexconfigurationgroupsvl-4693](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hexconfigurationgroupsvl-4693.html#hexconfigurationgroupsvl-4693)

## Columns

- CONFIGURATION_GROUP_ID
- BASE_CONFIG_GROUP_CODE
- CONFIG_GROUP_NAME
- DESCRIPTION
- PARENT_CONFIG_GROUP_NAME
- LEGACY_PROCESS_CONFIG_CODE
- LEGACY_COMPATIBLE
- ENABLED_FLAG
- ATTRIBUTE_CATEGORY
- ATTRIBUTE1
- ATTRIBUTE2
- ATTRIBUTE3
- ATTRIBUTE4
- ATTRIBUTE5
- ENTERPRISE_ID
- MODULE_ID
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN
- OBJECT_VERSION_NUMBER
- SGUID

## Query

```sql
SELECT confgrpb.CONFIGURATION_GROUP_ID, confgrpb.BASE_CONFIG_GROUP_CODE, confgrptl.CONFIG_GROUP_NAME, confgrptl.DESCRIPTION, confgrpb.PARENT_CONFIG_GROUP_NAME, confgrpb.LEGACY_PROCESS_CONFIG_CODE, confgrpb.LEGACY_COMPATIBLE, confgrpb.ENABLED_FLAG, confgrpb.ATTRIBUTE_CATEGORY, confgrpb.ATTRIBUTE1, confgrpb.ATTRIBUTE2, confgrpb.ATTRIBUTE3, confgrpb.ATTRIBUTE4, confgrpb.ATTRIBUTE5, confgrpb.ENTERPRISE_ID, confgrpb.MODULE_ID, confgrpb.CREATED_BY, confgrpb.CREATION_DATE, confgrpb.LAST_UPDATED_BY, confgrpb.LAST_UPDATE_DATE, confgrpb.LAST_UPDATE_LOGIN, confgrpb.OBJECT_VERSION_NUMBER, confgrpb.SGUID SGUID FROM HEX_CONFIGURATION_GROUPS_B confgrpb, HEX_CONFIGURATION_GROUPS_TL confgrptl WHERE confgrpb.CONFIGURATION_GROUP_ID = confgrptl.CONFIGURATION_GROUP_ID AND confgrptl.LANGUAGE = USERENV('LANG')
```

---

[← Back to Index](../18_HCM_Extracts_Views_Index.md)
