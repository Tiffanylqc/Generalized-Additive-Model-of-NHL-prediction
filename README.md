# Generalized-Additive-Model-of-NHL-prediction


## csv files

### result.csv
Based on preprocessed_datasets.csv where semantics are defined:


Field Name| Explanation|
----------|------------|
id        | nhl.com id for NHL players, otherwise Eliteprospects.com id|
Draft Age | Age in Draft Year|
Country_group   | Nationality. Canada -> 'CAN', USA -> 'USA', countries in Europe -> 'EURO'|
Position  | Position in Draft Year. Left Wing -> 'L', Right Wing -> 'R', Center -> 'C', Defencemen -> 'D'| 
Overall   | Overall pick in NHL Entry Draft|
CSS_rank  | Central scouting service ranking in the draft year|
rs_GP     | Games played in regular seasons in the draft year|
rs_G      | Goals in regular seasons in the draft year|
rs_A      | Assists in regular seasons in the draft year|
rs_P      | Points in regular seasons in the draft year|
rs_PIM    | Penality_in_Minutes in regular seasons in the draft year|
rs_PlusMinus| Goal Differential in regular seasons in the draft year|
po_GP     | Games played in playoffs in the draft year|
po_G      | Goals in playoffs in the draft year|
po_A      | Assists in playoffs in the draft year|
po_P      | Points in playoffs in the draft year|
po_PIM    | Penality_in_Minutes in playoffs in the draft year|
po_PlusMinus|  Goal Differential in playoffs in the draft year|
sum_7yr_GP| Total games played in player's first 7 years of NHL career|
sum_7yr_TOI| Total Time_on_Ice in player's first 7 years of NHL career|
GP_7yr_greater_than_0| Played a game or not in player's first 7 years of NHL career|


I add 5 colomuns and create a new file called result.csv

Field Name| Explanation|
----------|------------|
rs_ppg    | points per game in regular season for players|
po_ppg    | points per game in play off for players|
cescin    | if Country_group=='EURO' then cescin=CSS_rank*6.27, else cescin=CSS_rank*1.35|
rs_gaa    | rs_G-rs_G_avg(in player's draft year)|
po_gaa    | po_G-po_G_avg(in player's draft year)|

### test1.csv test2.csv train1.csv train2.csv
These four files are part of result.csv and divided according to the draft year

### test1_withpredict.csv test2_withpredict.csv
Add the predict value for sum_7yr_GP using GAM model to test1.csv and test2.csv


## Python


DataPreprocess.py is for generating the new 5 columns 
TrainAndTest.py is for creating test files and train files. Test files and train files are divided according to players' draft years.

File Name | Draft Year |
----------|------------|
Train1 | 1998,1999,2000|
Test1 | 2001,2002|
Train2 | 2004,2005,2006|
Test2 | 2007,2008|


## R


Model.R is for creating GAM model and calculate the correlations
