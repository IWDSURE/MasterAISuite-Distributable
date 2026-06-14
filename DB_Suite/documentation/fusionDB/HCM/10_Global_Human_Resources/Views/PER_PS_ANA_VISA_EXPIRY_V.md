# PER_PS_ANA_VISA_EXPIRY_V

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perpsanavisaexpiryv-6517.html#perpsanavisaexpiryv-6517](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perpsanavisaexpiryv-6517.html#perpsanavisaexpiryv-6517)

## Columns

- PERSON_ID
- ASSIGNMENT_ID
- TEXT_TITLE
- TEXT_METRIC
- TEXT_META
- BADGE_TEXT
- BADGE_STATUS
- PERIOD_CHN_IND_VAL
- PERIOD_CHN_IND_CMP
- CHART_TYPE
- CHART_COLOR
- CHART_DATA
- LINK_TEXT

## Query

```sql
SELECT v.person_id, NULL assignment_id, '{"strKey":"HdrSVisaCOUNTRY", "tokens":{"COUNTRY":"' || t.territory_short_name || '"}}' text_title, ( CASE WHEN v.expiration_date < trunc(sysdate) THEN decode(sign((trunc(sysdate) - v.expiration_date) - 14), - 1, '{"strKey":"PgHIExpiredonDATE", "tokens":{"DATE":"' || hrl_df_util.date_to_char(v.expiration_date) || '"}}') ELSE decode(trunc(v.expiration_date - trunc(sysdate)), 0, '{"strKey":"PgHIExpiringtoday"}', 1, '{"strKey":"PgHIExpiringtomorrow"}', '{"strKey":"PgHIExpiringinDAYSNUMdays", "tokens":{"DAYS_NUM":"' ||(trunc(v.expiration_date - trunc(sysdate))) || '"}}') END ) text_metric, v.visa_permit_number text_meta, ( CASE WHEN v.expiration_date < trunc(sysdate) THEN decode(sign((trunc(sysdate) - v.expiration_date) - 14), - 1, '{"strKey":"BdgExpired1"}') ELSE decode(sign((v.expiration_date - trunc(sysdate)) - 30), - 1, '{"strKey":"BdgExpiring"}') END ) badge_text, ( CASE WHEN v.expiration_date < trunc(sysdate) THEN decode(sign((trunc(sysdate) - v.expiration_date) - 14), - 1, 'danger') ELSE decode(sign((v.expiration_date - trunc(sysdate)) - 30), - 1, 'warning') END ) badge_status, NULL period_chn_ind_val, NULL period_chn_ind_cmp, NULL chart_type, NULL chart_color, NULL chart_data, '' link_text FROM per_visas_permits_f v, fnd_territories_vl t WHERE t.territory_code = v.legislation_code AND v.expiration_date IS NOT NULL AND ( v.visa_permit_id, v.expiration_date ) = ( SELECT v2.visa_permit_id, MAX(v2.expiration_date) greatest_expiration_date FROM per_visas_permits_f v2 WHERE v2.person_id = v.person_id AND v2.visa_permit_id = v.visa_permit_id AND v2.effective_start_date <= trunc(sysdate) and v2.effective_end_date >= trunc(sysdate) AND v2.expiration_date IS NOT NULL GROUP BY v2.visa_permit_id ) AND ( ( v.expiration_date < trunc(sysdate) AND ( sign((trunc(sysdate) - v.expiration_date) - 14) = - 1 ) ) OR ( v.expiration_date >= trunc(sysdate) AND ( sign((v.expiration_date - trunc(sysdate)) - 30) = - 1 ) ) )
```

---

[← Back to Index](../10_Global_Human_Resources_Views_Index.md)
