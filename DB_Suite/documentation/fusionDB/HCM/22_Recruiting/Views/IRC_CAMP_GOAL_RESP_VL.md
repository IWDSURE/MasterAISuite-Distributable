# IRC_CAMP_GOAL_RESP_VL

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampgoalrespvl-6354.html#irccampgoalrespvl-6354](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampgoalrespvl-6354.html#irccampgoalrespvl-6354)

## Columns

- GOAL_RESPONSE_ID
- GOAL_ID
- RESPONSE_LABEL
- DESTINATION_URL
- USE_DEFAULT_URL_FLAG
- INCLUDE_IN_TARGET_FLAG
- OBJECT_VERSION_NUMBER
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN

## Query

```sql
SELECT B.GOAL_RESPONSE_ID, B.GOAL_ID, TL.RESPONSE_LABEL, B.DESTINATION_URL, B.USE_DEFAULT_URL_FLAG, B.INCLUDE_IN_TARGET_FLAG, B.OBJECT_VERSION_NUMBER, B.CREATED_BY, B.CREATION_DATE, B.LAST_UPDATED_BY, B.LAST_UPDATE_DATE, B.LAST_UPDATE_LOGIN FROM IRC_CAMP_GOAL_RESP_B B, IRC_CAMP_GOAL_RESP_TL TL WHERE B.GOAL_RESPONSE_ID = TL.GOAL_RESPONSE_ID AND TL.LANGUAGE = USERENV('LANG')
```

---

[← Back to Index](../22_Recruiting_Views_Index.md)
