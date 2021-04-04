library(tidyverse)

prediction_data340 <- read.csv("prediction_data340.csv")
prediction_data360 <- read.csv("prediction_data360.csv")
prediction_data390 <- read.csv("prediction_data390.csv")

lag1_CR <- data.frame("datetime_id" = prediction_data340$datetime_id,
                      "lag1_CR_FL340" = prediction_data340$lag_1_CR,
                      "lag1_CR_FL360" = prediction_data360$lag_1_CR,
                      "lag1_CR_FL390" = prediction_data390$lag_1_CR)
window_wsize = 2

data <- lag1_CR %>%
  mutate(FL340_1 = lag(lag1_CR_FL340, 2),
         FL340_2 = lag(lag1_CR_FL340, 1),
         FL360_1 = lag(lag1_CR_FL360, 2),
         FL360_2 = lag(lag1_CR_FL360, 1),
         FL390_1 = lag(lag1_CR_FL390, 2),
         FL390_2 = lag(lag1_CR_FL390, 1),)

output <- data %>%
  select(datetime_id, lag1_CR_FL360, FL340_1, FL340_2,FL360_1, FL360_2,FL390_1, FL390_2)

output <- output[c(-1:-4),]
