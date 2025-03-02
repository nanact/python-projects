import pandas as pd  
import numpy as np   

exams_data = {"name":["Anaslaia","Dina","Katherine","james","Emily","Matthew","kevin","james"],"score":[12.5,9,16.5,np.nan,9,20,14.5,np.nan],"attempts":[1,3,2,3,2,1,1,2],"quality":["yes","no","yes","no","no","yes","yes","no"]}
labels = ["a","b","c","d","e","f","g","h"]
df = pd.DataFrame(exams_data, index = labels)
print("Summany of the basic information about this Dataframe and its data")
print(df.info())