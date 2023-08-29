
#INSTALLING LIBRARIES
install.packages("dpylr")
library(dplyr)
install.packages("tidyverse")
library(tidyverse)
install.packages("hmisc")
library(hmisc)
install.packages("psych")
library(psych)
install.packages("explore")
library(explore)
install.packages("lubricate")
library(lubridate)

hist(movie_dataset$Revenue)
#IMPORTING DATASET
library(readxl)
movie_datasetClean <- read_excel("D:/EDAWOW/movie_datasetClean.xlsx")
View(movie_datasetClean)


#HEADER
head(movie_datasetClean)

#SUMMARY
summary(movie_datasetClean)

#DESCRIBE
describe(movie_dataset)
explore(movie_dataset)


#CALCULATION FOR REVENUE
movie_dataset <- movie_datasetClean %>%
  drop_na(everything()) %>%
  mutate(Year = gsub("/", "", Year)) %>% 
  mutate(Year = substring(Year, 5, 8)) %>% 
  mutate(Year = gsub("-", "", Year)) %>% 
  filter(Year > 1900) %>% 
  mutate(Revenue = Revenue / 1000000) %>% 
  mutate(Budget = Budget / 1000000)

unique(movie_dataset$Year)



#Correlation Revenue and Budget
cor.test(movie_dataset$Budget,movie_dataset$Revenue, use="complete.obs")
#Plot
xyplot(Revenue~Budget, 
       data = movie,
       type=c("p","r"))

cor.test(movie$Popularity,movie$Revenue, use="complete.obs")

#Correlation Budget and Popularity
cor.test(movie$Budget,movie$Popularity, use="complete.obs")











