# IRC_REG_RESPONSE_ETHNICITY_V

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircregresponseethnicityv-8384.html#ircregresponseethnicityv-8384](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircregresponseethnicityv-8384.html#ircregresponseethnicityv-8384)

## Columns

- RESPONSE_ID
- SUBMISSION_ID
- PERSON_ID
- ETHNICITY_CODE
- ROWLEVEL

## Query

```sql
select r.response_id, r.submission_id, r.person_id, trim(regexp_substr(attribute_2,'[^,]+', 1, level) ) ethnicity_code, 1 as rowlevel from irc_regulatory_responses r connect by regexp_substr(attribute_2, '[^,]+', 1, level) is not null and PRIOR response_id = response_id and PRIOR SYS_GUID() is not null
```

---

[← Back to Index](../22_Recruiting_Views_Index.md)
