# FAI_SAM_BASE_SEQUENCE_DEF_VL

## Details

**Schema:** FUSION

**Object owner:** FAI

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faisambasesequencedefvl-7167.html#faisambasesequencedefvl-7167](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/faisambasesequencedefvl-7167.html#faisambasesequencedefvl-7167)

## Columns

- BASE_SEQUENCE_DEF_ID
- TYPE
- BASE_SEQUENCE_KEY
- NAME
- DESCRIPTION
- SEQUENCER
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN
- ENTERPRISE_ID
- SGUID
- MODULE_ID
- OBJECT_VERSION_NUMBER

## Query

```sql
Select B.BASE_SEQUENCE_DEF_ID ,B.TYPE ,B.BASE_SEQUENCE_KEY ,TL.NAME ,TL.DESCRIPTION ,B.SEQUENCER ,B.CREATED_BY ,B.CREATION_DATE ,B.LAST_UPDATED_BY ,B.LAST_UPDATE_DATE ,B.LAST_UPDATE_LOGIN ,B.ENTERPRISE_ID ,B.SGUID ,B.MODULE_ID ,B.OBJECT_VERSION_NUMBER FROM FAI_SAM_BASE_SEQUENCE_DEF_B B, FAI_SAM_BASE_SEQUENCE_DEF_TL TL WHERE B.BASE_SEQUENCE_DEF_ID = TL.BASE_SEQUENCE_DEF_ID AND TL.LANGUAGE = USERENV('LANG')
```

---

[← Back to Index](../2_AI_Views_Index.md)
