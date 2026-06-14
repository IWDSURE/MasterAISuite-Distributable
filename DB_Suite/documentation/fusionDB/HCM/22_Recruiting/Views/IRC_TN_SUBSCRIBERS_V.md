# IRC_TN_SUBSCRIBERS_V

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irctnsubscribersv-3929.html#irctnsubscribersv-3929](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irctnsubscribersv-3929.html#irctnsubscribersv-3929)

## Columns

- SUBSCRIBER_ID
- STATUS_CODE
- CODE
- NAME
- FA_POD_CODE
- FA_POD_URL
- FA_INTEG_USERNAME
- TN_INTEG_USERNAME
- TN_INTEG_USERGUID
- LOGO_URL
- SUBSCRIBER_GUID
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE

## Query

```sql
SELECT S.SUBSCRIBER_ID SUBSCRIBER_ID, S.STATUS_CODE , S.CODE, S.NAME, (select ss.value from irc_tn_subscriber_settings ss where ss.subscriber_id = s.subscriber_id and ss.key = 'FA_POD_CODE') FA_POD_CODE, (select ss.value from irc_tn_subscriber_settings ss where ss.subscriber_id = s.subscriber_id and ss.key = 'FA_POD_URL') FA_POD_URL, (select ss.value from irc_tn_subscriber_settings ss where ss.subscriber_id = s.subscriber_id and ss.key = 'FA_INTEG_USERNAME') FA_INTEG_USERNAME, (select ss.value from irc_tn_subscriber_settings ss where ss.subscriber_id = s.subscriber_id and ss.key = 'TN_INTEG_USERNAME') TN_INTEG_USERNAME, (select ss.value from irc_tn_subscriber_settings ss where ss.subscriber_id = s.subscriber_id and ss.key = 'TN_INTEG_USER_GUID') TN_INTEG_USERGUID, S.LOGO_URL , S.SUBSCRIBER_GUID, S.CREATED_BY, S.CREATION_DATE, S.LAST_UPDATED_BY, S.LAST_UPDATE_DATE FROM irc_tn_subscribers S
```

---

[← Back to Index](../22_Recruiting_Views_Index.md)
