# HWR_SKILLS_SOURCE_VL

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrskillssourcevl-4336.html#hwrskillssourcevl-4336](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrskillssourcevl-4336.html#hwrskillssourcevl-4336)

## Columns

- SKILL_ID
- IS_ENABLED
- SKILL_NAME
- SKILL_DESCRIPTION
- SKILL_ATTR_1
- SKILL_ATTR_2
- SKILL_ATTR_3
- SKILL_ATTR_4
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN

## Query

```sql
SELECT B.SKILL_ID , B.IS_ENABLED , T.SKILL_NAME , T.SKILL_DESCRIPTION , B.SKILL_ATTR_1 , B.SKILL_ATTR_2 , B.SKILL_ATTR_3 , B.SKILL_ATTR_4 , B.CREATED_BY , B.CREATION_DATE , B.LAST_UPDATED_BY , B.LAST_UPDATE_DATE , B.LAST_UPDATE_LOGIN FROM HWR_SKILLS_SOURCE_B B, HWR_SKILLS_SOURCE_TL T WHERE B.SKILL_ID = T.SKILL_ID AND T.LANGUAGE = USERENV('LANG')
```

---

[← Back to Index](../34_Workforce_Reputation_Management_Views_Index.md)
