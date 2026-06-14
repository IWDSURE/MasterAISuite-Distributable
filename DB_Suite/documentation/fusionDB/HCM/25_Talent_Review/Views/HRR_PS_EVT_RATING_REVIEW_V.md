# HRR_PS_EVT_RATING_REVIEW_V

## Details

**Schema:** FUSION

**Object owner:** HRR

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrrpsevtratingreviewv-7843.html#hrrpsevtratingreviewv-7843](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrrpsevtratingreviewv-7843.html#hrrpsevtratingreviewv-7843)

## Columns

- PERSON_ID
- ASSIGNMENT_ID
- EVENT_YEAR
- EVENT_DAYS
- EVENT_TITLE
- EVENT_DETAILS
- EVENT_DATE
- LINK_TEXT

## Query

```sql
SELECT a.person_id person_id, a.assignment_id assignment_id, to_char(b.data_submit_date, 'yyyy') event_year, 0 event_days, '{"strKey":"HdrSRatingreviewdate"}' event_title, b.meeting_title event_details, b.data_submit_date event_date, '?meetingId=' || b.meeting_id || '&' || 'sort=nameAsc' link_text FROM per_all_assignments_m a, hrr_meetings b, hrr_meeting_participants c WHERE a.person_id = c.participant_person_id AND b.meeting_id = c.meeting_id AND a.assignment_type IN ( 'E', 'C', 'N' ) AND a.primary_flag = 'Y' AND a.effective_latest_change = 'Y' AND trunc(sysdate) BETWEEN a.effective_start_date AND a.effective_end_date AND a.assignment_status_type IN ( 'ACTIVE', 'SUSPENDED' ) AND c.participant_type_code IN ( 'BUSINESS_LEADER', 'REVIEWER', 'DELEGATED_REVIEWER' ) AND b.data_submit_date IS NOT NULL
```

---

[← Back to Index](../25_Talent_Review_Views_Index.md)
