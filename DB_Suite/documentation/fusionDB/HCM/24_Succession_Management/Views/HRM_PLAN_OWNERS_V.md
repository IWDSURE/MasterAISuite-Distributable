# HRM_PLAN_OWNERS_V

## Details

**Schema:** FUSION

**Object owner:** HRM

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrmplanownersv-7544.html#hrmplanownersv-7544](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrmplanownersv-7544.html#hrmplanownersv-7544)

## Columns

- ENTERPRISE_ID
- PLAN_OWNER_ID
- PLAN_ID
- PERSON_ID
- OWNER_TYPE_CODE
- OBJECT_VERSION_NUMBER
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN
- LATEST_RECORD_FLAG
- OPERATION_TYPE
- DATE_FROM
- DATE_TO
- ENABLE_ALERT
- SOURCE_CODE
- SOURCE_KEY

## Query

```sql
SELECT hrm_plan_owners.ENTERPRISE_ID ENTERPRISE_ID, hrm_plan_owners.PLAN_OWNER_ID PLAN_OWNER_ID, hrm_plan_owners.PLAN_ID PLAN_ID, hrm_plan_owners.PERSON_ID PERSON_ID, hrm_plan_owners.OWNER_TYPE_CODE OWNER_TYPE_CODE, hrm_plan_owners.OBJECT_VERSION_NUMBER OBJECT_VERSION_NUMBER, hrm_plan_owners.CREATED_BY CREATED_BY, hrm_plan_owners.CREATION_DATE CREATION_DATE, hrm_plan_owners.LAST_UPDATED_BY LAST_UPDATED_BY, hrm_plan_owners.LAST_UPDATE_DATE LAST_UPDATE_DATE, hrm_plan_owners.LAST_UPDATE_LOGIN LAST_UPDATE_LOGIN, hrm_plan_owners.LATEST_RECORD_FLAG LATEST_RECORD_FLAG, hrm_plan_owners.OPERATION_TYPE OPERATION_TYPE, hrm_plan_owners.DATE_FROM DATE_FROM, hrm_plan_owners.DATE_TO DATE_TO, hrm_plan_owners.ENABLE_ALERT ENABLE_ALERT, hrm_plan_owners.SOURCE_CODE, hrm_plan_owners.SOURCE_KEY FROM hrm_plan_owners WHERE hrm_plan_owners.LATEST_RECORD_FLAG='Y'
```

---

[← Back to Index](../24_Succession_Management_Views_Index.md)
