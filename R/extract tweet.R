# Install Libraries/packages

install.packages("dplyr")
install.packages("tidyverse")
install.packages("httpuv")
install.packages("readr")
install.packages("ggplot2")
install.packages("rtweet")
install.packages("glue")
install.packages("backports")
install.packages("xlsx")

# Import library

library(xlsx)
library(dplyr)
library(tidyverse)
library(httpuv)
library(ggplot2)
library(rtweet)
library(readr)
library(glue)
library(backports)

#stream tweets
stream_tweets("")

#extract tweet #hacktoberfest with number 500
hacktoberfest <- search_tweets("#hacktoberfest", n=500, include_rts = TRUE, lang = "id")
hacktoberfest

#extract timeline Mr. JOkowi

jokowi <- get_timeline("@jokowi", n=100)

# information twitter user
pemerintah <-lookup_users(c("jokowi", "Menlu_RI", "mohmahfudmd"))

#cek followers
followers <- pemerintah[,c("screen_name", "followers_count")]

#plot followers twitter 07/07/2021

followers_twitter <- ggplot(data = followers,
                     mapping = aes(x = screen_name,
                                   y = followers_count,
                                   color = screen_name)) +
  geom_line(size=4)+geom_bar(stat="identity",fill="white", width=0.5) + 
  geom_text(aes(label=followers_count), vjust=1.6, color="black",
            position = position_dodge(0.9), size=3.5) +
  theme(axis.text.x = element_text(angle = 90, hjust = 1, size = 12, color="darkred"))

print(followers_twitter)  

# Save single data object to working directory
saveRDS(jokowi,
        file = "tweets_jokowi.RData")
saveRDS(corona,
        file = "tweets_hastag_corona.RData")

