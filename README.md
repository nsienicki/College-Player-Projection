# College-Player-Projection
Projecting current college player NBA careers through distance to former prospect cluster centroids. 

# DESCRIPTION
This package is designed to analyze and visualize the transition of college basketball players to the NBA, focusing on statistical performance, entity resolution, and player clustering. It begins with the collection and organization of data from two primary sources: Bart Torvik’s college basketball statistics and a Kaggle dataset containing NBA player game stats. College data is retrieved year by year starting from 2010, formatted with standardized headers, and slightly extended with positional classification. NBA data includes game-by-game statistics and player information, which are processed into three key outputs summarizing player season averages, top games, and standout seasons.

The next phase is data cleaning, where the college player data from 2010–2025 is merged into a comprehensive dataset. Duplicate and incomplete entries are removed, and key metrics are aggregated using weighted averages. A player matching system is then used to connect college players with their professional counterparts. This involves normalization of university names, blocking by tokens, and fuzzy name matching to pair similar players between datasets.

In the entity resolution stage, cleaned and processed college and NBA datasets are used to identify NCAA-NBA player matches. The output includes a direct mapping of matched players and a similarity score matrix that highlights players with statistically similar college careers. This resolution sets the foundation for the clustering module, which groups players who specifically made it to the NBA—based on their statistical profiles. Clusters are optimized using the Calinski-Harabasz index to determine natural groupings based on performance and position.

Finally, the package includes a Streamlit-based visualization dashboard, which allows users to interactively explore the data. It supports player stat displays, manual stat adjustments, trend visualizations, similarity comparisons to NBA players, and player-type clustering information. This enables both quantitative analysis and intuitive insight into how college performance might translate to professional potential.

# INSTALLATION
## 1. Data Access <br>
### 1.1 College Player Data: https://barttorvik.com/.
1. Player csv stats from 2010 on can be downloaded by year by adding requested year to “year=XXXX” string on to the url above: getadvstats.php?year=2010&csv=1
2. Code expects the downloaded files to be placed in the data folder where trank_processing.py is run
3. Header names sourced here: https://www.dropbox.com/scl/fi/ulpor6aan63e9aelqfkdb/pstatheaders.xlsx?rlkey=i6b0r1ln6jxl9uq5d9rrz03nv&e=1&dl=0
4. trank_processing.py takes the unlabeled csv files and adds the headers. There are two new columns that are not included in the header summary
5. One is a postitional classification (named "pos_class" in trank_processing.py), while the other is unknown, and has been dropped

### 1.2 NBA Player Data: 
1. NBA Game Histroical Box Score data and corresponding Player Identification helper data can be found at this link on Kaggle: https://www.kaggle.com/datasets/eoinamoore/historical-nba-data-and-player-box-scores
2. Download PlayerStatistics.csv and Players.csv and place them in the data folder within the CODE directory
3. Once the data is in the proper location, open and run the nba_players_season_avgs.ipynb Jupyter Notebook
4. This notebook will create three csv files: player_avgs_2008-2025.csv, player_best_games.csv, and player_best_seasons.csv 

## 2. Data Cleaning
### 2.1 College Player Data Cleaning
1. Input: college player data from 2010 - 2025
2.  Notebook: data_processing.ipynb
3.  Output: player_data_college.csv
4.  Process:
    - Concatenation: Combine player data from 2010 to 2025 into a single dataset.
    - Slicing: Merge player data across multiple years using a unique combination of player and team names, ensuring one row per player.
    - Cleaning: Remove incomplete records with minimal data for any given year.
    - Aggregation: Calculate the weighted average of key performance metrics.
 ### 2.2 Player Matching Summary
1. Input: college player and NBA data
2. Process:
    - Normalize: Normalize university names (uppercase, no punctuation).
    - Cleaning: Token block by splitting school names into words and matching on overlapping tokens (e.g., “Duke” ↔ “Duke University”).
    - Matching: Within each block, apply fuzzy name matching (token_sort_ratio) to find the best player name match.

 
## 3. Entity Resolution
### 3.1 Overview
1. Code (notebook): ./entity-resolution/nba_ncaa_entity_res.ipynb
2. Inputs: nba_player_avgs_2008-2025.csv, trank_data_2024.csv, player_data_college.csv
3. Outputs: nba_ncaa_matches.csv, player_similarity_results.csv

