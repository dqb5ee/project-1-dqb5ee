# DS 4320 Project 1: Finding the Arid Edge
### Optimizing Live Fuel Moisture Thresholds for Southern California Wildfire Readiness

**Executive Summary:** This repository contains a data engineering and predictive modeling pipeline designed to identify the "Arid Edge"—the critical Live Fuel Moisture (LFM) threshold at which Southern California landscapes transition from fire-resistant to explosively flammable. By integrating 10,000+ field-collected vegetation samples from the National Fuel Moisture Database with historical CAL FIRE perimeter data, the project transforms raw environmental observations into a normalized relational database using Python and DuckDB. The included analysis optimizes a "Red Line" moisture metric to provide emergency agencies with a stable, biological signal for resource staging, moving beyond the volatility of wind-based alerts to mitigate "alert fatigue" and enhance proactive wildfire suppression in the Wildland-Urban Interface.

**Name:** Avalon Bennett

**NetID:** dqb5ee

**DOI:** [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19340739.svg)](https://doi.org/10.5281/zenodo.19340739)

**Press Release:** [View the "Arid Edge" Announcement](https://github.com/dqb5ee/project-1-dqb5ee/blob/main/pressrelease.md)

**Data:** [OneDrive Folder: Southern California Wildfire & Moisture Data](https://myuva-my.sharepoint.com/:f:/g/personal/dqb5ee_virginia_edu/IgBl82ldBtixSpBs556Z1Z_gARDRne96Iha1X__LFe-_Zz4?e=RagYNQ)

**Pipeline:** [Technical Pipeline & Execution Log](https://github.com/dqb5ee/project-1-dqb5ee/tree/main/pipeline)

**License:** This project is licensed under the [MIT License.](https://github.com/dqb5ee/project-1-dqb5ee/blob/main/License.md)

## Problem Definition

**General Problem:** Predicting Wildfire Risk

**Refined Statement:** Rather than relying on numerous "High Fire Danger" alerts, this project seeks to identify and optimize the "Arid Edge," a.k.a the specific Live Fuel Moisture (LFM) threshold at which a landscape transitions from fire-resistant to explosively flammable. By using machine learning to establish this "Red Line," we can replace more unpredictable, wind-based alerts with a stable, evidence-based signal that allows emergency agencies and residents to move resources into position days before an ignition occurs.


**Rationale for Refinement:** The transition from broad meteorological prediction to threshold optimization is essential for combating "alert fatigue" in Southern California. While wind is a chaotic, short-term trigger, LFM represents the underlying state of the fuel. By focusing on the "Arid Edge," we move away from the messiness of frequent wind warnings that often result in no fire toward a more reliable trigger. This refinement allows us to identify the specific windows where the landscape's "thirst" makes a large fire more statistically probable, making sure that high-stakes warnings are only issued when the data confirms the environment is primed for catastrophe.

**Motivation:** The motivation for this project is the increasing vulnerability of the Wildland-Urban Interface (WUI) and the escalating cost of emergency resource deployment. Current "Red Flag" warnings often trigger massive, expensive mobilizations that may be unnecessary, while missing the subtle environmental drying that leads to "flash fires." By providing a clearer, data-driven "Vision" of danger, this project aims to reduce resident anxiety and improve agency readiness. We are motivated by the goal of giving responders a "Head Start"—shifting the strategy from reactive firefighting to proactive, pre-emptive positioning based on a hard "Red Line" in the moisture data.

**Press Release Headline:** The Arid Edge: New Data Model Identifies the 71% "Danger Zone" for Southern California Wildfires

[**Press Release Link**](https://github.com/dqb5ee/project-1-dqb5ee/blob/main/pressrelease.md)


## Domain Exposition

**Terminology:**

| Category | Term | Definition/Significance | KPI Type |
| :--- | :--- | :--- | :--- |
| **Atmospheric** | **Santa Ana Winds** | Strong, dry downslope winds that act as the primary "Training Load" for fire spread. | **Input Variable** |
| **Atmospheric** | **Vapor Pressure Deficit (VPD)** | Measure of the air's "thirst." High VPD accelerates the drying of live fuels. | **Predictive KPI** |
| **Biological** | **Live Fuel Moisture (LFM)** | Percentage of water content in living chaparral. This is the "Stable Signal" used to predict landscape flammability. | **Primary Biological KPI** |
| **Biological** | **The Arid Edge** | The optimized mathematical threshold where LFM levels indicate a statistically significant jump in catastrophic fire probability. | **Optimization Metric** |
| **Geospatial** | **Wildland-Urban Interface (WUI)** | The high-stakes zone where human infrastructure meets flammable natural vegetation. | **Spatial Metric** |
| **Operational** | **Resource Readiness** | The proactive deployment of fire crews and equipment based on environmental "readiness" rather than reactive triggers. | **Strategic Outcome** |
| **Operational** | **Ignition Window** | The critical intersection of wind, low humidity, and sub-threshold LFM where "flash fires" become probable. | **Primary Output** |
| **Weather** | **Relative Humidity (RH)** | The amount of water vapor in the air; during Santa Ana events, RH often drops into the dangerous single digits. | **Input Variable** |


**Project Domain:** This project lives at the intersection of Environmental Data Science and Public Safety Analytics. Specifically, it focuses on the domain of Wildfire Risk Modeling, a field that integrates meteorology, botany (fuel science), and geospatial physics to predict the behavior of natural disasters. While traditional fire response is reactive, this domain emphasizes pre-emptive risk identification. By analyzing historical fire perimeters against the biological "readiness" (LFM) of the landscape, we can treat Southern California's canyons as a monitored system. This approach allows for a more reliable, "all-sides ready" strategy that reduces resident anxiety and optimizes resource allocation by moving beyond unpredictable wind gusts to focus on the stable, measurable state of the fuel.


**Summary of Background Research:**

| Title | Description | Read More |
| :--- | :--- | :--- |
| **Evidence-Based Decision-Making** | Explores using Big Data in environmental regulation, emphasizing the need for spatial and temporal specificity in policy. | [Link](https://myuva-my.sharepoint.com/:b:/g/personal/dqb5ee_virginia_edu/IQCBQ6nHWnLjTrhf6za_et_XAWejwfEMXCOE8BevK9YGBGU?e=r20q0Z) |
| **Wildfire Risk Modeling** | Comprehensive overview of current methods in risk assessment and the integration of machine learning for prediction. | [Link](https://myuva-my.sharepoint.com/:b:/g/personal/dqb5ee_virginia_edu/IQBoqXBuMrivTbXXJhNvX4WOAYG9whWzdBhyuTGCvz6okQU?e=iIXmEz) |
| **ML Applied to Wildfire Data** | Technical study comparing ML algorithms to predict fires, providing a baseline for our "Arid Edge" model. | [Link](https://myuva-my.sharepoint.com/:b:/g/personal/dqb5ee_virginia_edu/IQCo6B5JLp2bRptp9KyLsjkmAXPGxTAVwKe3bKmVuzw-KBc?e=U91Npk) |
| **Santa Ana Winds & Topography** | Explains how "the atmosphere's thirst" and SoCal topography create the breeding grounds for extreme fire spread. | [Link](https://myuva-my.sharepoint.com/:b:/g/personal/dqb5ee_virginia_edu/IQDLL4CQ7bGeRbykx4sU0wAsAU8Y4_K2MiWLp0QmvXhqMgU?e=y0JwPs) |
| **The Impact of SoCal Fires** | Details the human and socio-economic costs of recent fires, emphasizing the need for better early warning signals. | [Link](https://myuva-my.sharepoint.com/:b:/g/personal/dqb5ee_virginia_edu/IQDMXX1hChvhT7naUOEX9j3kATtIHxhIjPgKEW-5w4sBWuY?e=cdhXYc) |

## Data Creation

**Provenance:** The raw data for this project was synthesized from two primary state-level repositories to correlate environmental conditions with historical wildfire behavior in Southern California. The foundational dataset consists of Live Fuel Moisture (LFM) observations sourced from the National Fuel Moisture Database (NFMD) and the CAL FIRE Vegetation Sampling Program. This data represents field-collected measurements from 28 specific sampling sites across the Southern California coastal range (including Los Angeles, Ventura, and Santa Barbara counties). These measurements are taken by clipping live vegetation (primarily chamise and sage scrub), weighing it before and after oven-drying, and calculating the percentage of water content relative to dry biomass. This dataset provides the physiological "stable signal" necessary to understand the landscape's risk for catastrophic ignition.


To evaluate the impact of these moisture levels on actual disaster events, I acquired the California Historic Wildfire Perimeters (Firep24_1) dataset from the CAL FIRE Fire and Resource Assessment Program (FRAP). This GIS-based dataset contains the spatial boundaries and metadata for all recorded wildfires in California since 1878. By filtering these perimeters for the Southern California units that match the geographic coordinates of the LFM sampling sites, I was able to cross-reference the exact fuel moisture percentage present on the day of major fire ignitions. This dual-source acquisition process allows the project to move beyond unpredictable wind patterns and pinpoint the specific biological thresholds (the Arid Edge) that lead to explosive fire growth and dictate resource deployment needs.


**Code:**

| Primary Source File | Code File & Link | Resulting Relational Entity | Description of Data Creation & Edits |
| :--- | :--- | :--- | :--- |
| `lfmc_observations.csv` | [`process_lfmc.py`](https://github.com/dqb5ee/project-1-dqb5ee/blob/main/code/process_lfmc.py) | `moisture_sites.parquet`, `moisture_readings.parquet` | Normalizes geographic metadata away from field observations to establish a 1:N relational structure. |
| `CA_Fire_Perimeters.csv` | [`filter_fires.py`](https://github.com/dqb5ee/project-1-dqb5ee/blob/main/code/filter_fires.py) | `wildfire_events.parquet` | Merges statewide GIS chunks, filters for Southern California Unit IDs, and deduplicates records. |
| `wildfire_events.parquet` | [`unit_agency.py`](https://github.com/dqb5ee/project-1-dqb5ee/blob/main/code/unit_agency.py) | `unit_agency.parquet` | Extracts unique administrative Unit IDs from fire perimeters to generate a standalone agency reference table. |
| **Relational Entities** | [`correlation_model.py`](https://github.com/dqb5ee/project-1-dqb5ee/blob/main/code/correlation_model.py) | **Analytical View** | Performs a temporal join in DuckDB to correlate historical ignitions with regional moisture baselines for threshold analysis. |

This automated pipeline transforms primary sources into a normalized four-table relational model. By using Python and DuckDB to separate static metadata from time-series events, the project ensures data integrity and high-performance querying for the threshold analysis.


**Bias Identification:** Bias was introduced into the data collection process primarily through spatial selection and reporting thresholds. Live Fuel Moisture (LFM) sampling sites are fixed and often located near accessible roads or fire breaks for technician safety. This roadside bias means the data captures vegetation exposed to different micro-climates, such as asphalt heat reflection, rather than interior canyon brush. Additionally, site distribution is heavily weighted toward the Wildland-Urban Interface (WUI), making the model more accurate for populated canyons than remote wilderness. Furthermore, the CAL FIRE perimeter data was acquired in discrete GIS chunks, necessitating a manual merge that could introduce reconciliation bias if duplicate events aren't perfectly filtered. Finally, by focusing on fires over 10,000 acres, a success bias is introduced; the model identifies the threshold for catastrophic spread rather than simple ignition, meaning it does not account for the thousands of small starts that fail to spread, which are still critical for localized safety.


**Bias Mitigation:** To ensure the "Arid Edge" is a reliable predictor, the analysis uses statistical aggregation and relational normalization to account for identified biases. To mitigate roadside bias and non-uniform sensor distribution, the model implements a regional monthly baseline in DuckDB that aggregates data from 28 distinct sites. This smoothing process prevents localized micro-climate anomalies from individual sensors from skewing the broader landscape representation. The analysis handles success bias by using a 10,000-acre filter, which intentionally shifts the study from simple ignition to suppression-resistant spread. This allows the model to quantify the specific conditions where fuel moisture is low enough to render standard fire suppression ineffective. Lastly, the temporal lag between field samples is mitigated by aligning ignitions with regional trends, ensuring the model captures the overall landscape "thirst" rather than relying on potentially outdated discrete samples.


**Rationale:** The model is built on prioritizing public safety and resource readiness over spatial precision. A major judgment call was setting the 75% moisture threshold, a more conservative "early warning" limit than the standard 60% critical state. While this increases the potential for false positives, it ensures the model identifies the onset of the ignition window, providing a reliable signal for agencies to stage resources before wind events escalate. Similarly, the decision to use a regional monthly baseline mitigates the high uncertainty associated with localized sensors. This assumes that fire risk is a landscape-level phenomenon requiring a stable, regional signal for effective decision-making. Finally, the use of a 10,000-acre filter intentionally isolates uncontrollable fire behavior, removing the "noise" of varying fire department response times to focus exclusively on the biological conditions—the Arid Edge—that allow for catastrophic spread.

## Metadata

**Schema:**
<img width="3994" height="229" alt="Blank diagram - Page 1 Wildfire Threshold Analysis ERD" src="https://github.com/user-attachments/assets/c5284c86-7d13-4ff2-9b85-d21805e2082e" />

The relationship between `Moisture_Reading` and `Wildfire_Event` is a temporal join based on the `Date` and `Alarm_Date` fields. Because environmental monitoring data lacks a shared unique ID with event-based GIS data, the logical model correlates these entities by matching fire ignition timestamps to the corresponding monthly regional fuel moisture baseline.

**Data:**

| Table Name | Entity Represented | Description | Link to Parquet File |
| :--- | :--- | :--- | :--- |
| `moisture_sites.parquet` | **Moisture_Site** | Metadata for 28 unique sampling stations (ID, County, Vegetation Type). Serves as the geographic anchor. | [Link](https://myuva-my.sharepoint.com/:u:/g/personal/dqb5ee_virginia_edu/IQApHxYTh5T1Qbdg1_V3WSFWAc56aVFT8zrQi8qli8uzgyc?e=hUXc0C) |
| `moisture_readings.parquet` | **Moisture_Reading** | 10,000+ field records containing bi-weekly vegetation water content samples tied to Site IDs. | [Link](https://myuva-my.sharepoint.com/:u:/g/personal/dqb5ee_virginia_edu/IQBpfwrjcvAHRYYWt00Xqgd4AdfmIvldaZQDy-hXM3F45k0?e=F2Dk4o) |
| `wildfire_events.parquet` | **Wildfire_Event** | Unified Southern California GIS records (>10k acres) created by merging and deduplicating raw state-wide chunks. | [Link](https://myuva-my.sharepoint.com/:u:/g/personal/dqb5ee_virginia_edu/IQBZ-lmKGjJiTJP-ice15ZedAcZj-y7n-YkXPbybJ5tO_0E?e=5j7sdh) |
| `unit_agency.parquet` | **Unit_Agency** | Administrative metadata for the responding fire departments (VNC, LAC, BDU, etc.) used for regional categorization. | [Link](https://myuva-my.sharepoint.com/:u:/g/personal/dqb5ee_virginia_edu/IQAdw469qcP1Sp7UERy-UzdRAZ6BinvJ5EI_uNDFA6RZDck?e=KYSkoN) |


**Data Dictionary:**

| Feature Name | Data Type | Description | Example | Entity / Table |
| :--- | :--- | :--- | :--- | :--- |
| `Site_ID` | String (PK) | Unique identifier for the sampling station. | "MALIBU_01" | **Moisture_Site** |
| `Site_Name` | String | Common name of the geographic location. | "Malibu Canyon" | **Moisture_Site** |
| `County` | String | Southern California county of origin. | "Los Angeles" | **Moisture_Site** |
| `Latitude` | Float | Geographic coordinate (North/South). | 34.079 | **Moisture_Site** |
| `Longitude` | Float | Geographic coordinate (East/West). | -118.694 | **Moisture_Site** |
| `Primary_Veg` | String | Dominant vegetation type sampled. | "Chamise" | **Moisture_Site** |
| `Reading_ID` | Integer (PK) | Unique auto-incrementing ID for the sample. | 1024 | **Moisture_Reading** |
| `Site_ID` | String (FK) | Reference to the originating `Moisture_Site`. | "MALIBU_01" | **Moisture_Reading** |
| `Date` | Date | The day the vegetation was field-sampled. | 2017-12-04 | **Moisture_Reading** |
| `LFM_Percent` | Float | Water content relative to dry biomass. | 62.5 | **Moisture_Reading** |
| `Fuel_Type` | String | Classification of the sampled material. | "Old Growth" | **Moisture_Reading** |
| `Fire_ID` | Integer (PK) | Unique record ID from the CAL FIRE database. | 5521 | **Wildfire_Event** |
| `Fire_Name` | String | Official name of the wildfire event. | "THOMAS" | **Wildfire_Event** |
| `Alarm_Date` | Date | Official ignition/reporting timestamp. | 2017-12-04 | **Wildfire_Event** |
| `GIS_Acres` | Float | Total area burned in acres. | 281893.0 | **Wildfire_Event** |
| `Unit_ID` | String (FK) | Reference to the managing `Unit_Agency`. | "VNC" | **Wildfire_Event** |
| `Is_Catastrophic` | Boolean | Target: True (1) if acres >= 10,000. | 1 | **Wildfire_Event** |
| `Unit_ID` | String (PK) | Three-letter agency code. | "VNC" | **Unit_Agency** |
| `Agency_Name` | String | Full name of the responding department. | "Ventura County Fire" | **Unit_Agency** |
| `Region_Type` | String | Administrative classification of the unit. | "Contract County" | **Unit_Agency** |

**Quantification of Uncertainty:**

| Feature Name | Primary Source of Uncertainty | Estimated Impact/Range |
| :--- | :--- | :--- |
| `LFM_Percent` | **Measurement Error:** Variations in oven-drying time, leaf-to-stem ratios, and scale calibration during field collection. | ±3% to 5% absolute moisture. |
| `GIS_Acres` | **Mapping Error:** Satellite and aerial infrared sensors struggle with "cloud masking" or smoke occlusion during active burns. | ±2% to 10% spatial variance. |
| `Alarm_Date` | **Reporting Lag:** The time between actual ignition and the first 911 call or satellite thermal anomaly detection. | < 30 min (Urban); < 2 hrs (Remote). |
| `Regional_Average` | **Spatial Variance:** Using a 28-site average assumes the landscape dries uniformly; ignores slope-aspect micro-climates. | ±8% variance. |

The values above reflect the inherent limitations of field-collected environmental data and remote sensing. Because fuel moisture can vary by topography, the "Arid Edge" is treated as a high-probability risk zone rather than an absolute binary. Acknowledging these margins of error makes sure the model accounts for the natural variance in Southern California’s complex landscape, allowing for a more robust and conservative safety threshold.
