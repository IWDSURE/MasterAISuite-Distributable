# IRC_MP_SEEKER_ALERT_PREF_V

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircmpseekeralertprefv-8699.html#ircmpseekeralertprefv-8699](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircmpseekeralertprefv-8699.html#ircmpseekeralertprefv-8699)

## Columns

- PERSON_ID
- CONTEXT_ID
- JOBS_PROFILE_OPTION_VALUE

## Query

```sql
SELECT person_id, context_id, jobs_profile_option_value FROM ( SELECT sp.person_id AS person_id, sp.context_id AS context_id, 'N' AS jobs_profile_option_value FROM irc_mp_optyseeker_preferences sp WHERE sp.context_type = 'ORA_NOTIFY_NEW_OPPS' AND EXISTS ( SELECT 1 FROM fnd_profile_option_values ov, fnd_profile_options_b o WHERE o.profile_option_id = ov.profile_option_id AND o.profile_option_name = 'ORA_HCM_OPP_MARKET_PLACE_JOBS' AND ov.profile_option_value = 'N' ) UNION ALL SELECT cp.person_id AS person_id, decode(cp.opt_in_tc_emails_flag, 'Y', 1, 'N', 0) AS context_id, 'Y' AS jobs_profile_option_value FROM irc_cand_preferences cp WHERE cp.site_number = 'ICE' AND cp.person_id IN ( SELECT person_id FROM irc_mp_seeker_v ) AND EXISTS ( SELECT 1 FROM fnd_profile_option_values ov, fnd_profile_options_b o WHERE o.profile_option_id = ov.profile_option_id AND o.profile_option_name = 'ORA_HCM_OPP_MARKET_PLACE_JOBS' AND ov.profile_option_value = 'Y' ) )
```

---

[← Back to Index](../22_Recruiting_Views_Index.md)
