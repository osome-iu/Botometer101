####################################
# 0.5
# shib vs. floki
res <- prop.test(x = c(1215, 1130), n = c(2000, 2000))
res$p.value
sqrt(res$statistic)

# shib vs. aapl
res <- prop.test(x = c(1215, 1030), n = c(2000, 2000))
res$p.value
sqrt(res$statistic)

# floki vs. appl
res <- prop.test(x = c(1130, 1030), n = c(2000, 2000))
res$p.value
sqrt(res$statistic)


####################################
# 0.7
# shib vs. floki
res <- prop.test(x = c(591, 578), n = c(2000, 2000))
res$p.value
sqrt(res$statistic)

# shib vs. aapl
res <- prop.test(x = c(591, 760), n = c(2000, 2000))
res$p.value
sqrt(res$statistic)

# floki vs. appl
res <- prop.test(x = c(578, 760), n = c(2000, 2000))
res$p.value
sqrt(res$statistic)