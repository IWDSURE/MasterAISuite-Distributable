# HWR_PER_GBL_PRFL_VL

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrpergblprflvl-5350.html#hwrpergblprflvl-5350](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrpergblprflvl-5350.html#hwrpergblprflvl-5350)

## Columns

- GBL_PRFL_ID
- GENDER_CODE
- EMAIL
- MENTOR_STATUS
- IMAGE_URL
- GAMIFICATION_USER_ID
- GAMIFICATION_PLAYER_ID
- NAME
- FIRST_NAME
- MIDDLE_NAME
- LAST_NAME
- STREET_ADDRESS
- PHONE
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN

## Query

```sql
SELECT B.GBL_PRFL_ID, B.GENDER_CODE, B.EMAIL, B.MENTOR_STATUS, B.IMAGE_URL, B.GAMIFICATION_USER_ID, B.GAMIFICATION_PLAYER_ID, T.NAME, T.FIRST_NAME, T.MIDDLE_NAME, T.LAST_NAME, T.STREET_ADDRESS, T.PHONE, B.CREATED_BY, B.CREATION_DATE, B.LAST_UPDATED_BY, B.LAST_UPDATE_DATE, B.LAST_UPDATE_LOGIN FROM HWR_PER_GBL_PRFL_B B, HWR_PER_GBL_PRFL_TL T WHERE B.GBL_PRFL_ID = T.GBL_PRFL_ID AND T.LANGUAGE = USERENV('LANG')
```

---

[← Back to Index](../34_Workforce_Reputation_Management_Views_Index.md)
