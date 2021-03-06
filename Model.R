library(mgcv)
train1=read.csv(file='~/Documents/Lab_GAM/DataPreprocess/train1.csv')
GAM_s1<-gam(Family=Poisson,sum_7yr_GP~s(rs_ppg,bs="cr")+s(po_ppg,bs="cr")+cescin+Weight+Height+s(rs_gaa,bs="cr")+s(po_gaa,bs="cr"),data=train1)
test1=read.csv(file='~/Documents/Lab_GAM/DataPreprocess/test1.csv')
predict1<-predict.gam(GAM_s1,newdata=test1)

test1['predict1']=predict1
write.csv(test1,file='~/Documents/Lab_GAM/DataPreprocess/test1_withpredict.csv')

test1_corr_predict_and_sum7yrGP_spearman=cor(test1['sum_7yr_GP'],predict1,method="spearman")
test1_corr_Overall_and_sum7yrGP_spearman=cor(test1['Overall'],test1['sum_7yr_GP'],method="spearman")

train2=read.csv(file='~/Documents/Lab_GAM/DataPreprocess/train2.csv')
GAM_s2<-gam(Family=Poisson,sum_7yr_GP~s(rs_ppg,bs="cr")+s(po_ppg,bs="cr")+cescin+Weight+Height+s(rs_gaa,bs="cr")+s(po_gaa,bs="cr"),data=train2)
test2=read.csv(file='~/Documents/Lab_GAM/DataPreprocess/test2.csv')
predict2<-predict.gam(GAM_s2,newdata=test2)

test2['predict2']=predict2
write.csv(test2,file='~/Documents/Lab_GAM/DataPreprocess/test2_withpredict.csv')

test2_corr_predict_and_sum7yrGP_spearman=cor(test2['sum_7yr_GP'],predict2,method="spearman")
test2_corr_Overall_and_sum7yrGP_spearman=cor(test2['Overall'],test2['sum_7yr_GP'],method="spearman")

original=read.csv(file='~/Documents/Lab_GAM/DataPreprocess/preprocessed_datasets.csv')
correlation=cor(original['sum_7yr_GP'],original['Overall'],method="pearson")
