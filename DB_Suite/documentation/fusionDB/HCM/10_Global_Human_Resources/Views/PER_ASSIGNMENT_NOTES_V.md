# PER_ASSIGNMENT_NOTES_V

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perassignmentnotesv-5884.html#perassignmentnotesv-5884](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perassignmentnotesv-5884.html#perassignmentnotesv-5884)

## Columns

- ASSIGNMENT_NOTE_ID
- ASSIGNMENT_ID
- ASG_EFFECTIVE_START_DATE
- ASG_EFFECTIVE_SEQUENCE
- ASG_ACTION_OCCURRENCE_ID
- PERSON_ID
- RECORD_CREATOR
- OBJECT_VERSION_NUMBER
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN
- NOTES

## Query

```sql
SELECT ASSIGNMENT_NOTE_ID, ASSIGNMENT_ID, ASG_EFFECTIVE_START_DATE, ASG_EFFECTIVE_SEQUENCE, ASG_ACTION_OCCURRENCE_ID, PERSON_ID, RECORD_CREATOR, OBJECT_VERSION_NUMBER, CREATED_BY, CREATION_DATE, LAST_UPDATED_BY, LAST_UPDATE_DATE, LAST_UPDATE_LOGIN, NOTES FROM per_assignment_notes
```

---

[← Back to Index](../10_Global_Human_Resources_Views_Index.md)
