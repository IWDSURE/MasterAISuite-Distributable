# PAY_PS_EVT_YEAR_END_DOC_V

## Details

**Schema:** FUSION

**Object owner:** PAY

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paypsevtyearenddocv-3385.html](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/paypsevtyearenddocv-3385.html)

## Columns

- PERSON_ID
- ASSIGNMENT_ID
- EVENT_YEAR
- EVENT_DATE
- EVENT_DAYS
- EVENT_TITLE
- EVENT_DETAILS
- LINK_TEXT

## Query

```sql
SELECT yed.person_id person_id, NULL assignment_id, to_char(yed.publish_date, 'YYYY') event_year, yed.publish_date event_date, 0 event_days, '{"strKey":"FdHIYearenddocuments"}' event_title, yed.document_name event_details, '' link_text FROM ( SELECT hdr.documents_of_record_id documents_of_record_id, hdr.person_id person_id, to_char(hdr.dei_information_number1) period_name, hdr.document_name document_name, hdt.system_document_type system_document_type, hdr.date_from, hdr.date_to, hdr.creation_date, to_date(nvl(hdr.publish_date, hdr.creation_date)) AS publish_date, hdr.related_object_id rel_action_id, 'HR_DOCUMENTS_OF_RECORD' attachment_entity_name FROM hr_document_types_vl hdt, hr_documents_of_record hdr WHERE hdt.category_code IN ( 'PAYROLL', 'BENEF' ) AND hdt.sub_category_code IN ( 'PAYROLL_TAX', 'BENEF_ENRL_CHNG_TERMIN' ) AND hdt.system_document_type IN ( SELECT * FROM TABLE ( CAST(pay_statistics_utility_pkg.in_varchar_list(pay_core_utils.get_legislation_rule(hdt.legislation_code, '#YEAR_END_TAX_FORM')) AS pay_number_varchar_t) ) ) AND hdr.document_type_id = hdt.document_type_id AND ( hdr.dei_information_category IS NULL OR hdr.dei_information_category = hdt.system_document_type ) UNION SELECT hdr.documents_of_record_id documents_of_record_id, hdr.person_id person_id, NULL period_name, hdr.document_name document_name, hdt.system_document_type system_document_type, hdr.date_from, hdr.date_to, hdr.creation_date, nvl(hpiri.iri_information_date1, hdr.issued_date) AS publish_date, hdr.related_object_id rel_action_id, 'HR_DOCUMENTS_OF_RECORD' attachment_entity_name FROM hr_document_types_vl hdt, hr_documents_of_record hdr, hry_pi_inbd_records hpir, hry_pi_inbd_record_information hpiri, pay_pay_relationships_dn pprd, per_legislative_data_groups ldg WHERE hdt.system_document_type = 'GLB_THIRD_PARTY_PAYROLL_DOCUMENTS' AND hdt.category_code = 'PAYROLL' AND hdr.document_type_id = hdt.document_type_id AND ldg.legislative_data_group_id (+) = pprd.legislative_data_group_id AND hpir.inbd_record_id = hpiri.inbd_record_id AND hpir.documents_of_record_id = hdr.documents_of_record_id AND hpir.record_type = 'ORA_HRY_INBD_PAYROLL_DOC' AND nvl(hpiri.iri_information_context, 'ORA_HRY_INBD_PAYROLL_DOC') = 'ORA_HRY_INBD_PAYROLL_DOC' AND pprd.payroll_relationship_id (+) = hpir.payroll_relationship_id AND pprd.person_id (+) = hpir.person_id ) yed WHERE system_document_type != 'GLB_THIRD_PARTY_PAYROLL_DOCUMENTS' AND yed.publish_date <= trunc(sysdate)
```

---

[← Back to HRMS Views Index](../HRMS_Views_Index.md)
