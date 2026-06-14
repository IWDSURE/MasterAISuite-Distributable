# HRC_DE_HISTORY_GT

A Global temporary table is used to store the main Date Effective History information at a Session level and is populated when the Date Effective History Main Window is invoked.

## Details

**Schema:** FUSION

**Object owner:** HRC

**Object type:** TABLE

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdehistorygt-16073.html#hrcdehistorygt-16073](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hrcdehistorygt-16073.html#hrcdehistorygt-16073)

## Primary Key

| Name | Columns |
|------|----------|
| HRC_DE_HISTORY_GT_PK | HISTORY_ID |

## Columns

| Name |
|---|
| HISTORY_IDNUMBER18YesSurrogate Primary KeyActive
OBJECT_SURROGATE_KEY_IDNUMBER18YesObject surrogate key id (e.g. Assignment Id)Active
OBJECT_VO_NAMEVARCHAR22000YesDate Effective View Object Name (eg oracle.apps.hcm.employment.EmployeeDVO)Active
EFFECTIVE_START_DATEDATEYesDate Effective Entity: indicates the date at the beginning of the date range within which the row is effective.Active
EFFECTIVE_END_DATEDATEYesDate Effective Entity: indicates the date at the end of the date range within which the row is effective.Active
EFFECTIVE_SEQUENCENUMBER4Date Effective Entity: indicates the order of different changes made during a day. The lowest value represents the earliest change in the day.Active
EFFECTIVE_SEQUENCE_DISPLAYVARCHAR230Holds the Effective Sequence Display Value (e.g. "1 of 4", "2 of 4"). Only set for Multiple Changes Per DayActive
EFFECTIVE_LATEST_CHANGEVARCHAR230Date Effective Entity: 'Y' indicates that this row represents the latest change in the day.Active
CHANGED_ATTRIBUTE_NAMESVARCHAR22000Concatenation of Attribute Names which have changed (e.g Department, Job, Position) etc'Active
CHANGED_ATTRIBUTE_GROUPVARCHAR22000Concatenation of Object Display Name(s)Active
CHANGED_ATTRIBUTE_CONCATVARCHAR22000Concatenation of: CHANGED_ATTRIBUTE_NAMES \|\| CHANGED_ATTRIBUTE_GROUPActive
OBJECT_DISPLAY_NAMEVARCHAR22000YesThe Object Display Name (e.g Employment, Manager, Phone, Address etc)Active
OBJECT_LOGICAL_DISPLAY_IDVARCHAR22000YesThe Object Logical Display  Identifier identifies the logical row name (e.g E000123, John Jones, Regular Salary)Active
PARENT_SURROGATE_KEY_IDNUMBER18Specifies the Parent (which points to OBJECT_SURROGATE_KEY_ID)Active
PARENT_OBJECT_DISPLAY_NAMEVARCHAR22000Specifies the parent object display name (e.g Employment, Manager, Phone, Address etc)Active
ACTION_REASON_MEANINGVARCHAR22000Specifies the HCM Core HR Action Reason MeaningActive
ACTION_MEANINGVARCHAR22000Specifies the HCM Core HR Action MeaningActive
OBJECT_VERSION_NUMBERNUMBER9YesUsed to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried.Active
CREATED_BYVARCHAR264YesWho column: indicates the user who created the row.Active
CREATION_DATETIMESTAMPYesWho column: indicates the date and time of the creation of the row.Active
LAST_UPDATED_BYVARCHAR264YesWho column: indicates the user who last updated the row.Active
LAST_UPDATE_DATETIMESTAMPYesWho column: indicates the date and time of the last update of the row.Active
LAST_UPDATE_LOGINVARCHAR232Who column: indicates the session login associated to the user who last updated the row.Active |

## Indexes

| Index | Uniqueness | Columns |
|---|---|---|
| HRC_DE_HISTORY_GT_U1 | Unique | HISTORY_ID |
| HRC_DE_HISTORY_GT_U2 | Unique | OBJECT_SURROGATE_KEY_ID, EFFECTIVE_START_DATE, EFFECTIVE_END_DATE, OBJECT_VO_NAME, EFFECTIVE_SEQUENCE, EFFECTIVE_LATEST_CHANGE |

---

[← Back to Index](../14_HCM_Common_Tables_Index.md)
