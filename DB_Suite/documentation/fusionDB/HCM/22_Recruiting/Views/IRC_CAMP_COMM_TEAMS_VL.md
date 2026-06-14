# IRC_CAMP_COMM_TEAMS_VL

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampcommteamsvl-7387.html#irccampcommteamsvl-7387](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/irccampcommteamsvl-7387.html#irccampcommteamsvl-7387)

## Columns

- TEAM_ID
- STATUS_CODE
- DOWNLOAD_FLAG
- TEAM_NAME
- TEAM_DESCRIPTION
- OBJECT_VERSION_NUMBER
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN

## Query

```sql
SELECT B.TEAM_ID, B.STATUS_CODE, B.DOWNLOAD_FLAG, TL.TEAM_NAME, TL.TEAM_DESCRIPTION, B.OBJECT_VERSION_NUMBER, B.CREATED_BY, B.CREATION_DATE, B.LAST_UPDATED_BY, B.LAST_UPDATE_DATE, B.LAST_UPDATE_LOGIN FROM IRC_CAMP_COMM_TEAMS_B B, IRC_CAMP_COMM_TEAMS_TL TL WHERE B.TEAM_ID = TL.TEAM_ID AND TL.LANGUAGE = USERENV('LANG')
```

---

[← Back to Index](../22_Recruiting_Views_Index.md)
