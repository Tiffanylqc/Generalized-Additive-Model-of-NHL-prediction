import pandas as pd


csvfile=pd.read_csv('preprocessed_datasets.csv')
outfile=pd.read_csv('result.csv')

#  calculate <regular season, points per game>
rs_P = csvfile['rs_P'] # Points in regular seasons in the draft year
rs_GP = csvfile['rs_GP'] # Games played in regular seasons in the draft year
rs_ppg=[]
for i in range(len(rs_P)):
    if rs_GP[i]==0:
        rs_ppg.append(0)
    else:
        rs_ppg.append(rs_P[i]/rs_GP[i]) # regular season, points per game


# calcuate <play off, points per game>
po_P = csvfile['po_P'] # Points in playoffs in the draft year
po_GP = csvfile['po_GP'] # Games played in playoffs in the draft year
po_ppg=[]
for i in range(len(po_P)):
    if po_GP[i]==0:
        po_ppg.append(0)
    else:
        po_ppg.append(po_P[i]/po_GP[i]) # play off, points per game


# calculate cescin
cescin=[]
country_group = csvfile['country_group'] # country group
cssRank = csvfile['CSS_rank'] # css rank
for i in range(len(country_group.tolist())):
    if country_group[i]=='EURO':
        cescin.append(cssRank[i]*6.27)
    else:
        cescin.append(cssRank[i]*1.35)


# calculate <regular season goal in average for each draft year>
# stored in dict <rs_G_avg>
rs_G = csvfile['rs_G'].tolist() # Goals in regular seasons in the draft year
draft_year = csvfile['DraftYear'].tolist() # draft year
rs_G_sum = {}
rs_G_avg = {}
count={}

for i in range(len(rs_G)):
    if draft_year[i] not in rs_G_sum:
        rs_G_sum[draft_year[i]]=rs_G[i]
        count[draft_year[i]]=1
    else:
        rs_G_sum[draft_year[i]]+=rs_G[i]
        count[draft_year[i]]=count[draft_year[i]]+1

for key,item in rs_G_sum.items():
    rs_G_avg[key]=item/count[key]


# calculate <play off goal in average for each draft year>
# stored in dict <po_G_avg>
po_G=csvfile['po_G'].tolist() # Goals in playoff in the draft year
po_G_sum = {}
po_G_avg = {}
count2={}

for i in range(len(po_G)):
    if draft_year[i] not in po_G_sum:
        po_G_sum[draft_year[i]]=po_G[i]
        count2[draft_year[i]] = 1
    else:
        po_G_sum[draft_year[i]]+=po_G[i]
        count2[draft_year[i]] = count2[draft_year[i]] + 1

for key,item in po_G_sum.items():
    po_G_avg[key]=item/count2[key]


# calculate <regular season, goals against average>
rs_gaa = [] # regular season, golas against average
for i in range(len(rs_G)):
    year = draft_year[i]
    average = rs_G_avg[year]
    rs_gaa.append(rs_G[i] - average)


# calculate <play off, goals against average>
po_gaa = [] # regular season, golas against average
for i in range(len(po_G)):
    year = draft_year[i]
    average = po_G_avg[year]
    po_gaa.append(po_G[i] - average)

outfile['rs_ppg'] = rs_ppg
outfile['po_ppg'] = po_ppg
outfile['cescin'] = cescin
outfile['rs_gaa'] = rs_gaa
outfile['po_gaa'] = po_gaa
outfile.to_csv('result.csv',index=False)
