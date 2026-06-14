# ANC_PS_EVT_ABSENCES_V

## Details

**Schema:** FUSION

**Object owner:** ANC

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancpsevtabsencesv-8540.html#ancpsevtabsencesv-8540](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ancpsevtabsencesv-8540.html#ancpsevtabsencesv-8540)

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
SELECT abs.person_id person_id, NULL assignment_id, EXTRACT(YEAR FROM abs.start_date) event_year, abs.start_date event_date, ( trunc(abs.end_datetime) - trunc(abs.start_datetime) ) + 1 event_days, typ.name event_title, anc_common_utils.get_formatted_number(abs.duration) || ' ' || lok.meaning event_details, '?pPersonId=' || abs.person_id || '&pDisplayName=' || pnf.display_name link_text FROM anc_per_abs_entries abs, anc_absence_types_f_tl typ, hcm_lookups lok, per_person_names_f_v pnf WHERE typ.absence_type_id = abs.absence_type_id AND trunc(sysdate) BETWEEN typ.effective_start_date AND typ.effective_end_date AND lok.lookup_code = abs.uom AND lok.lookup_type = 'ANC_DURATION_UOM' AND abs.absence_entry_basic_flag = 'Y' AND abs.start_date BETWEEN add_months(sysdate, - 12) AND add_months(sysdate, 6) AND typ.language = sys_context('USERENV', 'LANG') AND abs.person_id = pnf.person_id and not( (absence_status_cd ='ORA_WITHDRAWN' and APPROVAL_STATUS_CD = 'APPROVED') or (absence_status_cd ='SUBMITTED' and APPROVAL_STATUS_CD = 'DENIED')) AND trunc(sysdate) BETWEEN pnf.effective_start_date AND pnf.effective_end_date UNION SELECT abs.person_id person_id, NULL assignment_id, EXTRACT(YEAR FROM abs.start_date) event_year, abs_dtl.absence_date event_date, 1 event_days, typ.name event_title, anc_common_utils.get_formatted_number(abs_dtl.duration) || ' ' || lok.meaning event_details, '?pPersonId=' || abs.person_id || '&pDisplayName=' || pnf.display_name link_text FROM anc_per_abs_entry_dtls abs_dtl, anc_per_abs_entries abs, anc_absence_types_f_tl typ, hcm_lookups lok, per_person_names_f_v pnf WHERE typ.absence_type_id = abs.absence_type_id AND trunc(sysdate) BETWEEN typ.effective_start_date AND typ.effective_end_date AND lok.lookup_code = abs.uom AND lok.lookup_type = 'ANC_DURATION_UOM' AND abs.per_absence_entry_id = abs_dtl.per_absence_entry_id AND abs.absence_entry_basic_flag <> 'Y' AND abs.start_date BETWEEN add_months(sysdate, - 12) AND add_months(sysdate, 6) AND typ.language = sys_context('USERENV', 'LANG') AND abs.person_id = pnf.person_id and not( (absence_status_cd ='ORA_WITHDRAWN' and APPROVAL_STATUS_CD = 'APPROVED') or (absence_status_cd ='SUBMITTED' and APPROVAL_STATUS_CD = 'DENIED')) AND trunc(sysdate) BETWEEN pnf.effective_start_date AND pnf.effective_end_date
```

---

[← Back to Index](../3_Absence_Management_Views_Index.md)
