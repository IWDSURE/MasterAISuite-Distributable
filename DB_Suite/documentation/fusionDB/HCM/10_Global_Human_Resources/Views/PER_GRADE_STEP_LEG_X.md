# PER_GRADE_STEP_LEG_X

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/pergradesteplegx-6507.html#pergradesteplegx-6507](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/pergradesteplegx-6507.html#pergradesteplegx-6507)

## Columns

- GRADE_STEP_LEG_ID
- EFFECTIVE_START_DATE
- EFFECTIVE_END_DATE
- LEGISLATION_CODE
- GRADE_STEP_ID
- ACTION_OCCURRENCE_ID
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
- INFORMATION_CATEGORY
- INFORMATION1
- INFORMATION2
- INFORMATION3
- INFORMATION4
- INFORMATION5
- INFORMATION6
- INFORMATION7
- INFORMATION8
- INFORMATION9
- INFORMATION10
- INFORMATION11
- INFORMATION12
- INFORMATION13
- INFORMATION14
- INFORMATION15
- INFORMATION16
- INFORMATION17
- INFORMATION18
- INFORMATION19
- INFORMATION20
- INFORMATION21
- INFORMATION22
- INFORMATION23
- INFORMATION24
- INFORMATION25
- INFORMATION26
- INFORMATION27
- INFORMATION28
- INFORMATION29
- INFORMATION30
- OBJECT_VERSION_NUMBER
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN

## Query

```sql
SELECT grade_step_leg_id , effective_start_date , effective_end_date , legislation_code , grade_step_id , action_occurrence_id , attribute_category , attribute1 , attribute2 , attribute3 , attribute4 , attribute5 , attribute6 , attribute7 , attribute8 , attribute9 , attribute10 , attribute11 , attribute12 , attribute13 , attribute14 , attribute15 , attribute16 , attribute17 , attribute18 , attribute19 , attribute20 , attribute21 , attribute22 , attribute23 , attribute24 , attribute25 , attribute26 , attribute27 , attribute28 , attribute29 , attribute30 , information_category, information1 , information2 , information3 , information4 , information5 , information6 , information7 , information8 , information9 , information10 , information11 , information12 , information13 , information14 , information15 , information16 , information17 , information18 , information19 , information20 , information21 , information22 , information23 , information24 , information25 , information26 , information27 , information28 , information29 , information30 , object_version_number , created_by , creation_date , last_updated_by , last_update_date , last_update_login FROM PER_GRADE_STEP_LEG_F WHERE trunc(sysdate) between effective_start_date and effective_end_date
```

---

[← Back to Index](../10_Global_Human_Resources_Views_Index.md)
