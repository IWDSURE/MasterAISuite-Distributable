# IRC_CAND_PREFERRED_PHONE_V

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccandpreferredphonev-8860.html#irccandpreferredphonev-8860](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccandpreferredphonev-8860.html#irccandpreferredphonev-8860)

## Columns

- PERSON_ID
- PHONE_VERIFIED_FLAG
- PHONE_PREFERRED_FLAG
- PHONE_CHANNEL_TYPE
- CANDIDATE_NUMBER
- PHONE_ID
- COUNTRY_CODE_NUMBER
- AREA_CODE
- PHONE_NUMBER
- SEARCH_PHONE_NUMBER
- EXTENSION
- DISPLAY_PHONE_NUMBER
- PHONE_TYPE

## Query

```sql
SELECT cand.person_id, cand.phone_verified_flag, cand.phone_preferred_flag, cand.phone_channel_type, cand.candidate_number, cand.phone_id, phone.country_code_number, phone.area_code, phone.phone_number, phone.search_phone_number, phone.extension, phone.display_phone_number, phone.phone_type from (SELECT c.person_id, c.phone_verified_flag, c.phone_preferred_flag, c.phone_channel_type, c.candidate_number, ( CASE WHEN c.cand_phone_id IS NOT NULL AND EXISTS (SELECT 1 FROM per_phones p WHERE c.cand_phone_id = p.phone_id) THEN c.cand_phone_id WHEN EXISTS ( SELECT 1 FROM per_person_type_usages_m u WHERE ( ( EXISTS ( SELECT 1 FROM fnd_profile_options profileoptions, fnd_profile_option_values profileoptionvalues WHERE profileoptions.profile_option_name = 'IRC_TREAT_CWK_AS_EXTERNAL' AND profileoptions.profile_option_id = profileoptionvalues.profile_option_id AND profileoptionvalues.profile_option_value = 'Y' AND profileoptionvalues.LEVEL_VALUE = 'SITE' ) AND u.system_person_type IN ( 'EMP' ) ) OR ( NOT EXISTS ( SELECT 1 FROM fnd_profile_options profileoptions, fnd_profile_option_values profileoptionvalues WHERE profileoptions.profile_option_name = 'IRC_TREAT_CWK_AS_EXTERNAL' AND profileoptions.profile_option_id = profileoptionvalues.profile_option_id AND profileoptionvalues.profile_option_value = 'Y' AND profileoptionvalues.level_value = 'SITE' ) AND u.system_person_type IN ( 'EMP', 'CWK' ) ) ) AND u.person_id = c.person_id AND trunc(SYSDATE) BETWEEN u.effective_start_date AND u.effective_end_date AND u.effective_latest_change = 'Y' ) THEN ( SELECT PHONE_ID FROM (SELECT PP.phone_id AS PHONE_ID FROM PER_PHONES PP WHERE c.PERSON_ID = PP.person_id AND PP.PHONE_TYPE = 'W1' ORDER BY PP.LAST_UPDATE_DATE DESC) WHERE ROWNUM = 1 ) ELSE ( SELECT PHONE_ID FROM (SELECT PP.phone_id AS PHONE_ID FROM PER_PHONES PP WHERE c.PERSON_ID = PP.person_id AND PP.PHONE_TYPE = 'HM' ORDER BY PP.LAST_UPDATE_DATE DESC) WHERE ROWNUM = 1 ) END ) AS phone_id FROM irc_candidates c) cand, per_display_phones_v phone where phone.phone_id = cand.phone_id
```

---

[← Back to Index](../22_Recruiting_Views_Index.md)
