# HWR_MNTR_PLAN_GOALS_VL

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrmntrplangoalsvl-4658.html#hwrmntrplangoalsvl-4658](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrmntrplangoalsvl-4658.html#hwrmntrplangoalsvl-4658)

## Columns

- GOAL_ID
- PLAN_ID
- PERSON_ID
- MPG_ATTR_1
- MPG_ATTR_2
- GOAL_NAME
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN

## Query

```sql
SELECT B.GOAL_ID, B.PLAN_ID, B.PERSON_ID, B.MPG_ATTR_1, B.MPG_ATTR_2, T.GOAL_NAME, B.CREATED_BY, B.CREATION_DATE, B.LAST_UPDATED_BY, B.LAST_UPDATE_DATE, B.LAST_UPDATE_LOGIN FROM HWR_MNTR_PLAN_GOALS_B B, HWR_MNTR_PLAN_GOALS_TL T WHERE B.GOAL_ID = T.GOAL_ID AND T.LANGUAGE = USERENV('LANG')
```

---

[← Back to Index](../34_Workforce_Reputation_Management_Views_Index.md)
