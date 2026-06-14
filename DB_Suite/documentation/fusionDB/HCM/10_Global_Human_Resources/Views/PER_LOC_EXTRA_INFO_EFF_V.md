# PER_LOC_EXTRA_INFO_EFF_V

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perlocextrainfoeffv-4398.html#perlocextrainfoeffv-4398](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/perlocextrainfoeffv-4398.html#perlocextrainfoeffv-4398)

## Columns

- EFF_LINE_ID
- EFFECTIVE_START_DATE
- EFFECTIVE_END_DATE
- OBJECT_VERSION_NUMBER
- BUSINESS_GROUP_ID
- INFORMATION_TYPE
- LEGISLATION_CODE
- LOCATION_ID
- ACTION_OCCURRENCE_ID
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN
- LEI_ATTRIBUTE_CATEGORY
- LEI_ATTRIBUTE1
- LEI_ATTRIBUTE2
- LEI_ATTRIBUTE3
- LEI_ATTRIBUTE4
- LEI_ATTRIBUTE5
- LEI_ATTRIBUTE6
- LEI_ATTRIBUTE7
- LEI_ATTRIBUTE8
- LEI_ATTRIBUTE9
- LEI_ATTRIBUTE10
- LEI_ATTRIBUTE11
- LEI_ATTRIBUTE12
- LEI_ATTRIBUTE13
- LEI_ATTRIBUTE14
- LEI_ATTRIBUTE15
- LEI_ATTRIBUTE16
- LEI_ATTRIBUTE17
- LEI_ATTRIBUTE18
- LEI_ATTRIBUTE19
- LEI_ATTRIBUTE20
- LEI_ATTRIBUTE21
- LEI_ATTRIBUTE22
- LEI_ATTRIBUTE23
- LEI_ATTRIBUTE24
- LEI_ATTRIBUTE25
- LEI_ATTRIBUTE26
- LEI_ATTRIBUTE27
- LEI_ATTRIBUTE28
- LEI_ATTRIBUTE29
- LEI_ATTRIBUTE30
- CONTEXT_CODE
- LEI_INFORMATION1
- LEI_INFORMATION2
- LEI_INFORMATION3
- LEI_INFORMATION4
- LEI_INFORMATION5
- LEI_INFORMATION6
- LEI_INFORMATION7
- LEI_INFORMATION8
- LEI_INFORMATION9
- LEI_INFORMATION10
- LEI_INFORMATION11
- LEI_INFORMATION12
- LEI_INFORMATION13
- LEI_INFORMATION14
- LEI_INFORMATION15
- LEI_INFORMATION16
- LEI_INFORMATION17
- LEI_INFORMATION18
- LEI_INFORMATION19
- LEI_INFORMATION20
- LEI_INFORMATION21
- LEI_INFORMATION22
- LEI_INFORMATION23
- LEI_INFORMATION24
- LEI_INFORMATION25
- LEI_INFORMATION26
- LEI_INFORMATION27
- LEI_INFORMATION28
- LEI_INFORMATION29
- LEI_INFORMATION30

## Query

```sql
( select location_extra_info_id as EFF_LINE_ID, effective_start_date, effective_end_date, object_version_number, business_group_id, information_type, legislation_code, location_id, action_occurrence_id, created_by, creation_date, last_updated_by, last_update_date, last_update_login, lei_attribute_category, lei_attribute1, lei_attribute2, lei_attribute3, lei_attribute4, lei_attribute5, lei_attribute6, lei_attribute7, lei_attribute8, lei_attribute9, lei_attribute10, lei_attribute11, lei_attribute12, lei_attribute13, lei_attribute14, lei_attribute15, lei_attribute16, lei_attribute17, lei_attribute18, lei_attribute19, lei_attribute20, lei_attribute21, lei_attribute22, lei_attribute23, lei_attribute24, lei_attribute25, lei_attribute26, lei_attribute27, lei_attribute28, lei_attribute29, lei_attribute30, lei_information_category as CONTEXT_CODE, lei_information1, lei_information2, lei_information3, lei_information4, lei_information5, lei_information6, lei_information7, lei_information8, lei_information9, lei_information10, lei_information11, lei_information12, lei_information13, lei_information14, lei_information15, lei_information16, lei_information17, lei_information18, lei_information19, lei_information20, lei_information21, lei_information22, lei_information23, lei_information24, lei_information25, lei_information26, lei_information27, lei_information28, lei_information29, lei_information30 from per_location_extra_info_f)
```

---

[← Back to Index](../10_Global_Human_Resources_Views_Index.md)
