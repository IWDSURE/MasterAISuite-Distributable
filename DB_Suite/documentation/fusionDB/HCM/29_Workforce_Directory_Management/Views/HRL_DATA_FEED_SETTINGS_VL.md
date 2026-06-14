# HRL_DATA_FEED_SETTINGS_VL

## Details

**Schema:** FUSION

**Object owner:** HRL

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrldatafeedsettingsvl-7032.html#hrldatafeedsettingsvl-7032](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrldatafeedsettingsvl-7032.html#hrldatafeedsettingsvl-7032)

## Columns

- ROW_ID
- SETTING_ID
- ENTERPRISE_ID
- FLOW_CODE
- SECTION_CODE
- CATEGORY_CODE
- SOURCE_CODE
- SOURCE_NAME
- SOURCE_DESCRIPTION
- DATA_SOURCE_TYPE
- DATA_SOURCE_VALUE
- DATA_PRIV_NAME
- DATA_PRIV_OBJ
- ACTIVE_FLAG
- VISIBILITY_CODE
- DISPLAY_SEQUENCE
- COLOR_CODE
- IMAGE_NAME
- LINK_TYPE
- LINK_TEXT
- OBJECT_VERSION_NUMBER
- CREATED_BY
- CREATION_DATE
- LAST_UPDATE_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_LOGIN
- MODULE_ID
- SEED_DATA_SOURCE
- ORA_SEED_SET1
- ORA_SEED_SET2

## Query

```sql
SELECT B.ROWID ROW_ID , B.setting_id , B.enterprise_id , B.flow_code , B.section_code , B.category_code , B.source_code , T.source_name , T.source_description , B.data_source_type , B.data_source_value , B.data_priv_name , B.data_priv_obj , B.active_flag , B.visibility_code , B.display_sequence , B.color_code , B.image_name , B.link_type , B.link_text , B.object_version_number , B.created_by , B.creation_date , B.last_update_date , B.last_updated_by , B.last_update_login , B.module_id , B.seed_data_source , B.ora_seed_set1 , B.ora_seed_set2 FROM hrl_data_feed_settings_b B, hrl_data_feed_settings_tl T WHERE B.setting_id = T.setting_id and T.language = USERENV('LANG')
```

---

[← Back to Index](../29_Workforce_Directory_Management_Views_Index.md)
