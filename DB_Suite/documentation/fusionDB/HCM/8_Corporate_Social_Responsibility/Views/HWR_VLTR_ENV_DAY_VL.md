# HWR_VLTR_ENV_DAY_VL

## Details

**Schema:** FUSION

**Object owner:** HHR

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrvltrenvdayvl-5536.html#hwrvltrenvdayvl-5536](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrvltrenvdayvl-5536.html#hwrvltrenvdayvl-5536)

## Columns

- ID
- TYPE
- LEARN_MORE_LINK
- SEQUENCE
- NAME
- DESCRIPTION
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN

## Query

```sql
SELECT A.ID, A.TYPE, A.LEARN_MORE_LINK, A.SEQUENCE, B.NAME, B.DESCRIPTION, B.CREATED_BY, B.CREATION_DATE, B.LAST_UPDATED_BY, B.LAST_UPDATE_DATE, B.LAST_UPDATE_LOGIN FROM HWR_VLTR_ENV_DAY_B A, HWR_VLTR_ENV_DAY_TL B WHERE A.ID = B.ID AND B.LANGUAGE = USERENV('LANG')
```

---

[← Back to Index](../8_Corporate_Social_Responsibility_Views_Index.md)
