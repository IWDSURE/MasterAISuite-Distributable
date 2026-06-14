# 35_Workforce_Scheduling — Tables Index

**Total Tables:** 119

| Name                                               | Description |
|----------------------------------------------------|-------------|
| [HTS_CONSOL_CHANGE_EVENTS](Tables/HTS_CONSOL_CHANGE_EVENTS.md) | The table is to store one record for each impacted schedule unit, allowing for efficient tracking and processing of even… |
| [HTS_CONSOL_EVT_SCH_UNIT_USAGES](Tables/HTS_CONSOL_EVT_SCH_UNIT_USAGES.md) | The table is used to track the usage of consolidated event changes for schedule units. |
| [HTS_COVERAGES](Tables/HTS_COVERAGES.md) | Stores the aggregated actual and baseline durations for a schedule. Also stores the aggregate durations for assigned and… |
| [HTS_COVERAGE_DETAILS](Tables/HTS_COVERAGE_DETAILS.md) | Stores the coverage detail records of the workload plan and schedule shift, fully expanded to every 15 minute time slot. |
| [HTS_CUSTOM_SHIFT_TYPES_B](Tables/HTS_CUSTOM_SHIFT_TYPES_B.md) | Table to store Shift related data. |
| [HTS_CUSTOM_SHIFT_TYPES_TL](Tables/HTS_CUSTOM_SHIFT_TYPES_TL.md) | Translation table for Shifts. The table will store attributes for a shift that are translated in different languages. |
| [HTS_EVENT_PROCESSING_QUEUE](Tables/HTS_EVENT_PROCESSING_QUEUE.md) | Table to store the polled events information to be processed. |
| [HTS_GLOBAL_SETUPS_B](Tables/HTS_GLOBAL_SETUPS_B.md) | Base table containing Schedule Global Setup Options used by diffrent schedule apllications. |
| [HTS_GLOBAL_SETUPS_B_](Tables/HTS_GLOBAL_SETUPS_B_.md) | Base table containing Schedule Global Setup Options used by diffrent schedule apllications. |
| [HTS_GLOBAL_SETUPS_TL](Tables/HTS_GLOBAL_SETUPS_TL.md) | Table containing  translatable name and description of  Schedule Global Setup Options. |
| [HTS_GLOBAL_SETUPS_TL_](Tables/HTS_GLOBAL_SETUPS_TL_.md) | Table containing  translatable name and description of  Schedule Global Setup Options. |
| [HTS_ICAL_FEEDS](Tables/HTS_ICAL_FEEDS.md) | Stores the employee calendar feed preferences, along with feed security properties, rate limiting settings etc. |
| [HTS_ICAL_FEED_ACCESS](Tables/HTS_ICAL_FEED_ACCESS.md) | Stores the employee calendar feed access times |
| [HTS_LABOR_DEMAND_DEFS](Tables/HTS_LABOR_DEMAND_DEFS.md) | Table containing the types of labor demand , determined by their unit and time step. Labor demand is a criteria for sche… |
| [HTS_LABOR_DEMAND_PRFL_DEFS](Tables/HTS_LABOR_DEMAND_PRFL_DEFS.md) | labor demand instances defined for a scheduler profile |
| [HTS_LABOR_DEMAND_PRFL_DEFSETS](Tables/HTS_LABOR_DEMAND_PRFL_DEFSETS.md) | Set of demand profile definitions, for a given scheduler profile |
| [HTS_LABOR_DEMAND_PRFL_VALS](Tables/HTS_LABOR_DEMAND_PRFL_VALS.md) | Labor demand profile values, used to define default values for a given scheduler profile and the related demand |
| [HTS_LABOR_DEMAND_VALS](Tables/HTS_LABOR_DEMAND_VALS.md) | Values of the labor demand for the associated scheduler profile |
| [HTS_MSGS](Tables/HTS_MSGS.md) | Information associated with a messages related to internalization of imported shifts. |
| [HTS_MSGS_TKNS](Tables/HTS_MSGS_TKNS.md) | Specific detail to use within a message associated with validation or execution on intenalization of shifts imported. |
| [HTS_SCHEDULES](Tables/HTS_SCHEDULES.md) | Table holding the schedule information of schedule units. |
| [HTS_SCHEDULES_](Tables/HTS_SCHEDULES_.md) | Table holding the schedule information of schedule units. |
| [HTS_SCHEDULE_GEN_PROFILES_B](Tables/HTS_SCHEDULE_GEN_PROFILES_B.md) | Base table containing schedule generation profile information used to generate schedules. |
| [HTS_SCHEDULE_GEN_PROFILES_B_](Tables/HTS_SCHEDULE_GEN_PROFILES_B_.md) | Base table containing schedule generation profile information used to generate schedules. |
| [HTS_SCHEDULE_GEN_PROFILES_TL](Tables/HTS_SCHEDULE_GEN_PROFILES_TL.md) | Table containing  translatable name and description of Schedule Generation Profiles. |
| [HTS_SCHEDULE_GEN_PROFILES_TL_](Tables/HTS_SCHEDULE_GEN_PROFILES_TL_.md) | Table containing  translatable name and description of Schedule Generation Profiles. |
| [HTS_SCHEDULE_GROUPS](Tables/HTS_SCHEDULE_GROUPS.md) | Table holding scheduling groups data which are used for self scheduling. |
| [HTS_SCHEDULE_GROUP_WORKERS](Tables/HTS_SCHEDULE_GROUP_WORKERS.md) | Table holding scheduling group worker's data. |
| [HTS_SCHEDULE_PROCESSES](Tables/HTS_SCHEDULE_PROCESSES.md) | table to store master information of schedule process |
| [HTS_SCHEDULE_SHIFTS](Tables/HTS_SCHEDULE_SHIFTS.md) | Table holding the shifts scheduled for employees. |
| [HTS_SCHEDULE_SHIFTS_](Tables/HTS_SCHEDULE_SHIFTS_.md) | Table holding the shifts scheduled for employees. |
| [HTS_SCHEDULE_SHIFT_DETAILS](Tables/HTS_SCHEDULE_SHIFT_DETAILS.md) | Table holding the detailed information about the shifts scheduled for employees within a department or an unit. |
| [HTS_SCHEDULE_SHIFT_DETAILS_](Tables/HTS_SCHEDULE_SHIFT_DETAILS_.md) | Table holding the detailed information about the shifts scheduled for employees within a department or an unit. |
| [HTS_SCHEDULE_TASKS](Tables/HTS_SCHEDULE_TASKS.md) | This table is used to track the ESS jobs submitted from application and manage auto resubmit on failure if task allows. |
| [HTS_SCHEDULE_TASK_PARAMS](Tables/HTS_SCHEDULE_TASK_PARAMS.md) | This table stores the parameter related to tasks in the hts_schedule_tasks table. |
| [HTS_SCHEDULE_UNIT_PROCESSES](Tables/HTS_SCHEDULE_UNIT_PROCESSES.md) | table to store schedule unit process information |
| [HTS_SCHED_EVENTS](Tables/HTS_SCHED_EVENTS.md) | Table to store schedule events during import schedule process |
| [HTS_SCHED_EVENTS_ESS_PROCESS](Tables/HTS_SCHED_EVENTS_ESS_PROCESS.md) | Table to track the status of the Schedule events ESS Process per Integrators. |
| [HTS_SCHED_FULL_VALIDATIONS](Tables/HTS_SCHED_FULL_VALIDATIONS.md) | This table embodies the schedule validation execution and acts as a parent/root for the KPIs and schedule violation deta… |
| [HTS_SCHED_KPIS](Tables/HTS_SCHED_KPIS.md) | This table is dedicated to the KPI that were calculated during a schedule validation execution. |
| [HTS_SCHED_PROCESSES](Tables/HTS_SCHED_PROCESSES.md) | Schedules processes submitted as asynchronous batch requests |
| [HTS_SCHED_PROCESS_PARAMS](Tables/HTS_SCHED_PROCESS_PARAMS.md) | Schedule batch processes requests functional parameters |
| [HTS_SCHED_PROCESS_PARAM_ITEMS](Tables/HTS_SCHED_PROCESS_PARAM_ITEMS.md) | Schedule batch processes requests functional parameters: element of a sub-process group |
| [HTS_SCHED_PROFILE_COV_INTVLS](Tables/HTS_SCHED_PROFILE_COV_INTVLS.md) | Table containing coverage day intervals that are part of the schedule generation. |
| [HTS_SCHED_PROFILE_COV_INTVLS_](Tables/HTS_SCHED_PROFILE_COV_INTVLS_.md) | Table containing coverage day intervals that are part of the schedule generation. |
| [HTS_SCHED_PROFILE_FLOATS](Tables/HTS_SCHED_PROFILE_FLOATS.md) | Table containing list of Float Pool Departments as part of the schedule generation. |
| [HTS_SCHED_PROFILE_FLOATS_](Tables/HTS_SCHED_PROFILE_FLOATS_.md) | Table containing list of Float Pool Departments as part of the schedule generation. |
| [HTS_SCHED_PROFILE_MANAGERS](Tables/HTS_SCHED_PROFILE_MANAGERS.md) | Table containing schedule managers or individuals who have access to schedule generation profile for the schedule genera… |
| [HTS_SCHED_PROFILE_MANAGERS_](Tables/HTS_SCHED_PROFILE_MANAGERS_.md) | Table containing schedule managers or individuals who have access to schedule generation profile for the schedule genera… |
| [HTS_SCHED_PROFILE_OPPOR_GRPS](Tables/HTS_SCHED_PROFILE_OPPOR_GRPS.md) | Table holding Schedule Generation Profile groups for opportunity rotation. |
| [HTS_SCHED_PROFILE_OPPOR_GRPS_](Tables/HTS_SCHED_PROFILE_OPPOR_GRPS_.md) | Table holding Schedule Generation Profile groups for opportunity rotation. |
| [HTS_SCHED_PROFILE_PRSN_FLTRS](Tables/HTS_SCHED_PROFILE_PRSN_FLTRS.md) | Table containing include or excluded list of jobs and positions that are part of the schedule generation. |
| [HTS_SCHED_PROFILE_PRSN_FLTRS_](Tables/HTS_SCHED_PROFILE_PRSN_FLTRS_.md) | Table containing include or excluded list of jobs and positions that are part of the schedule generation. |
| [HTS_SCHED_PROFILE_ROTATIONS](Tables/HTS_SCHED_PROFILE_ROTATIONS.md) | Table holding self-scheduling rotations which are used self-scheduling |
| [HTS_SCHED_PROFILE_ROTATIONS_](Tables/HTS_SCHED_PROFILE_ROTATIONS_.md) | Table holding self-scheduling rotations which are used self-scheduling |
| [HTS_SCHED_PROFILE_RTN_GRPS](Tables/HTS_SCHED_PROFILE_RTN_GRPS.md) | Table holding self-scheduling rotation groups which are used self-scheduling |
| [HTS_SCHED_PROFILE_RTN_GRPS_](Tables/HTS_SCHED_PROFILE_RTN_GRPS_.md) | Table holding self-scheduling rotation groups which are used self-scheduling |
| [HTS_SCHED_PROFILE_RULES](Tables/HTS_SCHED_PROFILE_RULES.md) | Table holding Rules which are to be used for schedule generation |
| [HTS_SCHED_PROFILE_RULES_](Tables/HTS_SCHED_PROFILE_RULES_.md) | Table holding Rules which are to be used for schedule generation |
| [HTS_SCHED_PROFILE_RULE_SETS](Tables/HTS_SCHED_PROFILE_RULE_SETS.md) | Table holding Rule Sets which are to be used for schedule generation |
| [HTS_SCHED_PROFILE_RULE_SETS_](Tables/HTS_SCHED_PROFILE_RULE_SETS_.md) | Table holding Rule Sets which are to be used for schedule generation |
| [HTS_SCHED_PROFILE_SHIFTS](Tables/HTS_SCHED_PROFILE_SHIFTS.md) | Table holding shifts from the shift library which are to be scheduled for the profile |
| [HTS_SCHED_PROFILE_SHIFTS_](Tables/HTS_SCHED_PROFILE_SHIFTS_.md) | Table holding shifts from the shift library which are to be scheduled for the profile |
| [HTS_SCHED_PROFILE_UNITS](Tables/HTS_SCHED_PROFILE_UNITS.md) | Table containing list of departments and locations that defines the group to be staffed as part of the schedule generati… |
| [HTS_SCHED_PROFILE_UNITS_](Tables/HTS_SCHED_PROFILE_UNITS_.md) | Table containing list of departments and locations that defines the group to be staffed as part of the schedule generati… |
| [HTS_SCHED_PROFILE_UNIT_PREFS](Tables/HTS_SCHED_PROFILE_UNIT_PREFS.md) | table to store schedule unit preferences based on schedule generation profile |
| [HTS_SCHED_PROFILE_UNIT_PREFS_](Tables/HTS_SCHED_PROFILE_UNIT_PREFS_.md) | table to store schedule unit preferences based on schedule generation profile |
| [HTS_SCHED_PUBLISH_EVENTS](Tables/HTS_SCHED_PUBLISH_EVENTS.md) | Schedules events indicating schedules changes not yet published |
| [HTS_SCHED_REQUESTS](Tables/HTS_SCHED_REQUESTS.md) | Table to store schedule requests |
| [HTS_SCHED_RESET_EVENTS](Tables/HTS_SCHED_RESET_EVENTS.md) | Schedule events indicating schedule data that needs to be reset. |
| [HTS_SCHED_REVIEWS](Tables/HTS_SCHED_REVIEWS.md) | table to store schedule's review data |
| [HTS_SCHED_SHIFT_ATRBS](Tables/HTS_SCHED_SHIFT_ATRBS.md) | Table to store schedule shift attributes |
| [HTS_SCHED_SHIFT_EVENTS](Tables/HTS_SCHED_SHIFT_EVENTS.md) | Table to store schedule shift events |
| [HTS_SCHED_SHIFT_REQUESTS](Tables/HTS_SCHED_SHIFT_REQUESTS.md) | Table to store the schedule shift requests information. |
| [HTS_SCHED_UNITS](Tables/HTS_SCHED_UNITS.md) | Table containing a unique or distinct list of departments, locations, or other possible scheduling units in the future, … |
| [HTS_SCHED_VIOLATIONS](Tables/HTS_SCHED_VIOLATIONS.md) | This table denotes the schedule violation messages that were raised during schedule validation execution. |
| [HTS_SCHED_VIOLATION_MSG_TKNS](Tables/HTS_SCHED_VIOLATION_MSG_TKNS.md) | This table is associated with a specific violation message and represents the typed message tokens that were used to for… |
| [HTS_SCHED_VIOLATION_OBJ_REFS](Tables/HTS_SCHED_VIOLATION_OBJ_REFS.md) | This table is associated with a specific violation message and represents the objects that contributed to the violation. |
| [HTS_SHIFTS_B](Tables/HTS_SHIFTS_B.md) | Table holding templates for a library shift, shifts can be used to build work patterns. |
| [HTS_SHIFTS_B_](Tables/HTS_SHIFTS_B_.md) | Table holding templates for a library shift, shifts can be used to build work patterns. |
| [HTS_SHIFTS_TL](Tables/HTS_SHIFTS_TL.md) | Translatable name for library shift. Shifts can be used to build work patterns. |
| [HTS_SHIFTS_TL_](Tables/HTS_SHIFTS_TL_.md) | Translatable name for library shift. Shifts can be used to build work patterns. |
| [HTS_SHIFT_NOTIFICATIONS](Tables/HTS_SHIFT_NOTIFICATIONS.md) | Table holding information about shift notification flow and status. |
| [HTS_SHIFT_TYPES_DETAILS](Tables/HTS_SHIFT_TYPES_DETAILS.md) | Shift definition extension to support shift types library in scheduling application |
| [HTS_SKILLS_B](Tables/HTS_SKILLS_B.md) | This table holds the skill information for scheduling, that enables to match a worker with a task. |
| [HTS_SKILLS_TL](Tables/HTS_SKILLS_TL.md) | Skills translatable name and description. |
| [HTS_STAFFING_VOLUMES](Tables/HTS_STAFFING_VOLUMES.md) | Staffing volume items planned to repeat each day inside some date range. |
| [HTS_STAFFING_VOLUMES_](Tables/HTS_STAFFING_VOLUMES_.md) | Staffing volume items planned to repeat each day inside some date range. |
| [HTS_STAFF_GRIDS](Tables/HTS_STAFF_GRIDS.md) | Table holding the Schedule Staffing Grid header information |
| [HTS_STAFF_GRIDS_](Tables/HTS_STAFF_GRIDS_.md) | Table holding the Schedule Staffing Grid header information |
| [HTS_STAFF_GRID_SEGMENTS](Tables/HTS_STAFF_GRID_SEGMENTS.md) | Table holding the Schedule Staffing grid detail segments information for the grid context |
| [HTS_STAFF_GRID_VALUES](Tables/HTS_STAFF_GRID_VALUES.md) | Table holding the Schedule Staffing grid and Dynamic Flex field Values |
| [HTS_STAFF_GRID_VALUES_](Tables/HTS_STAFF_GRID_VALUES_.md) | Table holding the Schedule Staffing grid and Dynamic Flex field Values |
| [HTS_STAFF_PLANS](Tables/HTS_STAFF_PLANS.md) | Table holding the Schedule Staffing Plan for the Staffing matrix |
| [HTS_STAFF_PLANS_](Tables/HTS_STAFF_PLANS_.md) | Table holding the Schedule Staffing Plan for the Staffing matrix |
| [HTS_STAFF_PLAN_GRIDS](Tables/HTS_STAFF_PLAN_GRIDS.md) | Table holding the Schedule Staffing grid Day of week and grid segment detail definitions |
| [HTS_STAFF_PLAN_GRIDS_](Tables/HTS_STAFF_PLAN_GRIDS_.md) | Table holding the Schedule Staffing grid Day of week and grid segment detail definitions |
| [HTS_STAFF_PLAN_GRID_CONFIGS](Tables/HTS_STAFF_PLAN_GRID_CONFIGS.md) | Table holding the Schedule Staffing Plan configuration used in the Staffing grids |
| [HTS_STAFF_PLAN_GRID_CONFIGS_](Tables/HTS_STAFF_PLAN_GRID_CONFIGS_.md) | Table holding the Schedule Staffing Plan configuration used in the Staffing grids |
| [HTS_STAFF_PLAN_JOBS](Tables/HTS_STAFF_PLAN_JOBS.md) | Table holding the Schedule Staffing Plan Jobs used in the Staffing grids |
| [HTS_STAFF_PLAN_JOBS_](Tables/HTS_STAFF_PLAN_JOBS_.md) | Table holding the Schedule Staffing Plan Jobs used in the Staffing grids |
| [HTS_WORKER_AVAILABILITY_PREFS](Tables/HTS_WORKER_AVAILABILITY_PREFS.md) | Table to store the worker availability preferences. |
| [HTS_WORKER_AVAIL_PREF_DETAILS](Tables/HTS_WORKER_AVAIL_PREF_DETAILS.md) | Table to store the worker availability preference details. |
| [HTS_WORKLOADS](Tables/HTS_WORKLOADS.md) | Table to store the detailed value of the Workload demand, resulting from the various existing Workload plans. |
| [HTS_WORKLOAD_PLANS](Tables/HTS_WORKLOAD_PLANS.md) | Workload demand items planned to repeat each day inside some date range. |
| [HTS_WORKLOAD_PLANS_](Tables/HTS_WORKLOAD_PLANS_.md) | Workload demand items planned to repeat each day inside some date range. |
| [HTS_WORK_PATTERNS_B](Tables/HTS_WORK_PATTERNS_B.md) | Table to store the work pattern information. Work patterns will be used to assign to workers. |
| [HTS_WORK_PATTERNS_B_](Tables/HTS_WORK_PATTERNS_B_.md) | Table to store the work pattern information. Work patterns will be used to assign to workers. |
| [HTS_WORK_PATTERNS_TL](Tables/HTS_WORK_PATTERNS_TL.md) | Table to store translatable name of a work pattern |
| [HTS_WORK_PATTERNS_TL_](Tables/HTS_WORK_PATTERNS_TL_.md) | Table to store translatable name of a work pattern |
| [HTS_WORK_PATTERN_ASSIGNMENTS](Tables/HTS_WORK_PATTERN_ASSIGNMENTS.md) | Table to store the work pattern assignment information. |
| [HTS_WORK_PATTERN_ASSIGNMENTS_](Tables/HTS_WORK_PATTERN_ASSIGNMENTS_.md) | Table to store the work pattern assignment information. |
| [HTS_WORK_PATTERN_BREAKS](Tables/HTS_WORK_PATTERN_BREAKS.md) | Table to store the work pattern break information. |
| [HTS_WORK_PATTERN_BREAKS_](Tables/HTS_WORK_PATTERN_BREAKS_.md) | Table to store the work pattern break information. |
| [HTS_WORK_PATTERN_BREAKS_TL](Tables/HTS_WORK_PATTERN_BREAKS_TL.md) | Table to store translatable name of a work pattern break. |
| [HTS_WORK_PATTERN_BREAKS_TL_](Tables/HTS_WORK_PATTERN_BREAKS_TL_.md) | Table to store translatable name of a work pattern break. |
| [HTS_WORK_PATTERN_SHIFTS](Tables/HTS_WORK_PATTERN_SHIFTS.md) | Table to store the work pattern shift information. |
| [HTS_WORK_PATTERN_SHIFTS_](Tables/HTS_WORK_PATTERN_SHIFTS_.md) | Table to store the work pattern shift information. |
| [HTS_WPT_ASSIGNMENT_RULES](Tables/HTS_WPT_ASSIGNMENT_RULES.md) | Table to store the work pattern template assignment rules information |
