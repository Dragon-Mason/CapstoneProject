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

FL360 <- read.csv('FL360.csv')
FL360_summary <- FL360 %>%
  group_by(datetime_id) %>%
  summarise(date_id = min(date_id),
            month = min(month),
            day = min(day),
            hour = min(hour),
            volume_of_ISSR = n()/112/150*100)
write.csv(FL360_summary,"~/Desktop/master/4 DAEN690/YES_CSV/FL360_summary.csv", row.names = FALSE)

# Select all records with flight level of 390 (pressure level = 25000)
# Only retrive columns: datetime_id, date_id, date, hour, latitude, longitude
FL390 <- data.frame()
for (i in 1:length(grib_names)) {
  csv_name <- paste("yes_", grib_names[i], ".csv",sep="")
  yes_data <- read.csv(csv_name)
  data <- yes_data %>%
    filter(pressure_level == 25000) %>%
    mutate(month = date%%10000%/%100,
           day =  date%%10000%%100) %>%
    select(datetime_id, date_id, month, day, hour, latitude, longitude)
  
  FL390 <- bind_rows(FL390, data)
  print(i)
} 
write.csv(FL390,"~/Desktop/master/4 DAEN690/YES_CSV/FL390.csv", row.names = FALSE)

FL390 <- read.csv('FL390.csv')
FL390_summary <- FL390 %>%
  group_by(datetime_id) %>%
  summarise(date_id = min(date_id),
            month = min(month),
            day = min(day),
            hour = min(hour),
            volume_of_ISSR = n()/112/150*100)
write.csv(FL390_summary,"~/Desktop/master/4 DAEN690/YES_CSV/FL390_summary.csv", row.names = FALSE)

# Select all records with flight level of 340 (pressure level = 30000)
# Only retrive columns: datetime_id, date_id, date, hour, latitude, longitude
FL340 <- data.frame()
for (i in 1:length(grib_names)) {
  csv_name <- paste("yes_", grib_names[i], ".csv",sep="")
  yes_data <- read.csv(csv_name)
  data <- yes_data %>%
    filter(pressure_level == 30000) %>%
    mutate(month = date%%10000%/%100,
           day =  date%%10000%%100) %>%
    select(datetime_id, date_id, month, day, hour, latitude, longitude)
  
  FL340 <- bind_rows(FL340, data)
  print(i)
} 
write.csv(FL340,"~/Desktop/master/4 DAEN690/YES_CSV/FL340.csv", row.names = FALSE)

FL340 <- read.csv('FL340.csv')
FL340_summary <- FL340 %>%
  group_by(datetime_id) %>%
  summarise(date_id = min(date_id),
            month = min(month),
            day = min(day),
            hour = min(hour),
            volume_of_ISSR = n()/112/150*100)
write.csv(FL340_summary,"~/Desktop/master/4 DAEN690/YES_CSV/FL340_summary.csv", row.names = FALSE)


