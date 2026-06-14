# IRC_POOLMEM_LAST_INTERACTION_V

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircpoolmemlastinteractionv-8343.html#ircpoolmemlastinteractionv-8343](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircpoolmemlastinteractionv-8343.html#ircpoolmemlastinteractionv-8343)

## Columns

- INTERACTION_ID
- INTERACTION_DATE
- PERSON_ID
- CONTEXT_ID
- CONTEXT_TYPE_CODE
- INTERACTION_TYPE_CODE

## Query

```sql
SELECT li.interaction_id, li.interaction_date, li.person_id, li.context_id, li.context_type_code, li.interaction_type_code FROM (SELECT i.interaction_id, i.interaction_date, i.person_id, i.context_id, i.context_type_code, i.interaction_type_code, ROW_NUMBER() OVER(PARTITION BY context_id, person_id ORDER BY interaction_date DESC, interaction_id DESC) rn FROM irc_interactions i WHERE i.context_type_code = 'ORA_CAND_POOL') li WHERE li.rn = 1
```

---

[← Back to Index](../22_Recruiting_Views_Index.md)
