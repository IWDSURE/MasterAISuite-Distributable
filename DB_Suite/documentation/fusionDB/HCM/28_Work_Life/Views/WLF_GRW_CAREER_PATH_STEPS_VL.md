# WLF_GRW_CAREER_PATH_STEPS_VL

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfgrwcareerpathstepsvl-7624.html#wlfgrwcareerpathstepsvl-7624](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfgrwcareerpathstepsvl-7624.html#wlfgrwcareerpathstepsvl-7624)

## Columns

- CAREER_PATH_STEP_ID
- NAME
- DISPLAY_SEQUENCE
- CAREER_PATH_ID
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN
- OBJECT_VERSION_NUMBER
- LANGUAGE
- SOURCE_LANG

## Query

```sql
SELECT B.CAREER_PATH_STEP_ID, TL.NAME, B.DISPLAY_SEQUENCE, B.CAREER_PATH_ID, B.CREATED_BY, B.CREATION_DATE, B.LAST_UPDATED_BY, B.LAST_UPDATE_DATE, B.LAST_UPDATE_LOGIN, B.OBJECT_VERSION_NUMBER, TL.LANGUAGE, TL.SOURCE_LANG FROM WLF_GRW_CAREER_PATH_STEPS_B B, WLF_GRW_CAREER_PATH_STEPS_TL TL WHERE B.CAREER_PATH_STEP_ID = TL.CAREER_PATH_STEP_ID AND TL.LANGUAGE = USERENV('LANG')
```

---

[← Back to Index](../28_Work_Life_Views_Index.md)
