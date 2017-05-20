
# coding: utf-8

# In[ ]:

#파일 이름이 주어졌을 때 jpg를 찾아서 gif로 바꾸는 코드 작성
from PIL import Image
s = "minion.jpg"
m = Image.open("C:\\Users\\USER\\Desktop\\minion.jpg")
m.save("C:\\Users\\USER\\Desktop\\minion.gif")

