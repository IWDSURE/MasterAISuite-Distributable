# PAY_PS_ANA_YEAR_END_DOC_V

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paypsanayearenddocv-4890.html#paypsanayearenddocv-4890](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paypsanayearenddocv-4890.html#paypsanayearenddocv-4890)

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
SELECT yed.person_id person_id, NULL assignment_id, '{"strKey":"FdHIYearenddocuments"}' text_title, yed.document_name text_metric, yed.tax_reporting_unit text_meta, decode(sign((sysdate -cast(yed.creation_date as date)) - 7), - 1, '{"strKey":"BdgNew3"}', NULL) badge_text, decode(sign((sysdate -cast(yed.creation_date as date)) - 7), - 1, 'info', NULL) badge_status, NULL period_chn_ind_val, NULL period_chn_ind_cmp, NULL chart_type, NULL chart_color, NULL chart_data, '' link_text FROM pay_year_end_docs_vl yed WHERE system_document_type != 'GLB_THIRD_PARTY_PAYROLL_DOCUMENTS' AND trunc(sysdate) - publish_date BETWEEN 0 AND 30 AND creation_date = (select max(creation_date) from pay_year_end_docs_vl where person_id = yed.person_id and system_document_type = yed.system_document_type AND trunc(sysdate) - publish_date BETWEEN 0 AND 30)
```

---

[← Back to Index](../11_Global_Payroll_Views_Index.md)
