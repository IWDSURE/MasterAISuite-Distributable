# 26_Time_and_Labor — Tables Index

**Total Tables:** 35

| Name                                               | Description |
|----------------------------------------------------|-------------|
| [HXT_APRV_TASK_ENTRY_DETAIL](Tables/HXT_APRV_TASK_ENTRY_DETAIL.md) | This table stores all the entry level details of the time card and approvals |
| [HXT_APRV_TXN_DETAILS](Tables/HXT_APRV_TXN_DETAILS.md) | This table has all entries keyed by the approval record group header |
| [HXT_APRV_TXN_HEADER](Tables/HXT_APRV_TXN_HEADER.md) | Approval record group records for approval |
| [HXT_CHANGE_REQ_APRV_DTL](Tables/HXT_CHANGE_REQ_APRV_DTL.md) | This table has all the changes linked to a Change Request along with the attributes. |
| [HXT_GEOFENCES_B](Tables/HXT_GEOFENCES_B.md) | The hxt_geofence_b table stores the geofence information such as geofence code, location, geoJSON for geofence. Geofence… |
| [HXT_GEOFENCES_TL](Tables/HXT_GEOFENCES_TL.md) | The hxt_geofences_tl table is translation table for the hxt_geofences_b table to store transaltable data such geofence n… |
| [HXT_GEOFENCE_ASSIGNMENTS](Tables/HXT_GEOFENCE_ASSIGNMENTS.md) | Stores geofences assigned to workers using HCM groups. |
| [HXT_GE_PROCESSES](Tables/HXT_GE_PROCESSES.md) | The Input values collected from the UI to generate Time Cards, Time Entries and Time Events. |
| [HXT_GE_PROCESS_PARAMS](Tables/HXT_GE_PROCESS_PARAMS.md) | The Input values collected from the UI to generate Time Entries. The Time Attributes and their Values that are selected … |
| [HXT_SERIALIZED_LAYOUTS](Tables/HXT_SERIALIZED_LAYOUTS.md) | This table is to store the serialized object of layout information |
| [HXT_SERIALIZED_TCLAYFLD_DEFNS](Tables/HXT_SERIALIZED_TCLAYFLD_DEFNS.md) | This table is to store the serialized object of TCF information |
| [HXT_SETUP_EXTRA_INFO_F](Tables/HXT_SETUP_EXTRA_INFO_F.md) | A table to hold additional data for Setup Profiles. |
| [HXT_SETUP_OPTION_VALS](Tables/HXT_SETUP_OPTION_VALS.md) | This table holds the setup option values |
| [HXT_SETUP_PROFILES_B](Tables/HXT_SETUP_PROFILES_B.md) | A base table that holds Setup Profiles. |
| [HXT_SETUP_PROFILES_TL](Tables/HXT_SETUP_PROFILES_TL.md) | Translation table for HXT_SETUP_PROFILES_B. |
| [HXT_SETUP_PROFILE_ASGS](Tables/HXT_SETUP_PROFILE_ASGS.md) | Table that holds profile assignments |
| [HXT_TCLAYFLD_CXT_DEPT](Tables/HXT_TCLAYFLD_CXT_DEPT.md) | The table HXT_TCLAYFLD_CXT_DEPT table contains the values of the parent LC when the dependent LC should be enabled. This… |
| [HXT_TCLAYFLD_DEFNS_B](Tables/HXT_TCLAYFLD_DEFNS_B.md) | The table HXT_TCLAYFLD_DEFNS_B table contains the definition of each layout field which can be later associated to a lay… |
| [HXT_TCLAYFLD_DEFNS_TL](Tables/HXT_TCLAYFLD_DEFNS_TL.md) | Translation table for HXT_TCLAYFLD_DEFNS_B. |
| [HXT_TCLAYFLD_USGS](Tables/HXT_TCLAYFLD_USGS.md) | The table HXT_TCLAYFLD_USGS contains the usage mapping of layout fields in layout sets. |
| [HXT_TCLAYSET_TAF](Tables/HXT_TCLAYSET_TAF.md) | The table HXT_TCLAYST_TAF table contains the list of time repository attributes that are supported by a given layout set… |
| [HXT_TCLAYST_B](Tables/HXT_TCLAYST_B.md) | The table HXT_TCLAYST_B table contains the definition of each layout set that can be assigned to a set of workers throug… |
| [HXT_TCLAYST_PROP](Tables/HXT_TCLAYST_PROP.md) | The table HXT_TCLAYST_PROP table contains the additional properties of layout sets, such as layout set type, audit requi… |
| [HXT_TCLAYST_TL](Tables/HXT_TCLAYST_TL.md) | The translation table for HXT_CLAYST_B. |
| [HXT_TCLAY_B](Tables/HXT_TCLAY_B.md) | The table HXT_TCLAY_B table contains the list of all possible timecard layouts to be displayed for workers.  Examples ar… |
| [HXT_TM_COL_ATTR_MAP](Tables/HXT_TM_COL_ATTR_MAP.md) | The table contains the mapping between the data dictionary attribute to the columns of the timecard UI tables.  The cons… |
| [HXT_TM_HEADER](Tables/HXT_TM_HEADER.md) | This table represents the timecard header available in the Webentry Timecard UI. It will hold all the header level infor… |
| [HXT_TM_MTRX](Tables/HXT_TM_MTRX.md) | This is the table which represents the building blocks of a timecard MTRX row. This doesn't include the additional row a… |
| [HXT_TM_MTRX_DLY_ATRS](Tables/HXT_TM_MTRX_DLY_ATRS.md) | This table will contain the timecard attributes for each additional detail entry in the HXT_TM_MTRX_DLY_ATR_LNKS table. … |
| [HXT_TM_MTRX_DLY_ATR_LNKS](Tables/HXT_TM_MTRX_DLY_ATR_LNKS.md) | This table contains the additional detail entries for the timecard which are mapped against each detail entry. We will l… |
| [HXT_TM_MTRX_DTL_ATRS](Tables/HXT_TM_MTRX_DTL_ATRS.md) | This table is designed to store the reverse orientation of data stored in HXT_TM_MTRX_DLY_ATRS to allow configuration on… |
| [HXT_TM_MTRX_ROW_AD_ATRS](Tables/HXT_TM_MTRX_ROW_AD_ATRS.md) | This table would have the additional row level attributes for each timecard MTRX row. We will have 1..1 association betw… |
| [HXT_TM_MTRX_TBB_USGS](Tables/HXT_TM_MTRX_TBB_USGS.md) | Interface table between UI Time Entries Table (HXT_TM_MTRX) and Time Building Blocks Table (HXT_TM_BLDG_BLKS). |
| [HXT_WC_ATTR_VALS](Tables/HXT_WC_ATTR_VALS.md) | This table is for storing the timecard attribute and its value assosicated with the punches of webclock |
| [HXT_WC_CLICKED_TIMES](Tables/HXT_WC_CLICKED_TIMES.md) | This table stores web clock events and time information clicked by users |
