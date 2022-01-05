import glassdoor_scraper as gs
import gs as g
import pandas as pd 

path = "E:\\A vrudit\\Working\\Python Projects\\Glassdoor_Scraper\\chromedriver"

# df = gs.get_jobs('data scientist',1000, False, path, 15)
df = g.get_jobs('data scientist',15, False, path, 5)

df.to_csv('21aug.csv', index = False)