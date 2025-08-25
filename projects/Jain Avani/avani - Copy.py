import subprocess
import sys
subprocess.check_call([sys.executable, "-m", "pip", "install", "tabulate"])
import subprocess
import sys
subprocess.check_call([sys.executable, "-m", "pip", "install", "pandas"])
from tabulate import tabulate
import pandas as pd
print("What’s up! Diva Devo here — let’s ride the fashion vibe together!!!!!!")
gender=input("Select your gender(M for Male / F for Female):")
print('''Select you body type from the given menu:
1)Pear

2)Apple

3)Hourglass

4)Rectangle

5)Inverted Triangle

6)Oval

7)Trapezoid''')
shape=input("enter your body shape number: ")
print("what is your mood today?\n")
a=["SUNNY GLOW MOOD","LOW SOCIAL WEDNESDAY","TANGLED THOUGHTS","SPOTLIGHT DIVA","COFFEE AND RAIN","BLUE HOUR","UNEXPECTED SPARKLE","STORM SURGE"]
b=["Happy Good Vibes","Silent Black Vibes","Anxious Mood","Popular Vibes","Asthetic Mood","Sad Mood","Surprise Me Mood","Angry Furious"]
c=["Bright, Warm","Dark Colours","Muted Tones","Brbie Pallet","Vintage Pallet","Blue Colours","Fluorescent Colours","Yellowish Red"]
title={"Mood":a,"Meaning of Mood":b,"Colour Preferences":c}
df=pd.DataFrame(title)
print(tabulate(df, headers='keys', tablefmt='grid'))
mood=input("enter your mood number: ")
