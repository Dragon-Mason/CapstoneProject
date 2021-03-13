library(tidyverse)
setwd("~/Desktop/master/4 DAEN690/YES_CSV")
grib_names <- scan("nameFile.txt", what="", sep="\n")

# Select all records with flight level of 360 (pressure level = 27500)
# Only retrive columns: datetime_id, date_id, date, hour, latitude, longitude
FL360 <- data.frame()
for (i in 1:length(grib_names)) {
  csv_name <- paste("yes_", grib_names[i], ".csv",sep="")
  yes_data <- read.csv(csv_name)
  data <- yes_data %>%
    filter(pressure_level == 27500) %>%
    mutate(month = date%%10000%/%100,
           day =  date%%10000%%100) %>%
    select(datetime_id, date_id, month, day, hour, latitude, longitude)
  
  FL360 <- bind_rows(FL360, data)
  print(i)
} 
write.csv(FL360,"~/Desktop/master/4 DAEN690/YES_CSV/FL360.csv", row.names = FALSE)
