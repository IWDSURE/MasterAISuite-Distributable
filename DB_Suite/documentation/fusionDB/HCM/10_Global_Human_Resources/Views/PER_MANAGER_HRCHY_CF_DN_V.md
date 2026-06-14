# PER_MANAGER_HRCHY_CF_DN_V

## Details

**Schema:** FUSION

**Object owner:** PER

**Object type:** VIEW

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/permanagerhrchycfdnv-4119.html#permanagerhrchycfdnv-4119](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/permanagerhrchycfdnv-4119.html#permanagerhrchycfdnv-4119)

## Columns

- BUSINESS_GROUP_ID
- MANAGER_ID
- MANAGER_ASSIGNMENT_ID
- EFFECTIVE_START_DATE
- EFFECTIVE_END_DATE
- MANAGER_LEVEL
- MANAGER_TYPE
- LEVEL1_REPORTEE_ASG_ID
- LEVEL1_REPORTEE_PERSON_ID
- LEVEL1_REPORTEE_MANAGER_TYPE
- LEVEL2_REPORTEE_ASG_ID
- LEVEL2_REPORTEE_PERSON_ID
- LEVEL2_REPORTEE_MANAGER_TYPE
- LEVEL3_REPORTEE_ASG_ID
- LEVEL3_REPORTEE_PERSON_ID
- LEVEL3_REPORTEE_MANAGER_TYPE
- LEVEL4_REPORTEE_ASG_ID
- LEVEL4_REPORTEE_PERSON_ID
- LEVEL4_REPORTEE_MANAGER_TYPE
- LEVEL5_REPORTEE_ASG_ID
- LEVEL5_REPORTEE_PERSON_ID
- LEVEL5_REPORTEE_MANAGER_TYPE
- LEVEL6_REPORTEE_ASG_ID
- LEVEL6_REPORTEE_PERSON_ID
- LEVEL6_REPORTEE_MANAGER_TYPE
- LEVEL7_REPORTEE_ASG_ID
- LEVEL7_REPORTEE_PERSON_ID
- LEVEL7_REPORTEE_MANAGER_TYPE
- LEVEL8_REPORTEE_ASG_ID
- LEVEL8_REPORTEE_PERSON_ID
- LEVEL8_REPORTEE_MANAGER_TYPE
- LEVEL9_REPORTEE_ASG_ID
- LEVEL9_REPORTEE_PERSON_ID
- LEVEL9_REPORTEE_MANAGER_TYPE
- LEVEL10_REPORTEE_ASG_ID
- LEVEL10_REPORTEE_PERSON_ID
- LEVEL10_REPORTEE_MANAGER_TYPE
- LEVEL11_REPORTEE_ASG_ID
- LEVEL11_REPORTEE_PERSON_ID
- LEVEL11_REPORTEE_MANAGER_TYPE
- LEVEL12_REPORTEE_ASG_ID
- LEVEL12_REPORTEE_PERSON_ID
- LEVEL12_REPORTEE_MANAGER_TYPE
- LEVEL13_REPORTEE_ASG_ID
- LEVEL13_REPORTEE_PERSON_ID
- LEVEL13_REPORTEE_MANAGER_TYPE
- LEVEL14_REPORTEE_ASG_ID
- LEVEL14_REPORTEE_PERSON_ID
- LEVEL14_REPORTEE_MANAGER_TYPE
- LEVEL15_REPORTEE_ASG_ID
- LEVEL15_REPORTEE_PERSON_ID
- LEVEL15_REPORTEE_MANAGER_TYPE

## Query

