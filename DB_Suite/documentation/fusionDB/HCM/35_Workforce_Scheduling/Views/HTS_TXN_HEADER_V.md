# HTS_TXN_HEADER_V

## Details

**Schema:** FUSION

**Object owner:** HTS

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htstxnheaderv-7673.html#htstxnheaderv-7673](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/htstxnheaderv-7673.html#htstxnheaderv-7673)

## Columns

- TRANSACTION_ID
- FAMILY
- ENTERPRISE_ID
- INITIATOR_USER_ID
- APPLICATION_ID
- MODULE_GROUP
- MODULE_IDENTIFIER
- XML_DATA_CACHE
- PROCESS_ID
- OBJECT
- OBJECT_ID
- SUBJECT
- SUBJECT_ID
- PARENT_TRANSACTION_ID
- REENTRY_FUNCTION
- PROCESS_OWNER
- SECTION_DISPLAY_NAME
- CREATED_BY
- CREATION_DATE
- LAST_UPDATE_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_LOGIN
- OBJECT_VERSION_NUMBER
- IS_TXN_GETTING_ARCHIVED
- SCHED_SHIFT_ID

## Query

```sql
SELECT "TRANSACTION_ID", "FAMILY", "ENTERPRISE_ID", "INITIATOR_USER_ID", "APPLICATION_ID", "MODULE_GROUP", "MODULE_IDENTIFIER", "XML_DATA_CACHE", "PROCESS_ID", "OBJECT", "OBJECT_ID", "SUBJECT", "SUBJECT_ID", "PARENT_TRANSACTION_ID", "REENTRY_FUNCTION", "PROCESS_OWNER", "SECTION_DISPLAY_NAME", "CREATED_BY", "CREATION_DATE", "LAST_UPDATE_DATE", "LAST_UPDATED_BY", "LAST_UPDATE_LOGIN", "OBJECT_VERSION_NUMBER", "IS_TXN_GETTING_ARCHIVED", NVL( (select * from ( SELECT tmp.schedule_shift_id FROM hts_schedule_shifts tmp WHERE tmp.schedule_shift_id = object_id and rownum=1 UNION SELECT tmp1.schedule_shift_id FROM hts_schedule_shifts tmp1 WHERE tmp1.shift_group_id = object_id AND rownum=1 AND tmp1.schedule_shift_id = ( SELECT MIN(schedule_shift_id) FROM hts_schedule_shifts WHERE shift_group_id = tmp1.shift_group_id ) ) where rownum=1), -1 ) SCHED_SHIFT_ID FROM hrc_txn_header where module_identifier IN ( 'DROP_SHIFT', 'OFFER_SHIFT', 'SWAP_SHIFT', 'REQUEST_SHIFT' )
```

---

[← Back to Index](../35_Workforce_Scheduling_Views_Index.md)
