# Manager Identification Report

**Date**: 2026-06-14
**Worker Person Number**: FD100006
**Worker Name**: ABDULGHAFFARISHAQA.GHAFFAR M.
**Worker Person ID**: 100000013339986

## Manager Details
- **Manager Person Number**: TM100007
- **Manager Name**: MARWAN AHMAD ABDULLA AL ALI
- **Manager Type**: LINE_MANAGER
- **Primary Manager**: Yes (Y)

## Query Used
```sql
SELECT 
    mgr_p.person_number AS manager_person_number,
    mgr_n.full_name AS manager_name,
    sup.manager_type,
    sup.primary_flag
FROM 
    PER_ASSIGNMENT_SUPERVISORS_F sup,
    PER_ALL_PEOPLE_F mgr_p,
    PER_PERSON_NAMES_F mgr_n
WHERE 
    sup.person_id = '100000013339986'
    AND sup.manager_id = mgr_p.person_id
    AND mgr_p.person_id = mgr_n.person_id
    AND mgr_n.name_type = 'GLOBAL'
    AND TRUNC(SYSDATE) BETWEEN sup.effective_start_date AND sup.effective_end_date
    AND TRUNC(SYSDATE) BETWEEN mgr_p.effective_start_date AND mgr_p.effective_end_date
    AND TRUNC(SYSDATE) BETWEEN mgr_n.effective_start_date AND mgr_n.effective_end_date
```
