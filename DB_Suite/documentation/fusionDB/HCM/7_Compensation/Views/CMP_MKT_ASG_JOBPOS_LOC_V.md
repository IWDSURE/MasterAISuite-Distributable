# CMP_MKT_ASG_JOBPOS_LOC_V

## Details

**Schema:** FUSION

**Object owner:** CMP

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpmktasgjobposlocv-7339.html#cmpmktasgjobposlocv-7339](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/cmpmktasgjobposlocv-7339.html#cmpmktasgjobposlocv-7339)

## Columns

- ASSIGNMENT_ID
- EFFECTIVE_LATEST_CHANGE
- ASGN_JOB_ID
- ASGN_POSITION_ID
- ASGN_LOCATION_ID
- JOB_LIST_ID
- VENDOR_ID
- VENDOR_JOB_CODE
- JOB_FUNCTION_ID
- JOB_FAMILY_ID
- CAREER_STREAM_ID
- CAREER_LEVEL_ID
- OTHER_LEVEL_ID
- VENDOR_JOB_MAPPING_CODE
- MKTJOB_POSITION_ID
- MKTJOB_JOB_ID
- STATUS
- BUSINESS_GROUP_ID
- SURVEY_LOCATION_ID
- SURVEY_LOCATION_CODE
- SURVEY_LOCATION_MAP_ID
- MKTLOCMAP_LOCATION_ID
- CHILDJOBBENCHMARKJOBID
- DIRECTINDIRECTCODE
- ANCHORINGJOBINDICATORCODE

## Query

```sql
SELECT asgn.ASSIGNMENT_ID, asgn.EFFECTIVE_LATEST_CHANGE, asgn.job_id asgn_job_id, asgn.position_id asgn_position_id, asgn.location_id asgn_location_id, mktjob.job_list_id, mktjob.vendor_id, mktjob.vendor_job_code, mktjob.job_function_id, mktjob.job_family_id, mktjob.career_stream_id, mktjob.career_level_id, mktjob.other_level_id, mktjob.vendor_job_mapping_code, mktjob.position_id mktjob_position_id, mktjob.job_id mktjob_job_id, mktjob.status, mktjob.business_group_id, mktloc.SURVEY_LOCATION_ID , mktloc.SURVEY_LOCATION_CODE, mktlocmap.SURVEY_LOCATION_MAP_ID, mktlocmap.LOCATION_ID mktlocmap_LOCATION_ID, childjob.BENCHMARK_JOB_ID childjobbenchmarkjobid, ( case when ( asgn.JOB_ID = mktjob.JOB_ID ) then 'D' when ( childjob.BENCHMARK_JOB_ID = mktjob.JOB_ID ) then 'I' else null end ) DirectIndirectCode, ( case when ( asgn.JOB_ID = mktjob.JOB_ID AND childjob.BENCHMARK_JOB_FLAG = 'Y' ) then 'P' when ( childjob.BENCHMARK_JOB_ID = mktjob.JOB_ID ) then 'C' else 'N' end ) AnchoringJobIndicatorCode FROM PER_ALL_ASSIGNMENTS_M asgn, CMP_MKT_VND_JOBS_B mktjob, CMP_MKT_VND_LOC_B mktloc, CMP_MKT_VND_LOC_MAP mktlocmap, PER_JOBS_F childjob WHERE mktjob.VENDOR_ID = mktloc.VENDOR_ID AND mktloc.VENDOR_ID = mktlocmap.VENDOR_ID AND mktloc.SURVEY_LOCATION_ID = mktlocmap.SURVEY_LOCATION_ID AND asgn.LOCATION_ID = mktlocmap.LOCATION_ID AND asgn.JOB_ID = childjob.JOB_ID(+) AND asgn.EFFECTIVE_LATEST_CHANGE = 'Y' AND ( asgn.ASSIGNMENT_TYPE = 'E' or asgn.ASSIGNMENT_TYPE = 'C' or asgn.ASSIGNMENT_TYPE = 'N' or asgn.ASSIGNMENT_TYPE = 'P' ) AND ( ( asgn.JOB_ID = mktjob.JOB_ID OR childjob.BENCHMARK_JOB_ID = mktjob.JOB_ID ) OR ( mktjob.VENDOR_JOB_MAPPING_CODE = 'ORA_CMP_MD_POSITION' AND asgn.POSITION_ID = mktjob.POSITION_ID ) ) AND trunc(sysdate) BETWEEN asgn.EFFECTIVE_START_DATE AND asgn.EFFECTIVE_END_DATE AND trunc(sysdate) BETWEEN childjob.EFFECTIVE_START_DATE(+) AND childjob.EFFECTIVE_END_DATE(+)
```

---

[← Back to Index](../7_Compensation_Views_Index.md)
