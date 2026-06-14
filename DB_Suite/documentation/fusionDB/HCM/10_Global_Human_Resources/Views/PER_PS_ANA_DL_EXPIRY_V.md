# PER_PS_ANA_DL_EXPIRY_V

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perpsanadlexpiryv-4035.html#perpsanadlexpiryv-4035](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perpsanadlexpiryv-4035.html#perpsanadlexpiryv-4035)

## Columns

- PERSON_ID
- ASSIGNMENT_ID
- TEXT_TITLE
- TEXT_METRIC
- TEXT_META
- BADGE_STATUS
- BADGE_TEXT
- PERIOD_CHN_IND_VAL
- PERIOD_CHN_IND_CMP
- CHART_TYPE
- CHART_COLOR
- CHART_DATA
- LINK_TEXT

## Query

```sql
SELECT d.person_id, NULL assignment_id, '{"strKey":"HdrSDriverslicenseCOUNTRY", "tokens":{"COUNTRY":"' || t.territory_short_name || '"}}' text_title, ( CASE WHEN d.date_to < trunc(sysdate) THEN decode(sign((trunc(sysdate) - d.date_to) - 14), - 1, '{"strKey":"PgHIExpiredonDATE", "tokens":{"DATE":"' || hrl_df_util.date_to_char(d.date_to) || '"}}') ELSE decode(trunc(d.date_to - trunc(sysdate)), 0, '{"strKey":"PgHIExpiringtoday"}', 1, '{"strKey":"PgHIExpiringtomorrow"}', '{"strKey":"PgHIExpiringinDAYSNUMdays", "tokens":{"DAYS_NUM":"' ||(trunc(d.date_to - trunc(sysdate))) || '"}}') END ) text_metric, d.license_number text_meta, ( CASE WHEN d.date_to < trunc(sysdate) THEN decode(sign((trunc(sysdate) - d.date_to) - 14), - 1, 'danger') ELSE decode(sign((d.date_to - trunc(sysdate)) - 30), - 1, 'warning') END ) badge_status, ( CASE WHEN d.date_to < trunc(sysdate) THEN decode(sign((trunc(sysdate) - d.date_to) - 14), - 1, '{"strKey":"BdgExpired1"}') ELSE decode(sign((d.date_to - trunc(sysdate)) - 30), - 1, '{"strKey":"BdgExpiring"}') END ) badge_text, NULL period_chn_ind_val, NULL period_chn_ind_cmp, NULL chart_type, NULL chart_color, NULL chart_data, '' link_text FROM per_drivers_licenses d, fnd_territories_vl t WHERE t.territory_code = d.legislation_code AND d.date_to IS NOT NULL AND ( ( d.date_to < trunc(sysdate) AND ( sign((trunc(sysdate) - d.date_to) - 14) = - 1 ) ) OR ( d.date_to >= trunc(sysdate) AND ( sign((d.date_to - trunc(sysdate)) - 30) = - 1 ) ) )
```

---

[← Back to Index](../10_Global_Human_Resources_Views_Index.md)
