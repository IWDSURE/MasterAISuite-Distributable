# PER_SEC_CON_V

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/persecconv-8317.html#persecconv-8317](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/persecconv-8317.html#persecconv-8317)

## Columns

- PERSON_ID
- CONTACT_ID

## Query

```sql
SELECT c.person_id, c.contact_person_id as contact_id FROM per_contact_relships_f c WHERE c.effective_start_date = (SELECT MIN(effective_start_date) FROM per_contact_relships_f c1 where c1.contact_relationship_id=c.contact_relationship_id) and not exists (SELECT 1 FROM PER_PERIODS_OF_SERVICE PS WHERE PS.PERSON_ID=c.CONTACT_PERSON_ID)
```

---

[← Back to Index](../10_Global_Human_Resources_Views_Index.md)
