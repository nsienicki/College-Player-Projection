# College-Player-Projection
Projecting current college player NBA careers through distance to former prospect cluster centroids. 

## Data Access <br>
### College Player Data: https://barttorvik.com/.
1. Player csv stats from 2010 on can be downloaded by year by adding requested year to “year=XXXX” string on to the url above: getadvstats.php?year=2010&csv=1
2. Header names sourced here: https://www.dropbox.com/scl/fi/ulpor6aan63e9aelqfkdb/pstatheaders.xlsx?rlkey=i6b0r1ln6jxl9uq5d9rrz03nv&e=1&dl=0
3. trank_processing.py takes the unlabeled csv files and adds the headers. There are two new columns that are not included in the header summary
4. One is a postitional classification (named "pos_class" in trank_processing.py), while the other is unknown, and has been dropped

### NBA Player Data: XXXXXXX

## Entity Resolution

## Data Cleaning

## Clustering
Inputs: nba_ncaa_map.csv, player_data_college_2010-2025.csv
Code: college_class.py
1. Taking player_data_college_2010-2025.csv, we run college_class.py. For our uses the only_NBA indicator should be set to True to cluster on college players who made it to the NBA.
2. Goal is to cluster, optimizing on Calinski-Harabasz index to compare various variable selection techniques and number of clusters auto-define number of clusters
3. We strip out players who did not make the NBA (based on Entity Resolution via nba_ncaa_map.csv)
4. The code produces three outputs, cluster_stats.csv (lays out each cluster's highest concentration of position classification), eval_scores.csv (showing each dataset's CH Index performance) and player_cluster.csv (assigns each player a cluster) 

## Visualization
    

