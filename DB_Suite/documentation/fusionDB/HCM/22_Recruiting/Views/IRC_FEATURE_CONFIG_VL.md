# IRC_FEATURE_CONFIG_VL

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircfeatureconfigvl-3910.html#ircfeatureconfigvl-3910](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircfeatureconfigvl-3910.html#ircfeatureconfigvl-3910)

## Columns

- FEATURE_CONFIG_ID
- FEATURE_NAME
- FUNCTIONAL_AREA
- SETTING_NAME
- FEATURE_CODE
- PROFILE_OPTION_CODE
- SETTING_CODE
- FEATURE_RELEASE
- MODULE_ID
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN
- OBJECT_VERSION_NUMBER
- SQL_TEXT

## Query

```sql
SELECT irc_feature_config_b.FEATURE_CONFIG_ID FEATURE_CONFIG_ID, irc_feature_config_tl.FEATURE_NAME FEATURE_NAME, irc_feature_config_tl.FUNCTIONAL_AREA FUNCTIONAL_AREA, irc_feature_config_tl.SETTING_NAME SETTING_NAME, irc_feature_config_b.FEATURE_CODE FEATURE_CODE, irc_feature_config_b.PROFILE_OPTION_CODE PROFILE_OPTION_CODE, irc_feature_config_b.SETTING_CODE SETTING_CODE, irc_feature_config_b.FEATURE_RELEASE FEATURE_RELEASE, irc_feature_config_b.MODULE_ID MODULE_ID, irc_feature_config_b.CREATED_BY CREATED_BY, irc_feature_config_b.CREATION_DATE CREATION_DATE, irc_feature_config_b.LAST_UPDATED_BY LAST_UPDATED_BY, irc_feature_config_b.LAST_UPDATE_DATE LAST_UPDATE_DATE, irc_feature_config_b.LAST_UPDATE_LOGIN LAST_UPDATE_LOGIN, irc_feature_config_b.OBJECT_VERSION_NUMBER OBJECT_VERSION_NUMBER, irc_feature_config_b.SQL_TEXT SQL_TEXT FROM irc_feature_config_b, irc_feature_config_tl WHERE irc_feature_config_b.FEATURE_CONFIG_ID = irc_feature_config_tl.FEATURE_CONFIG_ID AND irc_feature_config_tl.LANGUAGE = USERENV('LANG')
```

---

[← Back to Index](../22_Recruiting_Views_Index.md)
