# HHR_VLTR_PROJECT_GUEST_VL

## Details

**Schema:** FUSION

**Object owner:** HHR

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hhrvltrprojectguestvl-3306.html#hhrvltrprojectguestvl-3306](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hhrvltrprojectguestvl-3306.html#hhrvltrprojectguestvl-3306)

## Columns

- PROJECT_ID
- GUEST_ID
- FIRST_NAME
- LAST_NAME
- EMAIL
- T_SIZE
- T_STYLE
- IS_MINOR
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN
- HCM_PERSON_ID

## Query

```sql
SELECT B.PROJECT_ID PROJECT_ID, B.GUEST_ID GUEST_ID, T.FIRST_NAME FIRST_NAME, T.LAST_NAME LAST_NAME, T.EMAIL EMAIL, B.T_SIZE T_SIZE, B.T_STYLE T_STYLE, B.IS_MINOR IS_MINOR, B.CREATED_BY CREATED_BY, B.CREATION_DATE CREATION_DATE, B.LAST_UPDATED_BY LAST_UPDATED_BY, B.LAST_UPDATE_DATE LAST_UPDATE_DATE, B.LAST_UPDATE_LOGIN LAST_UPDATE_LOGIN, B.HCM_PERSON_ID HCM_PERSON_ID FROM HHR_VLTR_PROJECT_GUEST_B B, HHR_VLTR_PROJECT_GUEST_TL T WHERE B.GUEST_ID = T.GUEST_ID AND B.PROJECT_ID = T.PROJECT_ID AND T.LANGUAGE = USERENV('LANG')
```

---

[← Back to Index](../8_Corporate_Social_Responsibility_Views_Index.md)
