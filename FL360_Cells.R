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

##### Hourly updated volume_of_ISSR at FL360
FL360_summary_hour <- FL360_summary
FL360_summary_hour$month<-factor(FL360_summary_hour$month)

ggplot(data = FL360_summary_hour, mapping = aes(x = datetime_id, y = volume_of_ISSR, fill = month)) +
  geom_bar(stat = "identity") +
  theme( axis.text.x=element_blank(), axis.ticks.x=element_blank()) +
  ylab("volume_of_ISSR (%)") + xlab("Hourly Datetime") +
  ggtitle("Hourly updated volume_of_ISSR at FL360")
  
  
ggplot(data = FL360_summary_hour, mapping = aes(x = datetime_id, y = volume_of_ISSR, col=month)) +
  # geom_bar(stat = "identity") +
  geom_line() +
  facet_wrap(~ month, nrow = 2,ncol = 4, scales = "free_x") +
  ylab("volume_of_ISSR (%)") + xlab("Hourly Datetime") +
  ggtitle("Hourly updated volume_of_ISSR at FL360")

##### Daily average volume_of_ISSR at FL360

FL360_summary_day <- FL360_summary %>%
  group_by(date_id) %>%
  summarise(month = min(month),
            day = min(day),
            avg_volume_of_ISSR = sum(volume_of_ISSR)/24)
FL360_summary_day$month<-factor(FL360_summary_day$month)  

ggplot(data = FL360_summary_day, mapping = aes(x = day, y = avg_volume_of_ISSR, col=month)) +
  # geom_bar(stat = "identity") +
  geom_line() +
  facet_wrap(~ month, nrow = 2,ncol = 4, scales = "free_x") +
  ylab("avg_volume_of_ISSR (%)") + xlab("Day") +
  ggtitle("Daily avgerage volume_of_ISSR at FL360")

###### Monthly average volume_of_ISSR at FL360
month_days_df = data.frame(month = c(5,6,7,8,9,10,11,12),
                           month_days = c(15,30,31,31,30,31,30,31))
FL360_summary_month <- FL360_summary %>%
  left_join(month_days_df, by = "month") %>%
  group_by(month) %>%
  summarise(avg_volume_of_ISSR = sum(volume_of_ISSR)/min(month_days)/24)
FL360_summary_month$month<-factor(FL360_summary_month$month)  

ggplot(data = FL360_summary_month, mapping = aes(x = month, y = avg_volume_of_ISSR, fill= month)) +
  geom_bar(stat = "identity") +
  ylab("avg_volume_of_ISSR (%)") + xlab("Month") +
  ggtitle("Monthly average volume_of_ISSR at FL360") +
  geom_text(aes(label = round(avg_volume_of_ISSR, 4)),
            vjust = -1.1, size = 3,
            show.legend = FALSE)



###### Daily updated volume_of_ISSR at midnight and midday at FL360
midnight_noon <- FL360_summary %>%
  filter(hour == 0 | hour == 12)
midnight_noon$hour <- factor(midnight_noon$hour)

ggplot(midnight_noon, aes(x = day, y = volume_of_ISSR, col=hour)) + 
  geom_line() +
  facet_wrap(~ month, nrow = 2,ncol = 4, scales = "free_x") +
  ylab("volume_of_ISSR (%)") + xlab("Day") +
  ggtitle("Volume_of_ISSR at midnight and midday at FL360")

###### Monthly average volume_of_ISSR at at each hour at FL360
month_days_df = data.frame(month = c(5,6,7,8,9,10,11,12),
                           month_days = c(15,30,31,31,30,31,30,31))
midnight_noon2 <- FL360_summary %>%
  # filter(hour == 0 | hour == 12) %>%
  left_join(month_days_df, by = "month") %>%
  group_by(month, hour) %>%
  summarise(avg_volume_of_ISSR = sum(volume_of_ISSR)/min(month_days))
midnight_noon2$hour <- factor(midnight_noon2$hour)

ggplot(midnight_noon2, aes(x = month, y = avg_volume_of_ISSR, col=hour)) + 
  geom_line() +
  ylab("Monthly average volume_of_ISSR (%)") + xlab("Months") +
  ggtitle("Monthly average volume_of_ISSR at each hour at FL360")







