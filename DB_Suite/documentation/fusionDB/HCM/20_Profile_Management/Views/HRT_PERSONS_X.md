# HRT_PERSONS_X

## Details

**Schema:** FUSION

**Object owner:** HRT

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtpersonsx-3451.html#hrtpersonsx-3451](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrtpersonsx-3451.html#hrtpersonsx-3451)

## Columns

- PERSON_ID
- DATE_OF_BIRTH
- DATE_OF_DEATH
- COUNTRY_OF_BIRTH
- REGION_OF_BIRTH
- TOWN_OF_BIRTH
- TITLE
- FULL_NAME
- FIRST_NAME
- LAST_NAME
- MIDDLE_NAMES
- ADDRESS_LINE_1
- ADDRESS_LINE_2
- ADDRESS_LINE_3
- COUNTRY
- POSTAL_CODE
- REGION_1
- REGION_2
- REGION_3
- TOWN_OR_CITY
- EMAIL_ADDRESS
- PHONE_NUMBER
- EXTENSION

## Query

```sql
SELECT person.PERSON_ID, person.DATE_OF_BIRTH, person.DATE_OF_DEATH, person.COUNTRY_OF_BIRTH, person.REGION_OF_BIRTH, person.TOWN_OF_BIRTH, personname.TITLE, personname.FULL_NAME, personname.FIRST_NAME, personname.LAST_NAME, personname.MIDDLE_NAMES, personaddress.ADDRESS_LINE_1, personaddress.ADDRESS_LINE_2, personaddress.ADDRESS_LINE_3, personaddress.COUNTRY, personaddress.POSTAL_CODE, personaddress.REGION_1, personaddress.REGION_2, personaddress.REGION_3, personaddress.TOWN_OR_CITY, personemail.EMAIL_ADDRESS, personphone.PHONE_NUMBER, personphone.EXTENSION FROM PER_PERSONS_V person, PER_ALL_PEOPLE_F_V people, PER_PERSON_NAMES_F_V personname, PER_ADDRESSES_F personaddress, PER_EMAIL_ADDRESSES_V personemail, PER_PHONES_V personphone WHERE ((person.PERSON_ID = people.PERSON_ID) AND (TRUNC(SYSDATE) BETWEEN people.EFFECTIVE_START_DATE AND people.EFFECTIVE_END_DATE) ) AND ((person.PERSON_ID = personname.PERSON_ID) AND (TRUNC(SYSDATE) BETWEEN personname.EFFECTIVE_START_DATE AND personname.EFFECTIVE_END_DATE) ) AND ((personaddress.ADDRESS_ID(+) = people.MAILING_ADDRESS_ID) AND (TRUNC(SYSDATE) BETWEEN personaddress.EFFECTIVE_START_DATE(+) AND personaddress.EFFECTIVE_END_DATE(+)) ) AND ((personemail.EMAIL_ADDRESS_ID(+) = people.PRIMARY_EMAIL_ID) ) AND ((personphone.PHONE_ID(+) = people.PRIMARY_PHONE_ID) )
```

---

[← Back to Index](../20_Profile_Management_Views_Index.md)