```sql
SELECT /*+ NO_MERGE*/ top_business_group_id business_group_id, top_manager_id manager_id, top_manager_assignment_id manager_assignment_id, top_effective_start_date effective_start_date, top_effective_end_date effective_end_date, top_manager_level manager_level, top_manager_type manager_type, NVL(MAX(decode(ldiff, 1, middle_manager_assignment_id)),top_assignment_id) level1_reportee_asg_id, NVL(MAX(DECODE(ldiff, 1, middle_manager_id)),top_person_id) level1_reportee_person_id, NVL(MAX(DECODE(ldiff, 1, middle_manager_type)),top_manager_type) level1_reportee_manager_type, NVL(MAX(decode(ldiff, 2, middle_manager_assignment_id)),top_assignment_id) level2_reportee_asg_id, NVL(MAX(DECODE(ldiff, 2, middle_manager_id)),top_person_id) level2_reportee_person_id, NVL(MAX(DECODE(ldiff, 2, middle_manager_type)),top_manager_type) level2_reportee_manager_type, NVL(MAX(decode(ldiff, 3, middle_manager_assignment_id)),top_assignment_id) level3_reportee_asg_id, NVL(MAX(DECODE(ldiff, 3, middle_manager_id)),top_person_id) level3_reportee_person_id, NVL(MAX(DECODE(ldiff, 3, middle_manager_type)),top_manager_type) level3_reportee_manager_type, NVL(MAX(decode(ldiff, 4, middle_manager_assignment_id)),top_assignment_id) level4_reportee_asg_id, NVL(MAX(DECODE(ldiff, 4, middle_manager_id)),top_person_id) level4_reportee_person_id, NVL(MAX(DECODE(ldiff, 4, middle_manager_type)),top_manager_type) level4_reportee_manager_type, NVL(MAX(decode(ldiff, 5, middle_manager_assignment_id)),top_assignment_id) level5_reportee_asg_id, NVL(MAX(DECODE(ldiff, 5, middle_manager_id)),top_person_id) level5_reportee_person_id, NVL(MAX(DECODE(ldiff, 5, middle_manager_type)),top_manager_type) level5_reportee_manager_type, NVL(MAX(decode(ldiff, 6, middle_manager_assignment_id)),top_assignment_id) level6_reportee_asg_id, NVL(MAX(DECODE(ldiff, 6, middle_manager_id)),top_person_id) level6_reportee_person_id, NVL(MAX(DECODE(ldiff, 6, middle_manager_type)),top_manager_type) level6_reportee_manager_type, NVL(MAX(decode(ldiff, 7, middle_manager_assignment_id)),top_assignment_id) level7_reportee_asg_id, NVL(MAX(DECODE(ldiff, 7, middle_manager_id)),top_person_id) level7_reportee_person_id, NVL(MAX(DECODE(ldiff, 7, middle_manager_type)),top_manager_type) level7_reportee_manager_type, NVL(MAX(decode(ldiff, 8, middle_manager_assignment_id)),top_assignment_id) level8_reportee_asg_id, NVL(MAX(DECODE(ldiff, 8, middle_manager_id)),top_person_id) level8_reportee_person_id, NVL(MAX(DECODE(ldiff, 8, middle_manager_type)),top_manager_type) level8_reportee_manager_type, NVL(MAX(decode(ldiff, 9, middle_manager_assignment_id)),top_assignment_id) level9_reportee_asg_id, NVL(MAX(DECODE(ldiff, 9, middle_manager_id)),top_person_id) level9_reportee_person_id, NVL(MAX(DECODE(ldiff, 9, middle_manager_type)),top_manager_type) level9_reportee_manager_type, NVL(MAX(decode(ldiff,10, middle_manager_assignment_id)),top_assignment_id) level10_reportee_asg_id, NVL(MAX(DECODE(ldiff,10, middle_manager_id)),top_person_id) level10_reportee_person_id, NVL(MAX(DECODE(ldiff,10, middle_manager_type)),top_manager_type) level10_reportee_manager_type, NVL(MAX(decode(ldiff,11, middle_manager_assignment_id)),top_assignment_id) level11_reportee_asg_id, NVL(MAX(DECODE(ldiff,11, middle_manager_id)),top_person_id) level11_reportee_person_id, NVL(MAX(DECODE(ldiff,11, middle_manager_type)),top_manager_type) level11_reportee_manager_type, NVL(MAX(decode(ldiff,12, middle_manager_assignment_id)),top_assignment_id) level12_reportee_asg_id, NVL(MAX(DECODE(ldiff,12, middle_manager_id)),top_person_id) level12_reportee_person_id, NVL(MAX(DECODE(ldiff,12, middle_manager_type)),top_manager_type) level12_reportee_manager_type, NVL(MAX(decode(ldiff,13, middle_manager_assignment_id)),top_assignment_id) level13_reportee_asg_id, NVL(MAX(DECODE(ldiff,13, middle_manager_id)),top_person_id) level13_reportee_person_id, NVL(MAX(DECODE(ldiff,13, middle_manager_type)),top_manager_type) level13_reportee_manager_type, NVL(MAX(decode(ldiff,14, middle_manager_assignment_id)),top_assignment_id) level14_reportee_asg_id, NVL(MAX(DECODE(ldiff,14, middle_manager_id)),top_person_id) level14_reportee_person_id, NVL(MAX(DECODE(ldiff,14, middle_manager_type)),top_manager_type) level14_reportee_manager_type, NVL(MAX(decode(ldiff,15, middle_manager_assignment_id)),top_assignment_id) level15_reportee_asg_id, NVL(MAX(DECODE(ldiff,15, middle_manager_id)),top_person_id) level15_reportee_person_id , NVL(MAX(DECODE(ldiff,15, middle_manager_type)),top_manager_type) level15_reportee_manager_type FROM ( SELECT topmanager.business_group_id top_business_group_id, topmanager.effective_start_date top_effective_start_date, topmanager.effective_end_date top_effective_end_date, topmanager.manager_assignment_id top_manager_assignment_id, topmanager.manager_id top_manager_id, topmanager.manager_level top_manager_level, topmanager.manager_type top_manager_type, topmanager.assignment_id top_assignment_id, topmanager.person_id top_person_id, middlemanager.effective_start_date middle_effective_start_date, middlemanager.effective_end_date middle_effective_end_date, middlemanager.manager_assignment_id middle_manager_assignment_id, middlemanager.manager_id middle_manager_id, middlemanager.assignment_id middle_assignment_id, middlemanager.manager_level middle_manager_level, middlemanager.manager_type middle_manager_type, (topmanager.manager_level - middlemanager.manager_level) ldiff FROM per_manager_hrchy_dn topmanager, per_manager_hrchy_dn middlemanager WHERE 1=1 AND middlemanager.assignment_id = topmanager.assignment_id AND middlemanager.manager_type = topmanager.manager_type AND topmanager.effective_end_date between middlemanager.effective_start_date and middlemanager.effective_end_date AND MiddleManager.manager_level <= TopManager.manager_level ) WHERE 1=1 GROUP BY top_business_group_id,top_manager_id, top_manager_assignment_id, TOP_EFFECTIVE_START_DATE ,TOP_EFFECTIVE_END_DATE , top_person_id,top_assignment_id,top_manager_level , top_manager_type
```

---

[← Back to Index](../10_Global_Human_Resources_Views_Index.md)
