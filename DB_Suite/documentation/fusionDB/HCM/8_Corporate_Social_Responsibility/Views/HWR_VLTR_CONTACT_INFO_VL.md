# HWR_VLTR_CONTACT_INFO_VL

## Details

**Schema:** FUSION

**Object owner:** HHR

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrvltrcontactinfovl-7191.html#hwrvltrcontactinfovl-7191](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hwrvltrcontactinfovl-7191.html#hwrvltrcontactinfovl-7191)

## Columns

- ID
- CONTACT_PHONE
- CONTACT_FAX
- EMAIL
- WEBSITE
- LOCATION_ID
- ADDRESS_TYPE
- ENTITY_ID
- ENTITY_TYPE
- CONTACT_TITLE
- CONTACT_NAME
- CREATED_BY
- CREATION_DATE
- LAST_UPDATE_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_LOGIN

## Query

```sql
SELECT A.ID, A.CONTACT_PHONE, A.CONTACT_FAX, A.EMAIL, A.WEBSITE, A.LOCATION_ID, A.ADDRESS_TYPE, A.ENTITY_ID, A.ENTITY_TYPE, B.CONTACT_TITLE, B.CONTACT_NAME, B.CREATED_BY, B.CREATION_DATE, B.LAST_UPDATE_DATE, B.LAST_UPDATED_BY, B.LAST_UPDATE_LOGIN FROM HWR_VLTR_CONTACT_INFO_B A, HWR_VLTR_CONTACT_INFO_TL B WHERE A.ID = B.ID AND B.LANGUAGE = USERENV('LANG')
```

---

[← Back to Index](../8_Corporate_Social_Responsibility_Views_Index.md)
