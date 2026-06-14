# HWM_TE_MESSAGES_V

## Details

**Schema:** FUSION

**Object owner:** HWM

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtemessagesv-6280.html#hwmtemessagesv-6280](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwmtemessagesv-6280.html#hwmtemessagesv-6280)

## Columns

- MESSAGE_NAME
- MESSAGE_NUMBER
- APPLICATION_SHORT_NAME
- APPLICATION_ID
- MESSAGE_LEVEL
- MESSAGE_TEXT
- CONTEXT
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN
- MESSAGE_USER_DETAILS

## Query

```sql
select distinct TimeMessagePEO.MESSAGE_NAME, fndMessagesVLPEO.MESSAGE_NUMBER, TimeMessagePEO.APPLICATION_SHORT_NAME, fndMessagesVLPEO.APPLICATION_ID, TimeMessagePEO.MESSAGE_LEVEL, fndMessagesVLPEO.MESSAGE_TEXT, fndMessagesVLPEO.CONTEXT, fndMessagesVLPEO.CREATED_BY, fndMessagesVLPEO.CREATION_DATE, fndMessagesVLPEO.LAST_UPDATED_BY, fndMessagesVLPEO.LAST_UPDATE_DATE, fndMessagesVLPEO.LAST_UPDATE_LOGIN, fndMessagesVLPEO.MESSAGE_USER_DETAILS from fusion.HWM_TM_REP_MSGS TimeMessagePEO, fusion.FND_MESSAGES_VL fndMessagesVLPEO, fusion.FND_APPLICATION fndApplicationPEO, fusion.HWM_TM_REC TimeRecordPEO where TimeMessagePEO.APPLICATION_SHORT_NAME = fndApplicationPEO.APPLICATION_SHORT_NAME and TimeMessagePEO.MESSAGE_NAME = fndMessagesVLPEO.MESSAGE_NAME and fndApplicationPEO.APPLICATION_ID = fndMessagesVLPEO.APPLICATION_ID and TimeMessagePEO.TM_BLDG_BLK_ID = TimeRecordPEO.TM_REC_ID and TimeMessagePEO.TM_BLDG_BLK_VERSION = TimeRecordPEO.TM_REC_VERSION and TimeRecordPEO.GRP_TYPE_ID IN (102, 106)
```

---

[← Back to Index](../31_Workforce_Management_Views_Index.md)
