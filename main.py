import pandas as pd
from config import *
filedata = pd.read_excel(excel_file_name, excel_sheet_name)

names = filedata["Top Contributors"].values.tolist()
posts = filedata["Posts"].values.tolist()
comments = filedata["Comments"].values.tolist()
likes = filedata["Likes"].values.tolist()

count = 0

result = []

while(count < len(names)):
    print(str(count+1) + ".Name: " + names[count] + " | Posts: " + str(posts[count]) \
        + " | Comments: " + str(comments[count]) + " | Likes: " + str(likes[count]))
    counted_points = (posts[count] * posts_points) + (comments[count] * comments_points) + (likes[count] * likes_points)
    name = ("Name: " + str(names[count]))
    result.append([counted_points,name])
    count = count + 1

y = result.sort(reverse=True)

print(*result, sep='\n')
