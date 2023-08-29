#Import Data
library(readxl)
rev_year <- read_excel("C:/Users/DVF2/Desktop/EDAwow/Revenue x Year.xlsx")

#Install Libraries
library(lattice)
library(ggplot2)

#Histogram
histogram(rev_year$Year, data = rev_year$Revenue,main = "Percentage of Distribution of Movie Revenue
          per Year",xlab = "Year",ylab = "Revenue",
          scales=list(x=list(at=seq(1880,2022,10))), breaks = 50, col= "#0e488c")

