# IRC_CAND_EMAIL_ADDRESS_V

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccandemailaddressv-6230.html#irccandemailaddressv-6230](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccandemailaddressv-6230.html#irccandemailaddressv-6230)

## Columns

- PERSON_ID
- EMAIL_VERIFIED_FLAG
- EMAIL_PREFERRED_FLAG
- CANDIDATE_NUMBER
- EMAIL_ADDRESS_ID
- EMAIL_ADDRESS
- EMAIL_TYPE

## Query

```sql
SELECT cand.person_id, cand.email_verified_flag, cand.email_preferred_flag, cand.candidate_number, cand.email_address_id, email.email_address, email.email_type from (SELECT c.person_id, c.email_verified_flag, c.email_preferred_flag, c.candidate_number, ( CASE WHEN c.cand_email_id IS NOT NULL AND EXISTS (SELECT 1 FROM per_email_addresses e WHERE c.cand_email_id = e.email_address_id) THEN c.cand_email_id WHEN EXISTS ( SELECT 1 FROM per_person_type_usages_m u WHERE ( ( EXISTS ( SELECT 1 FROM fnd_profile_options profileoptions, fnd_profile_option_values profileoptionvalues WHERE profileoptions.profile_option_name = 'IRC_TREAT_CWK_AS_EXTERNAL' AND profileoptions.profile_option_id = profileoptionvalues.profile_option_id AND profileoptionvalues.profile_option_value = 'Y' AND profileoptionvalues.LEVEL_VALUE = 'SITE' ) AND u.system_person_type IN ( 'EMP' ) ) OR ( NOT EXISTS ( SELECT 1 FROM fnd_profile_options profileoptions, fnd_profile_option_values profileoptionvalues WHERE profileoptions.profile_option_name = 'IRC_TREAT_CWK_AS_EXTERNAL' AND profileoptions.profile_option_id = profileoptionvalues.profile_option_id AND profileoptionvalues.profile_option_value = 'Y' AND profileoptionvalues.level_value = 'SITE' ) AND u.system_person_type IN ( 'EMP', 'CWK' ) ) ) AND u.person_id = c.person_id AND trunc(SYSDATE) BETWEEN u.effective_start_date AND u.effective_end_date AND u.effective_latest_change = 'Y' ) THEN ( select email_address_id from ( SELECT emailaddresseo.email_address_id AS email_address_id FROM per_email_addresses emailaddresseo WHERE emailaddresseo.person_id = c.person_id AND emailaddresseo.email_type = 'W1' ORDER BY emailaddresseo.last_update_date DESC ) WHERE ROWNUM = 1 ) ELSE ( select email_address_id from ( SELECT pea.email_address_id AS email_address_id FROM per_email_addresses pea WHERE c.person_id = pea.person_id AND pea.email_type != 'W1' ORDER BY pea.last_update_date DESC ) WHERE ROWNUM = 1 ) END ) AS email_address_id FROM irc_candidates c) cand, per_email_addresses email where email.email_address_id = cand.email_address_id
```

---

[← Back to Index](../22_Recruiting_Views_Index.md)
