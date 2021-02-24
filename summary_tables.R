library(tidyverse)
setwd("/Volumes/Long_long/DAEN690Dragon/YES_CSV")
grib_names <- scan("nameFile.txt", what="", sep="\n")
xyz_cells <- 112*150*37
xy_cells <- 112*150


overall_summary <- data.frame()
for (i in 1:length(grib_names)) {
  # for (i in 4561:5016) {
  csv_name <- paste("yes_", grib_names[i], ".csv",sep="")
  yes_data <- read.csv(csv_name)
  data <- yes_data %>%
    summarise(datetime_id = min(datetime_id),
              date_id = min(date_id),
              date = min(date),
              hour = min(hour),
              volume_of_ISSR = n()/xyz_cells,
              num_of_ISSR = n(),
              ceiling = max(pressure_level),
              floor = min(pressure_level),
              south_id = min(lat_id),
              north_id = max(lat_id), 
              south = min(latitude),
              north = max(latitude), 
              west_id =  min(lon_id),
              east_id = max(lon_id), 
              west = min(longitude),
              east = max(longitude))
  overall_summary <- bind_rows(overall_summary, data)
  print(i)
} 
write.csv(overall_summary,"/Volumes/Long_long/DAEN690Dragon/YES_CSV/overall_summary.csv", row.names = FALSE)


layer_summary <- data.frame()
for (i in 1:length(grib_names)) {
  # for (i in 4561:5016) {
  csv_name <- paste("yes_", grib_names[i], ".csv",sep="")
  yes_data <- read.csv(csv_name)
  data <- yes_data %>%
    group_by(pressure_level) %>%
    summarise(datetime_id = min(datetime_id),
              date_id = min(date_id),
              date = min(date),
              hour = min(hour),
              volume_of_ISSR = n()/xy_cells,
              num_of_ISSR = n(),
              south_id = min(lat_id),
              north_id = max(lat_id), 
              south = min(latitude),
              north = max(latitude), 
              west_id =  min(lon_id),
              east_id = max(lon_id), 
              west = min(longitude),
              east = max(longitude)) %>%
    relocate(pressure_level, .before = volume_of_ISSR)
  layer_summary <- bind_rows(layer_summary, data)
  print(i)
}  
write.csv(layer_summary,"/Volumes/Long_long/DAEN690Dragon/YES_CSV/layer_summary.csv", row.names = FALSE)




