from scipy import stats

speed=[60,70,65,80,100,100,110,65]
mode=stats.mode(speed)
print(mode)
