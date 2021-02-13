### Learning & Development In Children - Project Proposal

### Team members
Alison Beer, Jacob Sussmilch, Grace X

### Topic 
Predictors of developmental vulnerability in children.

### Rationale 
The Australian Early Development Census (AEDC) provides an insight at a community level into the learning and development needs of young children. The AEDC is also a useful measure of future development and learning, indicating how well early childhood education programs have prepared them for future learning experiences. AEDC data is collected on individual children around Australia who are in their first year of full-time school. 
Our group aims to use the AEDC data with ABS census data on labour force statistics to investigate factors driving developmental vulnerabilities in children. Data will be reported at Statistical Area Level 2 (SA2).

## Machine learning model
A supervised learning regression and classification machine learning model would be best suited for this analysis. A random forest algorithm will be used to determine the relative importance of each variable.

Note: A rule of thumb for determining number of trees: the more estimators you have the better the results. However, more estimators will require more training time and data could be too ‘noisy’ to make good predictions.

## Time period
AEDC data is collected on children during their first year of full-time school. AEDC age is based on the student’s reported date of birth and the date on which the Instrument was completed by the teacher. This variable is available in years and varies by state the first year of compulsory school starting age. Age variables include:
-	under five years
-	five years
-	six years
-	over six years.

In Victoia all children must be enrolled in a school in the year they turn 6, which is the compulsory school-starting age.
Children born in 2012 will be turning 4 years old in 2016 and turning 6 years old in 2018. 
-	2016 ABS census
-	2018 AEDC

### Data sources
AEDC data by SA2 (2018) Victoria: https://www.aedc.gov.au/resources/detail/public-table-by-statistical-area-level-2-(sa2)-2009-2018 

ABS census data by SA2 (2016) Victoria: Labour force status of one and two parent family / by age of youngest child (0-4 years) http://stat.data.abs.gov.au/Index.aspx?DataSetCode=ABS_C16_G44_SA# 

### Setup
With requirements installed:

**Flask App:**
`python3 run.py`

**Streamlit App:**
`streamlit run streamlitapp.py`

**Optional additional analysis**
Use Australia’s Mothers and Babies data on maternal age, smoking, low birth weight and preterm birth and compare to AEDC data
AEDC data: https://www.aedc.gov.au/resources/detail/public-table-by-statistical-area-level-(sa3)-2009-2018 
Aust. Mothers and Babies data: 2003, 2012, 2015, 2018
AEDC data: 2009, 2012, 2015, 2018
State: Victoria
Statistical Area Level 3 (SA3)

## Further information
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
