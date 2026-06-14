# IRC_JA_INTERACT_RCPT_V

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircjainteractrcptv-6955.html#ircjainteractrcptv-6955](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircjainteractrcptv-6955.html#ircjainteractrcptv-6955)

## Columns

- INTERACTION_ID
- WITH_HIRING_TEAM
- WITH_AGENT

## Query

```sql
SELECT a.interaction_id , (case when (count(case when b.interaction_id is not null and a.hiring_team_intr_flag = 'Y' and b.agent_id is null then b.interaction_recipient_id else null end ) ) > 0 then 'Y' ELSE 'N' END) with_hiring_team, (case when (count(case when b.interaction_id is not null and b.agent_id is not null then b.interaction_recipient_id else null end ) ) > 0 then 'Y' ELSE 'N' END) with_agent FROM irc_interactions a, irc_interact_recipients b where a.interaction_id = b.interaction_id (+) and a.context_type_code = 'ORA_SUBMISSION' group by a.interaction_id
```

---

[← Back to Index](../22_Recruiting_Views_Index.md)
