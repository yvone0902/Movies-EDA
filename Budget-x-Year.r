#Import Data
library(readxl)
budget_year <- read_excel("C:/Users/DVF2/Desktop/EDAwow/Budget x Year.xlsx")

#Install Libraries
library(lattice)
library(ggplot2)

#Histogram
histogram(budget_year$Year, data = budget_year$Budget,main = "Percentage of Distribution of Movie Budget
          per Year",xlab = "Year",ylab = "Budget",
          scales=list(x=list(at=seq(1880,2022,10))), breaks = 50, col= "pink")

