# WLF_CM_SHARES_LIST_V

## Details

**Schema:** FUSION

**Object owner:** WLF

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfcmshareslistv-6008.html#wlfcmshareslistv-6008](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/wlfcmshareslistv-6008.html#wlfcmshareslistv-6008)

## Columns

- SHARE_PROFILE_ID
- EFFECTIVE_START_DATE
- EFFECTIVE_END_DATE
- CONTENT_ID
- SHARED_BY_ID
- SHARED_TO_ID

## Query

```sql
WITH SHARE_PROFILE_DETAILS AS ( SELECT ShareProfiles.SHARE_PROFILE_ID, ShareProfiles.EFFECTIVE_START_DATE, ShareProfiles.EFFECTIVE_END_DATE, ShareProfiles.CREATED_BY_ID, ShareProfiles.CONTENT_ID, ShareProfileDestinations.OPERATION, ShareProfileDestinations.TYPE, ShareProfileDestinations.SHARED_TO_ID FROM WLF_CM_SHARE_PROFILES_F ShareProfiles, WLF_CM_SP_DESTINATIONS_F ShareProfileDestinations WHERE ShareProfileDestinations.SHARE_PROFILE_ID = ShareProfiles.SHARE_PROFILE_ID AND TRUNC(SYSDATE) BETWEEN ShareProfileDestinations.EFFECTIVE_START_DATE AND ShareProfileDestinations.EFFECTIVE_END_DATE AND ShareProfiles.STATUS = 'ACTIVE' AND ShareProfiles.SHARE_TYPE = 'SHARE' AND TRUNC(SYSDATE) BETWEEN ShareProfiles.EFFECTIVE_START_DATE AND ShareProfiles.EFFECTIVE_END_DATE), SHARE_INCLUSION_LIST AS ( SELECT DISTINCT ManagerHierarchy.PERSON_ID, ShareProfileDetails.SHARE_PROFILE_ID, ShareProfileDetails.EFFECTIVE_START_DATE, ShareProfileDetails.EFFECTIVE_END_DATE, ShareProfileDetails.CREATED_BY_ID, ShareProfileDetails.CONTENT_ID FROM SHARE_PROFILE_DETAILS ShareProfileDetails, PER_MANAGER_HRCHY_DN ManagerHierarchy WHERE ShareProfileDetails.SHARED_TO_ID = ManagerHierarchy.MANAGER_ID AND ManagerHierarchy.MANAGER_LEVEL = (CASE WHEN ShareProfileDetails.TYPE = 'ORG' THEN ManagerHierarchy.MANAGER_LEVEL WHEN ShareProfileDetails.TYPE = 'DIR' THEN 1 END) AND TRUNC(SYSDATE) BETWEEN ManagerHierarchy.EFFECTIVE_START_DATE AND ManagerHierarchy.EFFECTIVE_END_DATE AND ManagerHierarchy.MANAGER_TYPE = 'LINE_MANAGER' AND ShareProfileDetails.OPERATION = 'INCLUDE' UNION SELECT ShareProfileDetails.SHARED_TO_ID AS PERSON_ID, ShareProfileDetails.SHARE_PROFILE_ID, ShareProfileDetails.EFFECTIVE_START_DATE, ShareProfileDetails.EFFECTIVE_END_DATE, ShareProfileDetails.CREATED_BY_ID, ShareProfileDetails.CONTENT_ID FROM SHARE_PROFILE_DETAILS ShareProfileDetails WHERE ShareProfileDetails.TYPE = 'PER' AND ShareProfileDetails.OPERATION = 'INCLUDE'), SHARE_EXCLUSION_LIST AS ( SELECT DISTINCT ManagerHierarchy.PERSON_ID, ShareProfileDetails.SHARE_PROFILE_ID, ShareProfileDetails.EFFECTIVE_START_DATE, ShareProfileDetails.EFFECTIVE_END_DATE, ShareProfileDetails.CREATED_BY_ID, ShareProfileDetails.CONTENT_ID FROM SHARE_PROFILE_DETAILS ShareProfileDetails, PER_MANAGER_HRCHY_DN ManagerHierarchy WHERE ShareProfileDetails.SHARED_TO_ID = ManagerHierarchy.MANAGER_ID AND ManagerHierarchy.MANAGER_LEVEL = (CASE WHEN ShareProfileDetails.TYPE = 'ORG' THEN ManagerHierarchy.MANAGER_LEVEL WHEN ShareProfileDetails.TYPE = 'DIR' THEN 1 END) AND TRUNC(SYSDATE) BETWEEN ManagerHierarchy.EFFECTIVE_START_DATE AND ManagerHierarchy.EFFECTIVE_END_DATE AND ManagerHierarchy.MANAGER_TYPE = 'LINE_MANAGER' AND ShareProfileDetails.OPERATION = 'EXCLUDE' UNION SELECT ShareProfileDetails.SHARED_TO_ID AS PERSON_ID, ShareProfileDetails.SHARE_PROFILE_ID, ShareProfileDetails.EFFECTIVE_START_DATE, ShareProfileDetails.EFFECTIVE_END_DATE, ShareProfileDetails.CREATED_BY_ID, ShareProfileDetails.CONTENT_ID FROM SHARE_PROFILE_DETAILS ShareProfileDetails WHERE ShareProfileDetails.TYPE = 'PER' AND ShareProfileDetails.OPERATION = 'EXCLUDE') SELECT ShareInclusionList.SHARE_PROFILE_ID, ShareInclusionList.EFFECTIVE_START_DATE, ShareInclusionList.EFFECTIVE_END_DATE, ShareInclusionList.CONTENT_ID, ShareInclusionList.CREATED_BY_ID AS SHARED_BY_ID, ShareInclusionList.PERSON_ID AS SHARED_TO_ID FROM SHARE_INCLUSION_LIST ShareInclusionList MINUS SELECT ShareExclusionList.SHARE_PROFILE_ID, ShareExclusionList.EFFECTIVE_START_DATE, ShareExclusionList.EFFECTIVE_END_DATE, ShareExclusionList.CONTENT_ID, ShareExclusionList.CREATED_BY_ID AS SHARED_BY_ID, ShareExclusionList.PERSON_ID AS SHARED_TO_ID FROM SHARE_EXCLUSION_LIST ShareExclusionList
```

---

[← Back to Index](../28_Work_Life_Views_Index.md)
