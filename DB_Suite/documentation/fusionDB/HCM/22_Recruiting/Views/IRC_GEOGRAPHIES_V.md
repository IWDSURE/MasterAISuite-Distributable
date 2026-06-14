# IRC_GEOGRAPHIES_V

## Details

**Schema:** FUSION

**Object owner:** IRC

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircgeographiesv-8842.html#ircgeographiesv-8842](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/ircgeographiesv-8842.html#ircgeographiesv-8842)

## Columns

- IRC_GEOGRAPHY_ID
- FQN_TYPE
- FQN
- CITY
- STATE
- COUNTRY
- LANGUAGE
- OBJECT_VERSION_NUMBER
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN

## Query

```sql
SELECT IRC_GEOGRAPHY_ID IRC_GEOGRAPHY_ID, FQN_TYPE FQN_TYPE, FQN FQN, CITY CITY, STATE STATE, COUNTRY COUNTRY, LANGUAGE_CODE LANGUAGE, OBJECT_VERSION_NUMBER OBJECT_VERSION_NUMBER, CREATED_BY CREATED_BY, CREATION_DATE CREATION_DATE, LAST_UPDATED_BY LAST_UPDATED_BY, LAST_UPDATE_DATE LAST_UPDATE_DATE, LAST_UPDATE_LOGIN LAST_UPDATE_LOGIN FROM IRC_GEOGRAPHY_LOCATIONS
```

---

[← Back to Index](../22_Recruiting_Views_Index.md)