### 3.2 Steps to Run Code
1. Take the output of the NBA player data crawling and cleansing notebook (./CODE/nba_players_season_avgs.ipynb) and place it in the entity-resolution directory. Rename the file to nba_player_avgs_2008-2025.csv
2. Download the 2024 file from the college player dataset and place it in the entity-resolution directory with the file name as trank_data_2024.csv
3. Run the data cleaning notebook (./data/data_processing.ipynb) and put the output in the entity-resolution directory with file name player_data_college.csv
4. Run all the cells in the ./entity-resolution/nba_ncaa_entity_res.ipynb notebook to get the outputs
5. The nba_ncaa_entity_res.ipynb notebook will produce two outputs
   - nba_ncaa_matches.csv: The NCAA to NBA player matches
   - player_similarity_results.csv: A map that has NCAA player pairs that are similar to one another based on euclidean distance calculaions between a subset of season statistics
  
## 4. Clustering
1. Inputs: nba_ncaa_map.csv, player_data_college.csv
2. Code: college_class.py
3. Process
   - Taking player_data_college_2010-2025.csv, we run college_class.py. For our uses the only_NBA indicator should be set to True to cluster on college players who made it to the NBA.
   -  Goal is to cluster, optimizing on Calinski-Harabasz index to compare various variable selection techniques and number of clusters auto-define number of clusters
   -  We strip out players who did not make the NBA (based on Entity Resolution via nba_ncaa_map.csv)
   -  The code produces three outputs, cluster_stats.csv (lays out each cluster's highest concentration of position classification), eval_scores.csv (showing each dataset's CH Index performance) and player_cluster.csv (assigns each player a cluster) 

## 5. Visualization
1. Inputs/Outputs: player_data_college_latest_season.csv (input); nba_player_avgs_2008-2025.csv (input); nba_ncaa_map.csv (input); basketball.png (input); espn_ncaa_player_ids.csv (code-generated); cluster_stats.csv (code-generated); player_cluster.csv (code-generated)
2. Code: vis_dash_cse6242.py; ncaa_img_scrape.py
3. Tool: Streamlit, Python, Github
4. Implementation:
    - Utilized Streamlit Package in Python to develop the dashboard design on a local host
    - The base dashboard file is vis_dash_cse6242.py which utilizes the inputs and integrates the clustering methodology defined above
    - NCAA image id's were scraped using ncaa_img_scrape.py which outputted espn_ncaa_player_ids.csv
    - Top Comparisons were generated using kNN-Euclidean distance based off of Points, Assists, Rebounds, Blocks, Steals, Height, FT%, FG%, 3PT%, Turnovers, and Defensive Rating features
    - Projections were made utilizing the nba comparison stats in their first (1-5) years in the NBA
    - Player Type Archetype was predicted based on the PCA model that was trained (described under the clustering section)
    - All Relevant files (including requirements.txt, which lists the python packages that were used) were uploaded to a github repository and deployed to the streamlit app (also included in the visualization folder under the main branch)
6. Dashboard Link: https://visdashcse6242py-ygacmznbsumuhzrrhpdi3j.streamlit.app/
7. Features:
   - Player Selector: Dropdown menu to choose a player.
   - Player Stats Display: Auto-filled stats including Points, Assists, Rebounds, Blocks, and Steals.
   - Stat Adjustment Sliders: Manually tweak player stats using sliders.
   - Performance Projection: Visualizes year-over-year stat trends.
   - NBA Comparisons: Displays the most similar NBA player.
   - Player Type Projection: Classifies player and shows cluster placement.
   - All Visuals are Dyanamic to the interactive input from the sliders and can also be reset using the reset button or by selecting a new draft prospect.

# EXECUTION
1. Dashboard Link: https://visdashcse6242py-ygacmznbsumuhzrrhpdi3j.streamlit.app/
2. Features:
   - Player Selector: Dropdown menu to choose a player.
   - Player Stats Display: Auto-filled stats including Points, Assists, Rebounds, Blocks, and Steals.
   - Stat Adjustment Sliders: Manually tweak player stats using sliders.
   - Performance Projection: Visualizes year-over-year stat trends.
   - NBA Comparisons: Displays the most similar NBA player.
   - Player Type Projection: Classifies player and shows cluster placement.  

