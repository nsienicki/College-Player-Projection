# College-Player-Projection
Projecting current college player NBA careers through distance to former prospect cluster centroids. 

## Data Access <br>
### College Player Data: https://barttorvik.com/.
1. Player csv stats from 2010 on can be downloaded by year by adding requested year to “year=XXXX” string on to the url above: getadvstats.php?year=2010&csv=1
2. Header names sourced here: https://www.dropbox.com/scl/fi/ulpor6aan63e9aelqfkdb/pstatheaders.xlsx?rlkey=i6b0r1ln6jxl9uq5d9rrz03nv&e=1&dl=0
3. trank_processing.py takes the unlabeled csv files and adds the headers. There are two new columns that are not included in the header summary
4. One is a postitional classification (named "pos_class" in trank_processing.py), while the other is unknown, and has been dropped
    

