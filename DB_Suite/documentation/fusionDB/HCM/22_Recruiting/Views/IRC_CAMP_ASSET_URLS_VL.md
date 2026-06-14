# IRC_CAMP_ASSET_URLS_VL

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampasseturlsvl-7125.html#irccampasseturlsvl-7125](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampasseturlsvl-7125.html#irccampasseturlsvl-7125)

## Columns

- ASSET_URL_ID
- DEEP_LINK_ID
- ASSET_ID
- URL
- GOAL_ID
- GOAL_RESPONSE_ID
- REQUISITION_ID
- OBJECT_VERSION_NUMBER
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN

## Query

```sql
SELECT B.ASSET_URL_ID, B.DEEP_LINK_ID, B.ASSET_ID, TL.URL, B.GOAL_ID, B.GOAL_RESPONSE_ID, B.REQUISITION_ID, B.OBJECT_VERSION_NUMBER, B.CREATED_BY, B.CREATION_DATE, B.LAST_UPDATED_BY, B.LAST_UPDATE_DATE, B.LAST_UPDATE_LOGIN FROM IRC_CAMP_ASSET_URLS_B B, IRC_CAMP_ASSET_URLS_TL TL WHERE B.ASSET_URL_ID = TL.ASSET_URL_ID AND TL.LANGUAGE = USERENV('LANG')
```

---

[← Back to Index](../22_Recruiting_Views_Index.md)
