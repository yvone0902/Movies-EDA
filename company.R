##Company 
library(readxl)
library(dplyr)
movie_dataset <- read_excel("C:/Users/Administrator/Desktop/movie_dataset.xlsx")
View(movie_dataset)


##Paramount
Paramount = filter(movie_dataset,Production_company == "Paramount Pictures")
sum(Paramount$Revenue)
sum(Paramount$Budget)
summary(Paramount)

##Universal
Universal = filter(movie_dataset,Production_company == "Universal Pictures")
sum(Universal$Revenue)
sum(Universal$Budget)
summary(Universal)


##disney
Disney = filter(movie_dataset,Production_company == "Walt Disney Pictures")
sum(Disney$Revenue)
sum(Disney$Budget)
summary(Disney)

##columbia
Columbia = filter(movie_dataset,Production_company == "Columbia Pictures")
sum(Columbia$Revenue)
sum(Columbia$Budget)
summary(Columbia)

##Fox
Fox = filter(movie_dataset,Production_company == "Twentieth Century Fox Film Corporation")
sum(Fox$Revenue)
sum(Fox$Budget)
summary(Fox)

##NewLine
NewLine = filter(movie_dataset,Production_company == "New Line Cinema")
sum(NewLine$Revenue)
sum(NewLine$Budget)
summary(NewLine)

##Village
Village = filter(movie_dataset,Production_company == "Village Roadshow Pictures")
sum(Village$Revenue)
sum(Village$Budget)
summary(Village)

##Warner
Warner = filter(movie_dataset,Production_company == "Warner Bros.")
sum(Warner$Revenue)
sum(Warner$Budget)
summary(Warner)

##dreamworks
Dreamworks = filter(movie_dataset,Production_company == "DreamWorks SKG")
sum(Dreamworks$Revenue)
sum(Dreamworks$Budget)
summary(Dreamworks)

##Lucas
Lucas = filter(movie_dataset,Production_company == "Lucasfilm")
sum(Lucas$Revenue)
sum(Lucas$Budget)
summary(Lucas)