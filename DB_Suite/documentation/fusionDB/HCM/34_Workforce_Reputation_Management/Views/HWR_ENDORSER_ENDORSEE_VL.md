# HWR_ENDORSER_ENDORSEE_VL

## Details

**Schema:** FUSION

**Object owner:** HWR

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrendorserendorseevl-3953.html#hwrendorserendorseevl-3953](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrendorserendorseevl-3953.html#hwrendorserendorseevl-3953)

## Columns

- DISPLAY_TEXT
- ENDORSER_PRFL_ID
- ENDORSEE_PRFL_ID
- LAST_UPDATE_DATE

## Query

```sql
SELECT NVL(TL.DISPLAY_TEXT, (SELECT DISPLAY_TEXT FROM HWR_CAT_TOPIC_TL TL1 WHERE TL1.TOPIC_ID = T.TOPIC_ID AND ROWNUM =1 )) AS DISPLAY_TEXT, B.RECOMMENDER_FUS_PRFL_ID ENDORSER_PRFL_ID, B.ENDORSEE_FUS_PRFL_ID ENDORSEE_PRFL_ID, B.LAST_UPDATE_DATE FROM HWR_CAT_TOPIC_TL TL, HWR_ENDORSEMENT_B B, HWR_CAT_TOPIC_B T WHERE TL.LANGUAGE(+) = 'US' AND TL.TOPIC_ID(+) = T.TOPIC_ID AND T.TOPIC_ID = B.TOPIC_ID
```

---

[← Back to Index](../34_Workforce_Reputation_Management_Views_Index.md)
