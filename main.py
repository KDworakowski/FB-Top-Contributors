import pandas as pd
from config import *

"""
Create variable which reads excel data using pandas library.

Read data from given arguments.
"""
filedata = pd.read_excel(excel_file_name, excel_sheet_name)

"""
Create variables which necessary data such as names, posts etc.
"""
names = filedata["Top Contributors"].values.tolist()
posts = filedata["Posts"].values.tolist()
comments = filedata["Comments"].values.tolist()
likes = filedata["Likes"].values.tolist()

"""
Create count variable for our logic to work.
"""
count = 0

"""
Create list with results.
"""
result = []

"""
Create while loop.

While count variable is smaller than length of all the names.
"""
while(count < len(names)):
    """
    Print: number of count, name, amount of: posts, comments and likes.
    """
    print(str(count+1) + ".Name: " + names[count] + " | Posts: " + str(posts[count]) \
        + " | Comments: " + str(comments[count]) + " | Likes: " + str(likes[count]))
    """
    Multiply all of the points by given arguments and count them.
    """
    counted_points = (posts[count] * posts_points) + (comments[count] * comments_points) + (likes[count] * likes_points)
    """
    Connect name string with name from the excel.
    """
    name = ("Name: " + str(names[count]))
    """
    Append counted points and name to the result list.
    """
    result.append([counted_points,name])
    count = count + 1

"""
Sort result list, from high to low integer.
"""
sort_results = result.sort(reverse=True)

print(*result, sep='\n')
