# HNS_VEH_INC_EVENT_DETAIL

HNS_VEH_INC_EVENT_DETAIL. This table stores vehicle incident event (Driver and Vehicle/ Pedestrian or Bicyclist/Animal or Fixed Object) related data.

## Details

**Schema:** FUSION

**Object owner:** HNS

**Object type:** TABLE

**Tablespace:** TRANSACTION_TABLES

**Source:** [https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hnsvehinceventdetail-25576.html#hnsvehinceventdetail-25576](https://docs.oracle.com/en/cloud/saas/human-resources/oedmh/hnsvehinceventdetail-25576.html#hnsvehinceventdetail-25576)

## Primary Key

| Name | Columns |
|------|----------|
| HNS_VEH_INC_EVENT_DETAIL_PK | VEH_INC_EVT_DETAIL_ID |

## Columns

| Name | Datatype | Length | Precision | Not-null | Comments | Status |
|---|---|---|---|---|---|---|
| VEH_INC_EVT_DETAIL_ID | NUMBER |  | 18 | Yes | VEH_INC_EVT_DETAIL_ID unique identifier. Primary key for HNS_VEH_INC_EVENT_DETAIL table. | Active |
| INCIDENT_DETAIL_ID | NUMBER |  | 18 | Yes | Incident Detail identifier. Foreign key for HNS_INCIDENTS_DETAIL table. |  |
| VEH_INC_EVT_SUMMARY_ID | NUMBER |  | 18 |  | VEH_INC_EVT_SUMMARY_ID. Foreign key for HNS_VEH_INC_EVENT_SUMMARY table. |  |
| VEHICLE_CLASSIFICATION_CODE | VARCHAR2 | 30 |  | Yes | Classification of Vehicle Incident Event.Lookup from FND_LOOKUP.ORA_HNS_VEH_EVT_CLASS_CODE. | Active |
| COMPANY_VEHICLE_FLAG | VARCHAR2 | 1 |  |  | Is this a Company Vehicle. Lookup from FND_LOOKUP.YES_NO. | Active |
| VEHICLE_VIN_NUM | VARCHAR2 | 17 |  |  | VEHICLE_VIN_NUM column : Vehicle Identification Number. | Active |
| VEHICLE_LICENSE_PLATE_NUM | VARCHAR2 | 17 |  |  | VEHICLE_LICENSE_PLATE_NUM column : Vehicle License Plate Number. | Active |
| VEHICLE_COMPANY_ID_NUM | VARCHAR2 | 100 |  |  | VEHICLE_COMPANY_ID_NUM column : Company ID Number If the Company Vehicle flag is Yes. | Active |
| VEHICLE_REGISTRATION_COUNTRY | VARCHAR2 | 100 |  |  | Registration country of the vehicle. | Active |
| VEHICLE_REGISTRATION_STATE | VARCHAR2 | 100 |  |  | Registration state of the vehicle. | Active |
| VEHICLE_MAKE | VARCHAR2 | 100 |  |  | Manufacturer of the vehicle. | Active |
| VEHICLE_MODEL | VARCHAR2 | 100 |  |  | Model of the vehicle. | Active |
| VEHICLE_MODEL_YEAR | NUMBER |  |  |  | Model year of the vehicle. | Active |
| VEHICLE_BODY_TYPE | VARCHAR2 | 100 |  |  | VEHICLE_BODY_TYPE: vehicle body type (eg VAN).Lookup from FND_LOOKUP.ORA_HNS_VEHICLE_BODY_TYPE | Active |
| VEHICLE_GROSS_WEIGHT | NUMBER |  |  |  | VEHICLE_GROSS_WEIGHT: Gross Vehicle Weight. | Active |
| VEHICLE_WEIGHT_UNIT_CD | VARCHAR2 | 30 |  |  | Unit of measurement for Gross Vehicle Weight.Lookup from FND_LOOKUP.ORA_HNS_GVW_UOM | Active |
| VEHICLE_REGISTERED_FLAG | VARCHAR2 | 1 |  |  | VEHICLE_REGISTERED_FLAG: Registered Vehicle (eg USDOT).Lookup from FND_LOOKUP.YES_NO. | Active |
| VEHICLE_REGISTRATION_NUM | VARCHAR2 | 100 |  |  | Registration Number of the Vehicle. | Active |
| VEHICLE_POSITION_CODE | VARCHAR2 | 30 |  |  | Position code of Vehicle at Time of Accident. Lookup from FND_LOOKUP.ORA_HNS_VEH_POS. | Active |
| VEHICLE_MOVEMENT_CODE | VARCHAR2 | 30 |  |  | Vehicle Movement code. Lookup from FND_LOOKUP.ORA_HNS_VEH_MOV. | Active |
| VEHICLE_AREA_IMPACT_CODE | VARCHAR2 | 30 |  |  | Area of Vehicle Receiving First Impact. Lookup from FND_LOOKUP.ORA_HNS_IMPACT_LOC. | Active |
| VEHICLE_TOWED_FLAG | VARCHAR2 | 1 |  |  | Is Vehicle Towed from Scene. Lookup from FND_LOOKUP.YES_NO. | Active |
| TOWING_COMPANY_CONTACT_DETAIL | VARCHAR2 | 4000 |  |  | Towing Company Contact Details. | Active |
| DAMAGE_DESCR | VARCHAR2 | 4000 |  |  | Description of the Damage(Vehicle/Animal or fixed object). | Active |
| VEHICLE_HAS_AIRBAG_FLAG | VARCHAR2 | 1 |  |  | Airbag in vehicle. Lookup from FND_LOOKUP.YES_NO. | Active |
| AIRBAG_DEPLOYED_FLAG | VARCHAR2 | 1 |  |  | Airbag deployed Flag. Lookup from FND_LOOKUP.YES_NO. | Active |
| VEHICLE_SPEED | NUMBER |  |  |  | Vehicle Speed. | Active |
| VEHICLE_SPEED_UNIT_CD | VARCHAR2 | 30 |  |  | Unit of measurement for Vehicle Speed. Lookup from FND_LOOKUP.ORA_HNS_SPEED_UOM. | Active |
| PERSON_TYPE_CODE | VARCHAR2 | 30 |  |  | Person type. Lookup from FND_LOOKUP.ORA_HNS_PERSON. | Active |
| EMPLOYEE_ID | NUMBER |  | 18 |  | Employee ID of the Employee. This column will be blank if the person type is non employee. | Active |
| EMPLOYEE_ASSIGN_ID | NUMBER |  | 18 |  | Employee Assign ID of the Employee. This column will be blank if the person type is non employee. | Active |
| NON_EMP_NAME | VARCHAR2 | 200 |  |  | Non employee name (Vehicle Driver/Pedestrian or Bicyclist/Animal or Fixed object Owner). | Active |
| NON_EMP_EMAIL | VARCHAR2 | 250 |  |  | The email ID of the person (Non employee: Vehicle Driver/Pedestrian or Bicyclist/Animal or Fixed object Owner). | Active |
| PHONE_COUNTRY_CODE_NUM | VARCHAR2 | 30 |  |  | Country code of the non employee(Vehicle Driver/Pedestrian or Bicyclist/Animal or Fixed object Owner) phone number. | Active |
| PHONE_AREA_CODE | VARCHAR2 | 30 |  |  | Area code of the non employee (Vehicle Driver/Pedestrian or Bicyclist/Animal or Fixed object Owner) phone number. | Active |
| PHONE_NUM | VARCHAR2 | 18 |  |  | The phone number of the non employee (Vehicle Driver/Pedestrian or Bicyclist/Animal or Fixed object Owner). | Active |
| NON_EMP_ADDR_LINE1 | VARCHAR2 | 255 |  |  | Address Line1 of the non employee (Vehicle Driver/Pedestrian or Bicyclist/Animal or Fixed object Owner). | Active |
| NON_EMP_ADDR_LINE2 | VARCHAR2 | 255 |  |  | Address Line2 of the non employee (Vehicle Driver/Pedestrian or Bicyclist/Animal or Fixed object Owner). | Active |
| NON_EMP_ADDR_CITY | VARCHAR2 | 100 |  |  | Address city of the non employee (Vehicle Driver/Pedestrian or Bicyclist/Animal or Fixed object Owner). | Active |
| NON_EMP_ADDR_STATE | VARCHAR2 | 100 |  |  | Address State of the non employee (Vehicle Driver/Pedestrian or Bicyclist/Animal or Fixed object Owner). | Active |
| NON_EMP_ADDR_ZIP_CODE | VARCHAR2 | 100 |  |  | Address Zip code of the non employee (Vehicle Driver/Pedestrian or Bicyclist/Animal or Fixed object Owner). | Active |
| NON_EMP_ADDR_COUNTRY | VARCHAR2 | 100 |  |  | Address Country of the non employee (Vehicle Driver/Pedestrian or Bicyclist/Animal or Fixed object Owner). | Active |
| VEHICLE_DRIVERS_LICENSE_NUM | VARCHAR2 | 100 |  |  | VEHICLE_DRIVERS_LICENSE_NUM column : Drivers License Number. | Active |
| DRIVERS_LICENSE_EXP_DATE | TIMESTAMP |  |  |  | DRIVERS_LICENSE_EXP_DATE column : Drivers License Date of Expiration. | Active |
| STATE_ISSUED_DRIVERS_LICENSE | VARCHAR2 | 100 |  |  | State Issued Drivers License. | Active |
| VEHICLE_DRIVER_LOCATION_CODE | VARCHAR2 | 30 |  |  | VEHICLE_DRIVER_LOCATION_CODE column : Driver Location at Time of Accident. Lookup from FND_LOOKUP.ORA_HNS_DRIVER_LOC. |  |
| INJURED_FLAG | VARCHAR2 | 1 |  |  | Injured Flag. Lookup from FND_LOOKUP.YES_NO. | Active |
| TAKEN_TO_HOSPITAL_FLAG | VARCHAR2 | 1 |  |  | Taken to Hospital Flag. Lookup from FND_LOOKUP.YES_NO. | Active |
| FATALITY_FLAG | VARCHAR2 | 1 |  |  | Fatality Flag. Lookup from FND_LOOKUP.YES_NO. | Active |
| CELL_PHONE_IN_USE_FLAG | VARCHAR2 | 1 |  |  | Cell Phone In Use Flag. Lookup from FND_LOOKUP.YES_NO. | Active |
| COMPUTER_IN_USE_FLAG | VARCHAR2 | 1 |  |  | Computer In Use Flag. Lookup from FND_LOOKUP.YES_NO. | Active |
| SEAT_BELT_IN_USE_FLAG | VARCHAR2 | 1 |  |  | Seat Belt in Use by Driver Flag. Lookup from FND_LOOKUP.YES_NO. | Active |
| ALCOHOL_TEST_PERFORM_FLAG | VARCHAR2 | 1 |  |  | Alcohol Test Performed Flag. Lookup from FND_LOOKUP.YES_NO. | Active |
| DRUG_TEST_PERFORM_FLAG | VARCHAR2 | 1 |  |  | Drug Test Performed Flag. Lookup from FND_LOOKUP.YES_NO. | Active |
| VEHICLE_HAS_PASSENGER_FLAG | VARCHAR2 | 1 |  |  | This column signifies whether there are any passenger(s) present in the Vehicle at the time of the event. Lookup from FND_LOOKUP.YES_NO. | Active |
| DELETED_FLAG | VARCHAR2 | 1 |  |  | Deleted flag.This column signifies whether the Vehicle incident event is checked for deletion. | Active |
| CREATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who created the row. | Active |
| CREATION_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the creation of the row. | Active |
| LAST_UPDATED_BY | VARCHAR2 | 64 |  | Yes | Who column: indicates the user who last updated the row. | Active |
| LAST_UPDATE_DATE | TIMESTAMP |  |  | Yes | Who column: indicates the date and time of the last update of the row. | Active |
| LAST_UPDATE_LOGIN | VARCHAR2 | 32 |  |  | Who column: indicates the session login associated to the user who last updated the row. | Active |
| OBJECT_VERSION_NUMBER | NUMBER |  | 9 | Yes | Used to implement optimistic locking. This number is incremented every time that the row is updated. The number is compared at the start and end of a transaction to detect whether another session has updated the row since it was queried. | Active |
| ATTRIBUTE_CATEGORY | VARCHAR2 | 30 |  |  | Descriptive Flexfield: structure definition of the user descriptive flexfield. |  |
| ATTRIBUTE1 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE2 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE3 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE4 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE5 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE6 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE7 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE8 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE9 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE10 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE11 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE12 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE13 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE14 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE15 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE16 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE17 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE18 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE19 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE20 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE21 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE22 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE23 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE24 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE25 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE26 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE27 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE28 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE29 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE30 | VARCHAR2 | 150 |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_NUMBER1 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_NUMBER2 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_NUMBER3 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_NUMBER4 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_NUMBER5 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_NUMBER6 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_NUMBER7 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_NUMBER8 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_NUMBER9 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_NUMBER10 | NUMBER |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_TIMESTAMP1 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_TIMESTAMP2 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_TIMESTAMP3 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_TIMESTAMP4 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_TIMESTAMP5 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_TIMESTAMP6 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_TIMESTAMP7 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_TIMESTAMP8 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_TIMESTAMP9 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| ATTRIBUTE_TIMESTAMP10 | TIMESTAMP |  |  |  | Descriptive Flexfield: segment of the user descriptive flexfield. |  |
| RELATED_COMPANY_FLG | VARCHAR2 | 1 |  |  | is this a related company Lookup from FND_LOOKUP.YES_NO. |  |
| RELATED_COMPNAY_ID | NUMBER |  | 18 |  | Legal Entity ID |  |
| CONTACT_ID | NUMBER |  | 18 |  | Employee ID for contact name |  |
| OWNER_NAME | VARCHAR2 | 200 |  |  | Company name that owns the vehicle |  |
| COMPANY_ADDR_LINE1 | VARCHAR2 | 225 |  |  | Address line 1 for non related company |  |
| COMPANY_ADDR_LINE2 | VARCHAR2 | 225 |  |  | Address line 2 for non related company |  |
| COMPANY_ADDR_CITY | VARCHAR2 | 100 |  |  | Address city for non related company |  |
| COMPANY_ADDR_STATE | VARCHAR2 | 100 |  |  | Address state for non reated company |  |
| COMPANY_ADDR_ZIP_CODE | VARCHAR2 | 100 |  |  | Address zip code for non reated company |  |
| COMPANY_ADDR_COUNTRY | VARCHAR2 | 100 |  |  | Address country for non reated company |  |
| FLEET_VEHICLE_FLG | VARCHAR2 | 1 |  |  | is this a fleet vehicle Lookup from FND_LOOKUP.YES_NO. |  |
| VEHICLE_DESCRIPTION | VARCHAR2 | 200 |  |  | Fleet vehicle descirption |  |
| REGISTRATION_DATE | TIMESTAMP |  |  |  | Registered vehicle registration date |  |
| WAS_RENTAL_FLAG | VARCHAR2 | 1 |  |  | is this a rental vehicle Lookup from FND_LOOKUP.YES_NO. |  |
| RENTAL_COMPANY_NAME | VARCHAR2 | 200 |  |  | Rental company name for rental vehicle |  |
| RENTAL_LOCATION | VARCHAR2 | 4000 |  |  | Rental location |  |
| COST_OF_RENTAL_VEHICLE | VARCHAR2 | 20 |  |  | Cost of rental vehicle |  |
| RENTAL_DATE | TIMESTAMP |  |  |  | Rental start date |  |
| RENTAL_AGREEMENT_NUMBER | VARCHAR2 | 100 |  |  | Rental agreement number |  |
| PAID_BY_COMPANY_FLG | VARCHAR2 | 1 |  |  | is this paid by company  Lookup from FND_LOOKUP.YES_NO. |  |
| INSURANCE_ADD_FLG | VARCHAR2 | 1 |  |  | Is insurance added Lookup from FND_LOOKUP.YES_NO. |  |
| RENTAL_VEH_REPLACEMENT_FLG | VARCHAR2 | 1 |  |  | Is this a rental replacement vehicle Lookup from FND_LOOKUP.YES_NO. |  |
| REP_RENTAL_COMPANY_NAME | VARCHAR2 | 200 |  |  | Replacement rental vehicle company name |  |
| REP_RENTAL_LOCATION | VARCHAR2 | 4000 |  |  | Replacement rental vehicle location |  |
| REP_COST_OF_RENTAL_VEHICLE | VARCHAR2 | 20 |  |  | Replacement rental vehicle cost |  |
| REP_RENTAL_DATE | TIMESTAMP |  |  |  | Replacement rental vehicle rental sstart date |  |
| REP_RENTAL_AGREEMENT_NUMBER | VARCHAR2 | 100 |  |  | Replacement rental vehicle agreement number |  |
| REP_PAID_BY_COMPANY_FLG | VARCHAR2 | 1 |  |  | Is this a rental replacement vehicle paid by company Lookup from FND_LOOKUP.YES_NO. |  |
| REP_INSURANCE_ADD_FLG | VARCHAR2 | 1 |  |  | Is this a rental replacement vehicle insurance added Lookup from FND_LOOKUP.YES_NO. |  |
| INSURANCE_INFORMATION_FLG | VARCHAR2 | 1 |  |  | Insurance information Lookup from FND_LOOKUP.YES_NO. |  |
| INSURANCE_COMPANY_NAME | VARCHAR2 | 200 |  |  | Name of the insurance company |  |
| INSURANCE_POLICY_NUMBER | VARCHAR2 | 100 |  |  | Insurance policy number |  |
| EXPIRY_DATE | TIMESTAMP |  |  |  | Insurance expiry date |  |
| CASE_NUMBER | VARCHAR2 | 100 |  |  | Insurance case number |  |
| INSURANCE_AGENT | VARCHAR2 | 200 |  |  | Insurance agent information |  |
| REPAIR_COST | VARCHAR2 | 20 |  |  | Total repair cost |  |
| INS_PHONE_COUNTRY_CODE | VARCHAR2 | 30 |  |  | Insurance phone number country code |  |
| INS_PHONE_AREA_CODE | VARCHAR2 | 30 |  |  | Insurance phone number area code |  |
| INS_PHONE_NUM | VARCHAR2 | 10 |  |  | Insurance Phone number |  |
| INS_EMAIL | VARCHAR2 | 250 |  |  | Insurance email |  |
| PED_DOING_PRIOR_TO_INCIDENT | VARCHAR2 | 4000 |  |  | Description of what pedestrian or bicyclist was doing before incident |  |
| LOCATION_OF_PEDESTRIAN | VARCHAR2 | 4000 |  |  | Description of where the pedestrian or bicylcist prior to incident |  |
| PED_SAFETY_EQUIPMENT | VARCHAR2 | 4000 |  |  | Description of safety equipment that was used by pedestrian or biclyclist |  |
| DESCRIBE_DAMAGE | VARCHAR2 | 4000 |  |  | Description of the damage to pedestrian or bicyclist |  |
| NON_COM_VEH_OWNER_NAME | VARCHAR2 | 200 |  |  | Owner name of non company vehicle |  |
| NON_COM_VEH_CONTACT_NAME | VARCHAR2 | 200 |  |  | Contact name of non company vehicle |  |
| NON_COM_VEH_ADD_LINE1 | VARCHAR2 | 225 |  |  | Address line 1 of non company vehicle |  |
| NON_COM_VEH_ADD_LINE2 | VARCHAR2 | 225 |  |  | Address line 2 of non company vehicle |  |
| NON_COM_VEH_ADD_CITY | VARCHAR2 | 100 |  |  | Address city of non company vehicle |  |
| NON_COM_VEH_ADD_STATE | VARCHAR2 | 100 |  |  | Address state of non company vehicle |  |
| NON_COM_VEH_ADD_ZIP_CODE | VARCHAR2 | 100 |  |  | Address zip code of non company vehicle |  |
| NON_COM_VEH_ADD_COUNTRY | VARCHAR2 | 100 |  |  | Address country of non company vehicle |  |
| NON_REL_COM_VEH_CONTACT_NAME | VARCHAR2 | 200 |  |  | Contact name of non related company vehicle |  |
| NON_COM_VEH_LICENSE_NUM | VARCHAR2 | 17 |  |  | Non company Vehicle license number |  |
| NON_COM_VEH_VIN_NUM | VARCHAR2 | 17 |  |  | Non compnay vehicle identificaiton number |  |
| NON_COM_VEH_REGISTER_FLG | VARCHAR2 | 1 |  |  | Non company vehicle registration flag |  |
| NON_COM_VEH_REGI_NUM | VARCHAR2 | 100 |  |  | Non company vehicle registration number |  |
| NON_COM_VEH_BODY_TYPE | VARCHAR2 | 100 |  |  | Non company vehicle body type |  |
| NON_COM_VEH_REGI_STATE | VARCHAR2 | 100 |  |  | Non company vehicle registration state |  |
| NON_COM_VEH_MAKE | VARCHAR2 | 100 |  |  | Maker of non company vehicle |  |
| NON_COM_VEH_REGI_COUNTRY | VARCHAR2 | 100 |  |  | Non company vehicle registration country |  |
| NON_COM_VEH_MODEL | VARCHAR2 | 100 |  |  | Model of non company vehicle |  |
| NON_COM_VEH_YEAR | NUMBER |  | 5 |  | Year of non company vehicle |  |

## Indexes

| Index | Uniqueness | Tablespace | Columns | Status |
|---|---|---|---|---|
| HNS_VEH_INC_EVENT_DETAIL_N1 | Non Unique | FUSION_TS_TX_IDX | INCIDENT_DETAIL_ID | Active |
| HNS_VEH_INC_EVENT_DETAIL_UK1 | Unique | FUSION_TS_TX_IDX | VEH_INC_EVT_DETAIL_ID | Active |

---

[← Back to Index](../30_Workforce_Health_and_Safety_Incidents_Tables_Index.md)
