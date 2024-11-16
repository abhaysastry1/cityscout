# CityScout: Identifying Safe Cities Based on Crime Statistics

CityScout is a tool designed to help users identify safe cities based on specific demographic factors and crime statistics. Whether you're planning a vacation or considering a move, CityScout provides tailored safety information to meet your unique needs.

## Introduction

Safety is a top priority when choosing a place to live or visit. While general crime statistics are widely available, they often fail to address specific demographic concerns. CityScout bridges this gap by providing tailored safety information based on user-selected criteria, such as crime rates against women, children, or tourists.

## Dashboard

Explore our interactive dashboard here: [CityScout Dashboard](https://public.tableau.com/app/profile/sai.paresh.karyekar/viz/CityScout_17316885780750/Dashboard1#1)

### How to Use the Dashboard

1. Open the CityScout link provided above.
2. Select your demographic category of interest (e.g., women travelling solo, children, tourists).
3. View the interactive choropleth map displaying a heat map representing the risk score for different states.
4. Adjust the population filter using the sliding bar to refine your results.
5. Explore the list of top 10 safe cities based on the calculated crime risk scores.
6. Switch to State view to narrow down your results to a particular state and view the county-wise choropleth map with cities reflecting the state filter.
7. Analyze the top crimes for the selected category or states to make an informed decision.

   
## Technology Stack

- Python
- Pandas
- PySpark
- Google Cloud Platform (GCP)
- Dolthub (for database management)
- Tableau

## Project Structure

The project consists of two main components:

1. **Data Processing:**
   - `dolt_test.py`: Queries the database hosted on DoltHub
   - `merge.py`: Merges various datasets extracted for each year or feature

2. **Tableau Dashboard:**
   - Interactive visualization of processed data

## Data Source

The final dataset (~2GB) used for analysis is available on Google Drive: [Merged Dataset Link](https://drive.google.com/file/d/1bwY2fyMjmfNOJpI-wdUImQXk9CvTFs9E/view)

## Development

Data processing operations were performed using Python's PySpark and Pandas on Google Cloud Platform to handle the large dataset size and computational requirements. The orignal dataset can be found here [Dataset Link](https://www.dolthub.com/repositories/Liquidata/fbi-nibrs)

1.  Intall Dolt by [building from source](https://docs.dolthub.com/introduction/installation/source).
2.  Clone the FBI NIBRS data repository hosted on Dolthub [here](https://www.dolthub.com/repositories/Liquidata/fbi-nibrs) using the command `dolt clone Liquidata/fbi-nibrs`. Please keep in mind that this is a 1.1TB database, so ensure you have sufficient storage space.
3. Run the ___ script to get the necessary columns for further analysis. The script uses PySpark. Ensure the file path is correct when running the script.
4. Merge the files by running [merge.py](https://github.com/abhaysastry1/cityscout/blob/main/merge.py) script.
5. The merged_output.csv file was renamed and used in further analyses.

Alternatively, please feel free to access the data used for our tool linked under Data Source.

## Machine Learning and Regression Analysis
We employ Multiple Linear Regression (MLR) techniques to:
- Filter out relevant offenses for each demographic category using machine learning.
- Forecast crime rates for cities to provide more accurate safety suggestions.
[Placeholder for further details on ML files and reproduction steps]

## Limitations
- The current dataset is static and does not include real-time updates.
- Some states are not included in the dataset due to data availability constraints.
- The dashboard is currently available only as a Tableau visualization.

## Future Enhancements

- Incorporate real-time data updates
- Expand demographic categories
- Incorporate missing states
- Develop mobile applications for on-the-go access
