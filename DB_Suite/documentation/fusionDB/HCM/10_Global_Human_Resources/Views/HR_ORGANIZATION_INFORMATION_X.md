# HR_ORGANIZATION_INFORMATION_X

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrorganizationinformationx-7075.html#hrorganizationinformationx-7075](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrorganizationinformationx-7075.html#hrorganizationinformationx-7075)

## Columns

- ORG_INFORMATION_ID
- EFFECTIVE_START_DATE
- EFFECTIVE_END_DATE
- ORG_INFORMATION_CONTEXT
- ORGANIZATION_ID
- ORG_INFORMATION1
- ORG_INFORMATION2
- ORG_INFORMATION3
- ORG_INFORMATION4
- ORG_INFORMATION5
- ORG_INFORMATION6
- ORG_INFORMATION7
- ORG_INFORMATION8
- ORG_INFORMATION9
- ORG_INFORMATION10
- ORG_INFORMATION11
- ORG_INFORMATION12
- ORG_INFORMATION13
- ORG_INFORMATION14
- ORG_INFORMATION15
- ORG_INFORMATION16
- ORG_INFORMATION17
- ORG_INFORMATION18
- ORG_INFORMATION19
- ORG_INFORMATION20
- ORG_INFORMATION21
- ORG_INFORMATION22
- ORG_INFORMATION23
- ORG_INFORMATION24
- ORG_INFORMATION25
- ORG_INFORMATION26
- ORG_INFORMATION27
- ORG_INFORMATION28
- ORG_INFORMATION29
- ORG_INFORMATION30
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
- OBJECT_VERSION_NUMBER
- CREATED_BY
- CREATION_DATE
- LAST_UPDATED_BY
- LAST_UPDATE_DATE
- LAST_UPDATE_LOGIN

## Query

```sql
SELECT org_information_id, effective_start_date, effective_end_date, org_information_context, organization_id, org_information1, org_information2, org_information3, org_information4, org_information5, org_information6, org_information7, org_information8, org_information9, org_information10, org_information11, org_information12, org_information13, org_information14, org_information15, org_information16, org_information17, org_information18, org_information19, org_information20, org_information21, org_information22, org_information23, org_information24, org_information25, org_information26, org_information27, org_information28, org_information29, org_information30, attribute_category, attribute1, attribute2, attribute3, attribute4, attribute5, attribute6, attribute7, attribute8, attribute9, attribute10, attribute11, attribute12, attribute13, attribute14, attribute15, attribute16, attribute17, attribute18, attribute19, attribute20, attribute21, attribute22, attribute23, attribute24, attribute25, attribute26, attribute27, attribute28, attribute29, attribute30, object_version_number, created_by, creation_date, last_updated_by, last_update_date, last_update_login FROM hr_organization_information_f WHERE trunc(sysdate) between effective_start_date and effective_end_date
```

---

[← Back to Index](../10_Global_Human_Resources_Views_Index.md)
