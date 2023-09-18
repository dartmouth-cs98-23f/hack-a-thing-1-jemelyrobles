#!/usr/bin/env python
# coding: utf-8

# In[1]:


#JemelyR
#Hack-a-thing, 23F

# made from a tutorial from: https://medium.com/@stepanfilonov/tracking-your-eyes-with-python-3952e66194a6
#code is mostly from the tutorial as i was following it to learn how to develop eye tracking


import cv2
import numpy
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') #provided by tutorial
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml') #provided by tutorial


# In[2]:


img = cv2.imread("portrait.jpg")


# In[3]:


#make the picture gray so that what is flat color isn't a face
gray_picture = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray_picture, 1.3, 5)


# In[5]:


#if we can detect a face it can then be widdled down to eyes
#the rectangles are based on the gray image but drawn over the colorful one
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2) #creates rectangle around face
    gray_face = gray_picture[y:y+h, x:x+w] #gray version
    face = img[y:y+h, x:x+w] #normal version
    eyes = eye_cascade.detectMultiScale(gray_face)
    for (ex,ey,ew,eh) in eyes: 
        cv2.rectangle(face,(ex,ey),(ex+ew,ey+eh),(0,225,255),2)#creates rectangle around ""


# In[6]:


#will still detect other areas of the face that aren't eyes 
#just because they're small dark areas


# In[ ]:


cv2.imshow('my image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 

# In[ ]:




