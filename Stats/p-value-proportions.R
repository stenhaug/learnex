library(tidyverse)

# i make 60 out of 100 free throws
# is my

prop.test(60, 100, p = 0.53, alternative = "two.sided", correct = TRUE)
binom.test(60, 100, p = 0.53, alternative = "two.sided")

# we can basically half our p-value by saying hey we won't conclude anything if its less than
# essentially what we're fixing is if there isn't anything we are wrong 5% of the time
# we can sort of move around our ability to detect different things by saying
binom.test(60, 100, p = 0.53, alternative = "greater")

# what is that 19%
# if the truth is 53% here is the distribution out of 100

draws <- tibble(draws = rbinom(1000000, 100, 0.53))

draws %>%
    ggplot(aes(x = draws)) +
    geom_histogram() +
    geom_vline(xintercept = c(46, 60), color = "red")

mean(draws$draws >= 60 | draws$draws <= 46)
