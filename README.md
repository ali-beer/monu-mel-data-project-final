### Project proposal: Learning & development in children

**Team members:** Alison Beer, Jacob Sussmilch, Grace X

### Topic 
Predictors of developmental vulnerability in children.

### Rationale 
The Australian Early Development Census (AEDC) provides an insight at a community level into the learning and development needs of young children. The AEDC is also a useful measure of future development and learning, indicating how well early childhood education programs have prepared them for future learning experiences. AEDC data is collected on individual children around Australia who are in their first year of full-time school. AEDC age is based on the student’s reported date of birth and the date on which the Instrument was completed by the teacher. This variable is available in years and varies by state depending on the first year of compulsory school starting age.  

Our group aims to use the AEDC data with ABS census data on labour force statistics to investigate factors driving developmental vulnerabilities in children.

### Data
This project will use 2018 AEDC data and 2016 ABS census data. Data will be reported by Statistical Area level 2 for Victoria. 

In Victoria, all children must be enrolled in a school in the year they turn 6, which is the compulsory school-starting age. Using the 2018 AEDC data for Victoria means the developmental scores represent children turning 6 years old. These children will be turning 4 years old in the 2016 Census data year. Information on their parents labor force status will be investigated as a predictor of their developmental vulnerability.

**AEDC data by SA2:** (https://www.aedc.gov.au/resources/detail/public-table-by-statistical-area-level-2-(sa2)-2009-2018)[https://www.aedc.gov.au/resources/detail/public-table-by-statistical-area-level-2-(sa2)-2009-2018]

**ABS census data by SA2:** Labour force status of one and two parent family / by age of youngest child (0-4 years)

### Setup
With requirements installed:

**Flask App:**
`python3 run.py`

**Streamlit App:**
`streamlit run streamlitapp.py`

### Machine learning
A supervised learning regression and classification machine learning model would be best suited for this analysis. A random forest algorithm will be used to determine the relative importance of each variable.

Note: A rule of thumb for determining number of trees: the more estimators you have the better the results. However, more estimators will require more training time and data could be too ‘noisy’ to make good predictions.

### Further information
**AEDC data:** [https://www.aedc.gov.au/data/downloads](https://www.aedc.gov.au/data/downloads)

**ABS Census data:** [https://www.abs.gov.au/census/find-census-data/historical](https://www.abs.gov.au/census/find-census-data/historical)

**Useful Resources:**
- [2018 AEDC Data Collection Technical Report](https://www.aedc.gov.au/Websilk/Handlers/ResourceDocument.ashx?id=54a02864-db9a-6d2b-9fad-ff0000a141dd)
- [Report on the quality of 2016 Census data](https://www.abs.gov.au/websitedbs/d3310114.nsf/home/Independent+Assurance+Panel/$File/CIAP+Report+on+the+quality+of+2016+Census+data.pdf)


### Optional additional analysis
Use Australia’s Mothers and Babies data on maternal age, smoking, low birth weight and preterm birth and compare to AEDC data.

**Aust. Mothers and Babies data:** 
2003, 2012, 2015, 2018

**AEDC data:** 
2009, 2012, 2015, 2018
