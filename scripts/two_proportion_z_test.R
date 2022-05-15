####################################
# 0.5
# shib vs. floki
res <- prop.test(x = c(1098, 1061), n = c(1819, 1893))
res$p.value
sqrt(res$statistic)

# shib vs. aapl
res <- prop.test(x = c(1098, 936), n = c(1819, 1864))
res$p.value
sqrt(res$statistic)

# floki vs. appl
res <- prop.test(x = c(1061, 936), n = c(1893, 1864))
res$p.value
sqrt(res$statistic)


####################################
# 0.7
# shib vs. floki
res <- prop.test(x = c(524, 557), n = c(1819, 1893))
res$p.value
sqrt(res$statistic)

# shib vs. aapl
res <- prop.test(x = c(524, 688), n = c(1819, 1864))
res$p.value
sqrt(res$statistic)

# floki vs. appl
res <- prop.test(x = c(557, 688), n = c(1893, 1864))
res$p.value
sqrt(res$statistic)