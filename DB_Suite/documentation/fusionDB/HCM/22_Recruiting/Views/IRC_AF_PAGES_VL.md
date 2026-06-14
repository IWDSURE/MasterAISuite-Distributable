# IRC_AF_PAGES_VL

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircafpagesvl-5463.html#ircafpagesvl-5463](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircafpagesvl-5463.html#ircafpagesvl-5463)

## Columns

- PAGE_ID
- SECTION_ID
- PAGE_SEQ_NUM
- PAGE_NAME
- OBJECT_VERSION_NUMBER
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN

## Query

```sql
SELECT B.PAGE_ID PAGE_ID, B.SECTION_ID SECTION_ID, B.PAGE_SEQ_NUM PAGE_SEQ_NUM, TL.PAGE_NAME PAGE_NAME, B.OBJECT_VERSION_NUMBER OBJECT_VERSION_NUMBER, B.CREATED_BY CREATED_BY, B.CREATION_DATE CREATION_DATE, B.LAST_UPDATED_BY LAST_UPDATED_BY, B.LAST_UPDATE_DATE LAST_UPDATE_DATE, B.LAST_UPDATE_LOGIN LAST_UPDATE_LOGIN FROM IRC_AF_PAGES_B B, IRC_AF_PAGES_TL TL WHERE B.PAGE_ID = TL.PAGE_ID AND TL.LANGUAGE = USERENV('LANG')
```

---

[← Back to Index](../22_Recruiting_Views_Index.md)
