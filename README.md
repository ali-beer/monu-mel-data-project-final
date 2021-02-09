### Setup

With requirements installed:

**Flask App:**
`python3 run.py`

**Streamlit App:**
`streamlit run streamlitapp.py`


---

### Learning & Development In Children - Data Analysis - Project Proposal

**Team members:** Alison Beer, Jacob Sussmilch, Grace X

### Topic 
Learning and developmental needs of young children.

### Rationale 
The five Australian Early Development Census (AEDC) domains provide an insight at a community level into the learning and development needs of young children. The AEDC is also a useful predictor of future development and learning, indicating how well early childhood education programs have prepared them for future learning experiences. AEDC data is collected on individual children around Australia who are in their first year of full-time school. 
Our group aims to use the AEDC data with ABS census data on labour force statistics and/or Australian Mothers and Babies data to investigate factors driving developmental vulnerabilities in children. Data will be reported at Statistical Area Level 2 (SA2) or Level 3 depending on availability.
A supervised learning regression and classification machine learning model would be best suited for this analysis. A random forest algorithm will be used to determine the relative importance of each variable.

**Time period/s:**

Children born in 2009 will be turning 2 years old in 2011 and turning 6 years old in 2015. 
-	2011 ABS census 
-	2015 AEDC (NSW, VIC)

Children born in 2003 will be turning 3 years old in 2006 and turning 6 years old in 2009. 
-	2006 ABS census
-	2009 AEDC

### Data sources

AEDC data by SA2 (2009, 2012, 2015 and 2018): https://www.aedc.gov.au/resources/detail/public-table-by-statistical-area-level-2-(sa2)-2009-2018 
ABS census data by SA2 (2011) Vic and NSW: 
Labour force status and age of mothers / one or two parent family / by age of youngest child http://stat.data.abs.gov.au/Index.aspx?DataSetCode=ABS_C16_G44_SA# 

**Optional additional analysis**
Use Australia’s Mothers and Babies data on maternal age, smoking, low birth weight and preterm birth by SA3 and compare to AEDC data (SA3)
AEDC data: https://www.aedc.gov.au/resources/detail/public-table-by-statistical-area-level-(sa3)-2009-2018 
Aust. Mothers and Babies data: 
State	Aust. Mothers and Babies	AEDC data 	Statistical Area
Vic & NSW	2012	2018	Level 3 (SA3)
Vic & NSW	2009	2015	Level 3 (SA3)
Vic & NSW	2006	2012	Level 3 (SA3)
Vic & NSW	2003	2009	Level 3 (SA3)

### Notes:
-	A rule of thumb for determining number of trees: the more estimators you have the better the results. However, more estimators will require more training time and data could be too ‘noisy’ to make good predictions.

**What time periods should we use?**
AEDC data collected on children during their first year of full-time school. AEDC age is based on the student’s reported date of birth and the date on which the Instrument was completed by the teacher. This variable is available in years: 
-	under five years
-	five years
-	six years
-	over six years.

First year of full-time school: https://schoolinfo.com.au/ 
-	WA – All WA children must be enrolled in pre-primary if they are 5 years old by 30 June of the year they start. Age range - four-and-a-half to five-and-a-half. For example, for 2018 they must be 5 years old by 30 June 2018
-	VIC -   all Victorian children must be enrolled in a school in the year they turn 6, which is the compulsory school-starting age.
-	NSW - All NSW children must be enrolled in a primary school in the year they turn 6.

AEDC data: https://www.aedc.gov.au/data/downloads 
-	2018
-	2015
-	2012
-	2009

ABS Census data: https://www.abs.gov.au/census/find-census-data/historical 
-	2011
-	2006
-	2001
-	1996

Data available:
- Children born in 2009 will be turning 2 years old in 2011 and turning 6 years old in 2015. 
-	Children born in 2003 will be turning 3 years old in 2006 and turning 6 years old in 2009.

Data not available:
-	Children born in 2003 will be turning 2 years old in 2005 and turning 6 years old in 2009 (AEDC available).
-	Children born in 2006 will be turning 2 years old in 2008 (ABS census not available) and turning 6 years old in 2012 (AEDC available). 
-	Children born in 2012 will be turning 2 years old in 2014 (ABS census not available) and turning 6 years old in 2018 (AEDC available). 

https://www.abs.gov.au/statistics/labour/employment-and-unemployment/labour-force-status-families/latest-release#update-on-families-data-for-2015-2018 

