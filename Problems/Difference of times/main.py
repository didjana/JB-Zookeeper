walk1 = (int(input()))
walk2 = (int(input()))
walk3 = (int(input()))
walk = ((walk1 * 3600) + (walk2 * 60) + walk3)
rain1 = (int(input()))
rain2 = (int(input()))
rain3 = (int(input()))
rain = ((rain1 * 3600) + (rain2 * 60) + rain3)
print(abs(int(walk - rain)))