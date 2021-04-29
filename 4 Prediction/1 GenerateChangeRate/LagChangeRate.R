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

id <- data.frame("datetime_id" = c(1:5496))

FL340_summary <- FL340_summary %>%
  right_join(id, by="datetime_id")  %>%
  select(datetime_id, volume_of_ISSR) %>%
  replace_na(list(volume_of_ISSR= 0))

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

id <- data.frame("datetime_id" = c(1:5496))

FL390_summary <- FL390_summary %>%
  right_join(id, by="datetime_id")  %>%
  select(datetime_id, volume_of_ISSR) %>%
  replace_na(list(volume_of_ISSR= 0))

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








