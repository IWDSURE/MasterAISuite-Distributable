# FAI_INSTRUCTIONS_VL

## Details

**Schema:** FUSION

**Object owner:** FAI

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faiinstructionsvl-5109.html#faiinstructionsvl-5109](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faiinstructionsvl-5109.html#faiinstructionsvl-5109)

## Columns

- INSTRUCTION_ID
- TOPIC_ID
- INSTRUCTION_CODE
- INTERNAL_NAME
- INSTRUCTION
- SEEDED_FLAG
- STATUS
- OBJECT_VERSION_NUMBER
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN
- NAME
- DESCRIPTION

## Query

```sql
select B.INSTRUCTION_ID, B.TOPIC_ID, B.INSTRUCTION_CODE, B.INTERNAL_NAME, B.INSTRUCTION, B.SEEDED_FLAG, B.STATUS, B.OBJECT_VERSION_NUMBER, B.CREATED_BY, B.CREATION_DATE, B.LAST_UPDATED_BY, B.LAST_UPDATE_DATE, B.LAST_UPDATE_LOGIN, T.NAME, T.DESCRIPTION FROM FAI_INSTRUCTIONS_B B, FAI_INSTRUCTIONS_TL T WHERE B.INSTRUCTION_ID = T.INSTRUCTION_ID AND T.LANGUAGE = USERENV('LANG')
```

---

[← Back to Index](../2_AI_Views_Index.md)
