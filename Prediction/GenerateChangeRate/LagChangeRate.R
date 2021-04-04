library(tidyverse)
setwd("~/Desktop/master/4 DAEN690/YES_CSV")

############ FL360
FL360_summary <- read.csv("FL360_summary.csv")
output <- FL360_summary %>%
  select(datetime_id, volume_of_ISSR) %>%
  rename(percent_volume = volume_of_ISSR )

for (i in 1:48){
  col_name <- paste("lag_", as.character(i), "_CR",sep = "")
  output <- output %>%
    mutate( !!col_name :=  if_else((log(percent_volume)-log(lag(percent_volume, i)) ) == -Inf |
                                     (log(percent_volume)-log(lag(percent_volume, i)) ) == Inf |
                                     is.na((log(percent_volume)-log(lag(percent_volume, i)) )), 
                                   0, 
                                   (log(percent_volume)-log(lag(percent_volume, i)) ) * 100))
  for (j in 1:i){
    output[j,i+2] = NA
  }
}
write.csv(output,"~/Desktop/master/4 DAEN690/YES_CSV/prediction_data360.csv", row.names = FALSE)

############ FL340
FL340_summary <- read.csv("FL340_summary.csv")
output <- FL340_summary %>%
  select(datetime_id, volume_of_ISSR) %>%
  rename(percent_volume = volume_of_ISSR )

for (i in 1:48){
  col_name <- paste("lag_", as.character(i), "_CR",sep = "")
  output <- output %>%
    mutate( !!col_name :=  if_else((log(percent_volume)-log(lag(percent_volume, i)) ) == -Inf |
                                     (log(percent_volume)-log(lag(percent_volume, i)) ) == Inf |
                                     is.na((log(percent_volume)-log(lag(percent_volume, i)) )), 
                                   0, 
                                   (log(percent_volume)-log(lag(percent_volume, i)) ) * 100))
  for (j in 1:i){
    output[j,i+2] = NA
  }
}
write.csv(output,"~/Desktop/master/4 DAEN690/YES_CSV/prediction_data340.csv", row.names = FALSE)

############ FL390
FL390_summary <- read.csv("FL390_summary.csv")
output <- FL390_summary %>%
  select(datetime_id, volume_of_ISSR) %>%
  rename(percent_volume = volume_of_ISSR )

for (i in 1:48){
  col_name <- paste("lag_", as.character(i), "_CR",sep = "")
  output <- output %>%
    mutate( !!col_name :=  if_else((log(percent_volume)-log(lag(percent_volume, i)) ) == -Inf |
                                     (log(percent_volume)-log(lag(percent_volume, i)) ) == Inf |
                                     is.na((log(percent_volume)-log(lag(percent_volume, i)) )), 
                                   0, 
                                   (log(percent_volume)-log(lag(percent_volume, i)) ) * 100))
  for (j in 1:i){
    output[j,i+2] = NA
  }
}
write.csv(output,"~/Desktop/master/4 DAEN690/YES_CSV/prediction_data390.csv", row.names = FALSE)








