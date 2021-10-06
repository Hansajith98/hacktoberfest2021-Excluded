
  # Loading airquality dataset
  data("airquality")
  my_airquality_data <- airquality
 
  # Summarising dataset
  summary(my_airquality_data)

  
  # Data cleaning
 
   # Solution 1 to remove NA values : Omit rows containing NA value  
   copy <- airquality
   nrow(copy)

   nrow(na.omit(copy))
   
   # Solution 2 to remove NA values : Replace NA value with mean value 
   
   my_airquality_data$Ozone[is.na(my_airquality_data$Ozone)] <- as.integer(mean(my_airquality_data$Ozone, na.rm = TRUE))
   
   my_airquality_data$Solar.R[is.na(my_airquality_data$Solar.R)] <- as.integer(mean(my_airquality_data$Solar.R, na.rm = TRUE))
   
   # Checking if there are any NA values
   sum(is.na(my_airquality_data))
   
   
  # Data integration
  
   my_airquality_data_subset_1 <- my_airquality_data[1:10, c(2,3)]

   my_airquality_data_subset_2 <- my_airquality_data[1:10, c(4,5)]   
   
   cbind(my_airquality_data_subset_1, my_airquality_data_subset_2)

   
  # Data transformation

   copy$Month <- month.abb[copy$Month]
   str(copy)

  
  # Data model building (regression model for prediction of Ozone value)   
   
   # Setting predictor attribute
   solar_R <- my_airquality_data[, "Solar.R"]
   
   # Setting target attribute
   ozone <- my_airquality_data[, "Ozone"]
   
   plot(ozone~solar_R)
   
   # Fitting linear model
   model_ozone_solar_R <- lm(ozone~solar_R)
   model_ozone_solar_R        # Gives values of y-intercept and slope         
   
   abline(model_ozone_solar_R, col="blue")
   
   # Prediction of 'Ozone' when 'Solar.R'= 10
   p1 <- predict(model_ozone_solar_R, data.frame("solar_R" = 10))
   p1   
      
   