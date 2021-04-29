install.packages("AppliedPredictiveModeling")
library(AppliedPredictiveModeling)
library(caret)
library(e1071) # misc library including skewness function
library(corrplot)
library(lattice)

## Data loading
data_all <- read.csv("C:/Users/ssays/Desktop/GMU/2021_Spring/DAEN690 Capstone project/Team Dragon/6.Prediction/Prediction/prediction_data_V2.csv")
str(data_all)

## Data spliting
train_row <- c(1:4000)
train_x <- data_all[train_row,c(3:8)]
train_y <- data_all[train_row,c(2)]
test_x <- data_all[-train_row,c(3:8)]
test_y <- data_all[-train_row,c(2)]

## Preprocessing ??
# fl_PP <- preProcess(train_x, c("BoxCox", "center", "scale"))
# trainXTrans <- predict(fl_PP, train_x)
# testXTrans <- predict(fl_PP, test_x)

## Linear regression
set.seed(100)
lrfit <- lm (train_y ~ . , data = train_x)
summary(lrfit)

# Compute the prediction for the new test data set 
lmPred1 <-  predict(lrfit, test_x)

# Evaluate the test performance using a caret function
lmValues1 <-  data.frame(obs = test_y, pred = lmPred1)
result1 <- as.data.frame(t(defaultSummary(lmValues1)))
result1$Models <- "Linear regression"
result1

##############################################################################

# MLP (Neural Network)
nnGrid = expand.grid( .decay=c(0,0.01,0.1), .size=1:10 )
set.seed(100)
nnetModel = train(x=train_x, y=train_y, method="nnet", preProc=c("center", "scale"),
                  linout=TRUE, trace=FALSE, MaxNWts=10 * (ncol(train_x)+1) + 10 + 1, 
                  maxit=500, tuneGrid = nnGrid)

nnetModel  

summary(nnetModel)

 
# Compute the prediction for the new test data set 
nnetPred = predict(nnetModel, test_x)
nnetPR = postResample(pred=nnetPred, obs=test_y)

nnetPR

# Evaluate the test performance using a caret function
lmValues2 <-  data.frame(obs = test_y, pred = nnetPred)
result2 <- as.data.frame(t(defaultSummary(lmValues2)))
result2$Models <- "Neural Networks"

result2

# Final results
result <-rbind(result1, result2)
result
