# HWM_TM_REP_S_SEC_ATRBS_V

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmrepssecatrbsv-7349.html#hwmtmrepssecatrbsv-7349](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtmrepssecatrbsv-7349.html#hwmtmrepssecatrbsv-7349)

## Columns

- SEC_TIME_REPOS_ATRB_ID
- SEC_ATTRIBUTE_CATEGORY
- SECURITY_ENTERPRISE_ID
- SECURITY_BUSINESS_UNIT
- SECURITY_LEG_DATA_GROUP
- SECURITY_ORGANIZATION_ID
- USAGES_SOURCE_ID
- USAGES_SOURCE_VERSION

## Query

```sql
SELECT SecurityAtrbs.tm_rep_atrb_id Sec_Time_Repos_Atrb_id, SecurityAtrbs.attribute_category Sec_Attribute_Category, SecurityAtrbs.attribute_number1 Security_Enterprise_Id, SecurityAtrbs.attribute_number2 Security_Business_Unit, SecurityAtrbs.attribute_number3 Security_Leg_Data_Group, SecurityAtrbs.attribute_number4 Security_Organization_Id, SecAtrbUsg.usages_source_id, SecAtrbUsg.usages_source_version FROM hwm_tm_rep_atrbs SecurityAtrbs, hwm_tm_rep_atrb_usages SecAtrbUsg WHERE SecurityAtrbs.tm_rep_atrb_id = SecAtrbUsg.tm_rep_atrb_id and SecurityAtrbs.attribute_category = 'Security Attributes'
```

---

[← Back to Index](../31_Workforce_Management_Views_Index.md)
