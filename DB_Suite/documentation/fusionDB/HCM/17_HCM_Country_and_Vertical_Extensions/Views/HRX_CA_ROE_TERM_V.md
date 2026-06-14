# HRX_CA_ROE_TERM_V

## Details

**Schema:** FUSION

**Object owner:** HRX

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrxcaroetermv-5253.html#hrxcaroetermv-5253](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrxcaroetermv-5253.html#hrxcaroetermv-5253)

## Columns

- ACTION_ID
- ACTION_NAME
- ACTION_REASON

## Query

```sql
SELECT pa.action_id, pa.action_name, '' action_reason FROM per_actions_vl pa WHERE pa.action_type_code in ('EMPL_TERMINATE','EMPL_GLB_TRANSFER') AND trunc(sysdate) between pa.start_date and pa.end_date UNION SELECT to_number(concat(pav.action_id,parv.action_reason_id) ) action_id, concat(pav.action_name,': '|| parv.action_reason) action_name, parv.action_reason FROM per_actions_vl pav, per_action_reasons_vl parv, per_action_reason_usages paru WHERE pav.action_type_code in ('EMPL_TERMINATE','EMPL_GLB_TRANSFER') AND paru.action_id = pav.action_id AND parv.action_reason_id = paru.action_reason_id AND trunc(sysdate) between pav.start_date and pav.end_date AND trunc(sysdate) between parv.start_date and parv.end_date AND trunc(sysdate) between paru.start_date and paru.end_date ORDER BY action_name, action_reason DESC
```

---

[← Back to Index](../17_HCM_Country_and_Vertical_Extensions_Views_Index.md)
