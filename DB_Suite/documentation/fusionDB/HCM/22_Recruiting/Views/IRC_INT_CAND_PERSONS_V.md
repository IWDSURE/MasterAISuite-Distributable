# IRC_INT_CAND_PERSONS_V

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircintcandpersonsv-8177.html#ircintcandpersonsv-8177](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircintcandpersonsv-8177.html#ircintcandpersonsv-8177)

## Columns

- PERSON_ID

## Query

```sql
SELECT DISTINCT CANDS.PERSON_ID FROM IRC_CANDIDATES CANDS, PER_PERSON_TYPE_USAGES_M PTUM WHERE CANDS.PERSON_ID = PTUM.PERSON_ID AND TRUNC(SYSDATE) BETWEEN EFFECTIVE_START_DATE AND EFFECTIVE_END_DATE AND EFFECTIVE_LATEST_CHANGE = 'Y' AND (SYSTEM_PERSON_TYPE IN ('EMP') OR (SYSTEM_PERSON_TYPE IN ('CWK') AND NOT EXISTS (SELECT 1 FROM fnd_profile_options profileoptions, fnd_profile_option_values profileoptionvalues WHERE profileoptions.profile_option_name = 'IRC_TREAT_CWK_AS_EXTERNAL' AND profileoptions.profile_option_id = profileoptionvalues.profile_option_id AND profileoptionvalues.LEVEL_VALUE = 'SITE' AND profileoptionvalues.profile_option_value = 'Y')))
```

---

[← Back to Index](../22_Recruiting_Views_Index.md)
