# PER_CHK_CONTENT_ITEMS_VL

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchkcontentitemsvl-3082.html#perchkcontentitemsvl-3082](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perchkcontentitemsvl-3082.html#perchkcontentitemsvl-3082)

## Columns

- CHK_CONTENT_ITEM_ID
- CONTENT_ITEM_CODE
- CHK_CONTENT_DEFN_ID
- SEQUENCE
- TITLE
- DESCRIPTION
- NOTE_CONTENT_DEFN_ID
- CONTENT_URL
- ENTERPRISE_ID
- OBJECT_VERSION_NUMBER
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN

## Query

```sql
select B.CHK_CONTENT_ITEM_ID, B.CONTENT_ITEM_CODE, B.CHK_CONTENT_DEFN_ID, B.SEQUENCE, T.TITLE, T.DESCRIPTION, B.NOTE_CONTENT_DEFN_ID, B.CONTENT_URL, B.ENTERPRISE_ID, B.OBJECT_VERSION_NUMBER, B.CREATED_BY, B.CREATION_DATE, B.LAST_UPDATED_BY, B.LAST_UPDATE_DATE, B.LAST_UPDATE_LOGIN FROM PER_CHK_CONTENT_ITEMS_B B, PER_CHK_CONTENT_ITEMS_TL T WHERE B.CHK_CONTENT_ITEM_ID = T.CHK_CONTENT_ITEM_ID AND T.LANGUAGE = USERENV('LANG')
```

---

[← Back to Index](../10_Global_Human_Resources_Views_Index.md)
