import pandas as pd

csvfile=pd.read_csv('result.csv')
# train 1, get player information from 1998-2000
train1=csvfile[(csvfile['DraftYear']==1998)|(csvfile['DraftYear']==1999)|(csvfile['DraftYear']==2000)]
train1.to_csv('train1.csv')

# test 1, get player information from 2001-2002
test1=csvfile[(csvfile['DraftYear']==2001)|(csvfile['DraftYear']==2002)]
test1.to_csv('test1.csv')

# train 2, get player information from 2004-2006
train2=csvfile[(csvfile['DraftYear']==2004)|(csvfile['DraftYear']==2005)|(csvfile['DraftYear']==2006)]
train2.to_csv('train2.csv')

# test2, get player information from 2007-2008
test2=csvfile[(csvfile['DraftYear']==2007)|(csvfile['DraftYear']==2008)]
test2.to_csv('test2.csv')