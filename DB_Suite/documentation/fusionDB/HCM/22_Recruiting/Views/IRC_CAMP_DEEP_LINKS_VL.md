# IRC_CAMP_DEEP_LINKS_VL

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampdeeplinksvl-5393.html#irccampdeeplinksvl-5393](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampdeeplinksvl-5393.html#irccampdeeplinksvl-5393)

## Columns

- DEEP_LINK_ID
- OBJECT_TYPE
- ACTION
- STATUS_CODE
- DISPLAY_NAME
- OBJECT_VERSION_NUMBER
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN

## Query

```sql
SELECT B.DEEP_LINK_ID, B.OBJECT_TYPE, B.ACTION, B.STATUS_CODE, TL.DISPLAY_NAME, B.OBJECT_VERSION_NUMBER, B.CREATED_BY, B.CREATION_DATE, B.LAST_UPDATED_BY, B.LAST_UPDATE_DATE, B.LAST_UPDATE_LOGIN FROM IRC_CAMP_DEEP_LINKS_B B, IRC_CAMP_DEEP_LINKS_TL TL WHERE B.DEEP_LINK_ID = TL.DEEP_LINK_ID AND TL.LANGUAGE = USERENV('LANG')
```

---

[← Back to Index](../22_Recruiting_Views_Index.md)
