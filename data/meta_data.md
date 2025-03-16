## Basketball Player Season Data Documentation

### Player and Team Information

- player_name: (string) Name of the player.
- team: (string) Team abbreviation or name.
- conf: (string) Conference the team belongs to (e.g., ACC, Big Ten).
- yr: (string) Player's year in college (e.g., Freshman, Sophomore, Junior, Senior).
- ht: (float) Player's height in cm.
- num: (integer) Player's jersey number.
- pid: (integer) Unique player ID.
- type: (string) Player classification (e.g., guard, forward, center).
- pos_class: (string) Positional classification (e.g., "Combo G", "Pure PG", "Wing F").

### Performance Metrics
- GP: (integer) Games played.
- Min_per: (float) Minutes played per game.
- ORtg: (float) Offensive rating.
- usg: (float) Usage rate.
- eFG: (float) Effective field goal percentage.
- TS_per: (float) True shooting percentage.
- ORB_per: (float) Offensive rebound percentage.
- DRB_per: (float) Defensive rebound percentage.
- AST_per: (float) Assist percentage.
- TO_per: (float) Turnover percentage.
- FTM: (integer) Free throws made.
- FTA: (integer) Free throws attempted.
- FT_per: (float) Free throw percentage.
- twoPM: (integer) Two-point field goals made.
- twoPA: (integer) Two-point field goals attempted.
- twoP_per: (float) Two-point field goal percentage.
- TPM: (integer) Three-point field goals made.
- TPA: (integer) Three-point field goals attempted.
- TP_per: (float) Three-point field goal percentage.
- blk_per: (float) Block percentage.
- stl_per: (float) Steal percentage.
- ftr: (float) Free throw rate.

### Advanced Metrics
- porpag: (float) Points over replacement player per game.
- adjoe: (float) Adjusted offensive efficiency.
- pfr: (float) Personal foul rate.
- Rec Rank: (integer) Player's recruiting rank.
- ast/tov: (float) Assist-to-turnover ratio.
- rimmade: (integer) Field goals made at the rim.
- rimmade+rimmiss: (integer) Total attempts at the rim.
- midmade: (integer) Mid-range field goals made.
- midmade+midmiss: (integer) Total mid-range attempts.
- rimmade/(rimmade+rimmiss): (float) Rim field goal percentage.
- midmade/(midmade+midmiss): (float) Mid-range field goal percentage.
- dunksmade: (integer) Dunks made.
- dunksmiss+dunksmade: (integer) Total dunk attempts.
- dunksmade/(dunksmade+dunksmiss): (float) Dunk percentage.

### Defensive Metrics
- pick: (integer) Number of steals or defensive plays.
- drtg: (float) Defensive rating.
- adrtg: (float) Adjusted defensive rating.
- dporpag: (float) Defensive points over replacement per game.
- stops: (integer) Defensive stops.

### Box Plus-Minus Metrics
- bpm: (float) Box plus-minus.
- obpm: (float) Offensive box plus-minus.
- dbpm: (float) Defensive box plus-minus.
- gbpm: (float) Global box plus-minus.
- ogbpm: (float) Offensive global box plus-minus.
- dgbpm: (float) Defensive global box plus-minus.

### Counting Stats
- mp: (integer) Minutes played.
- oreb: (integer) Offensive rebounds.
- dreb: (integer) Defensive rebounds.
- treb: (integer) Total rebounds.
- ast: (integer) Assists.
- stl: (integer) Steals.
- blk: (integer) Blocks.
- pts: (integer) Points scored.

Metadata
- year: (integer) Season year (2010-2025).

