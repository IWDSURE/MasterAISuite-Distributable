# CMP_SALARY_SECURED_LIST_V

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpsalarysecuredlistv-5269.html#cmpsalarysecuredlistv-5269](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpsalarysecuredlistv-5269.html#cmpsalarysecuredlistv-5269)

## Columns

- PERSON_ID
- BUSINESS_GROUP_ID
- ASSIGNMENT_ID
- SALARY_ID
- SALARY_BASIS_ID
- ELEMENT_ENTRY_ID
- DATE_FROM
- DATE_TO
- SALARY_AMOUNT
- SALARY_APPROVED
- ACTION_OCCURRENCE_ID
- ACTION_ID
- ACTION_REASON_ID
- MULTIPLE_COMPONENTS
- NEXT_SAL_REVIEW_DATE
- OBJECT_VERSION_NUMBER
- LAST_UPDATE_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_LOGIN
- CREATED_BY
- CREATION_DATE
- ATTRIBUTE_CATEGORY
- ATTRIBUTE1
- ATTRIBUTE2
- ATTRIBUTE3
- ATTRIBUTE4
- ATTRIBUTE5
- ATTRIBUTE6
- ATTRIBUTE7
- ATTRIBUTE8
- ATTRIBUTE9
- ATTRIBUTE10
- ATTRIBUTE11
- ATTRIBUTE12
- ATTRIBUTE13
- ATTRIBUTE14
- ATTRIBUTE15
- ATTRIBUTE16
- ATTRIBUTE17
- ATTRIBUTE18
- ATTRIBUTE19
- ATTRIBUTE20
- ATTRIBUTE21
- ATTRIBUTE22
- ATTRIBUTE23
- ATTRIBUTE24
- ATTRIBUTE25
- ATTRIBUTE26
- ATTRIBUTE27
- ATTRIBUTE28
- ATTRIBUTE29
- ATTRIBUTE30
- ATTRIBUTE_NUMBER1
- ATTRIBUTE_NUMBER2
- ATTRIBUTE_NUMBER3
- ATTRIBUTE_NUMBER4
- ATTRIBUTE_NUMBER5
- ATTRIBUTE_NUMBER6
- ATTRIBUTE_NUMBER7
- ATTRIBUTE_NUMBER8
- ATTRIBUTE_NUMBER9
- ATTRIBUTE_NUMBER10
- ATTRIBUTE_NUMBER11
- ATTRIBUTE_NUMBER12
- ATTRIBUTE_NUMBER13
- ATTRIBUTE_NUMBER14
- ATTRIBUTE_NUMBER15
- ATTRIBUTE_NUMBER16
- ATTRIBUTE_NUMBER17
- ATTRIBUTE_NUMBER18
- ATTRIBUTE_NUMBER19
- ATTRIBUTE_NUMBER20
- ATTRIBUTE_DATE1
- ATTRIBUTE_DATE2
- ATTRIBUTE_DATE3
- ATTRIBUTE_DATE4
- ATTRIBUTE_DATE5
- ATTRIBUTE_DATE6
- ATTRIBUTE_DATE7
- ATTRIBUTE_DATE8
- ATTRIBUTE_DATE9
- ATTRIBUTE_DATE10
- ATTRIBUTE_DATE11
- ATTRIBUTE_DATE12
- ATTRIBUTE_DATE13
- ATTRIBUTE_DATE14
- ATTRIBUTE_DATE15

## Query

```sql
Select Asg.Person_Id ,CSL.business_group_id ,CSL.assignment_id ,CSL.salary_id ,CSL.salary_basis_id ,CSL.element_entry_id ,CSL.date_from ,CSL.date_to ,CSL.salary_amount ,CSL.salary_approved ,CSL.action_occurrence_id ,CSL.action_id ,CSL.action_reason_id ,CSL.multiple_components ,CSL.next_sal_review_date ,CSL.object_version_number ,CSL.last_update_date ,CSL.last_updated_by ,CSL.last_update_login ,CSL.created_by ,CSL.creation_date ,CSL.attribute_category ,CSL.attribute1 ,CSL.attribute2 ,CSL.attribute3 ,CSL.attribute4 ,CSL.attribute5 ,CSL.attribute6 ,CSL.attribute7 ,CSL.attribute8 ,CSL.attribute9 ,CSL.attribute10 ,CSL.attribute11 ,CSL.attribute12 ,CSL.attribute13 ,CSL.attribute14 ,CSL.attribute15 ,CSL.attribute16 ,CSL.attribute17 ,CSL.attribute18 ,CSL.attribute19 ,CSL.attribute20 ,CSL.attribute21 ,CSL.attribute22 ,CSL.attribute23 ,CSL.attribute24 ,CSL.attribute25 ,CSL.attribute26 ,CSL.attribute27 ,CSL.attribute28 ,CSL.attribute29 ,CSL.attribute30 ,CSL.attribute_number1 ,CSL.attribute_number2 ,CSL.attribute_number3 ,CSL.attribute_number4 ,CSL.attribute_number5 ,CSL.attribute_number6 ,CSL.attribute_number7 ,CSL.attribute_number8 ,CSL.attribute_number9 ,CSL.attribute_number10 ,CSL.attribute_number11 ,CSL.attribute_number12 ,CSL.attribute_number13 ,CSL.attribute_number14 ,CSL.attribute_number15 ,CSL.attribute_number16 ,CSL.attribute_number17 ,CSL.attribute_number18 ,CSL.attribute_number19 ,CSL.attribute_number20 ,CSL.attribute_date1 ,CSL.attribute_date2 ,CSL.attribute_date3 ,CSL.attribute_date4 ,CSL.attribute_date5 ,CSL.attribute_date6 ,CSL.attribute_date7 ,CSL.attribute_date8 ,CSL.attribute_date9 ,CSL.attribute_date10 ,CSL.attribute_date11 ,CSL.attribute_date12 ,CSL.attribute_date13 ,CSL.attribute_date14 ,CSL.attribute_date15 From Cmp_Salary Csl , Per_All_Assignments_F Asg Where csl.Assignment_Id = Asg.Assignment_Id And Csl.Date_From Between Asg.Effective_Start_Date And Asg.Effective_End_Date
```

---

[← Back to Index](../7_Compensation_Views_Index.md)
