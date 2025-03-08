import pytesseract
from PIL import Image
import re
import time


def imageToText():
    pytesseract.pytesseract.tesseract_cmd = r'/bin/tesseract'
    c = pytesseract.image_to_string(Image.open('screenshot.png'), lang='eng', config='--psm 6')

    s = c.split("\n")
    teams = re.split(r'Team', s[-2])[1:]

    points = s[0].split(" ")[1:]

    points = [s[1].split(" ")[1]] + points

    if len(points) != 15 or len(teams) != 15:
        print("Failing to parse image correctly")
        return {}
    
    mapping = {}
    for i in range(15):
        print(f"Team: {teams[i]}, Points: {points[i]}")
        mapping[f"Team{teams[i]}"] = points[i]
    return mapping

def calDiff(past, money_per_points):
    current = imageToText()
    for key in current:
        current[key] = ( (current[key] - past[key]) * money_per_points ) + current[key]
    return current

m = imageToText()
MONEY_PRE_POINTS = 100
while True:
    time.sleep(1000)
    m = calDiff(m, MONEY_PRE_POINTS)

