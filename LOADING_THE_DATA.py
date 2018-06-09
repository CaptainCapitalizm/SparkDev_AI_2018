
# coding: utf-8

# In[3]:


from xml.etree import ElementTree
from skimage import io
from PIL import Image


# In[4]:


dom = ElementTree.parse('MiracleDataFile.xml') #xml file we're gonna parse
root = dom.getroot()


# In[67]:


images_labels = []
#imgs = [] #if you need single arrays just uncomment this
#labels = [] #if you need single arrays just uncomment this
images_labels.append([]) #making a 2D array in python
images_labels.append([])

filepath = 'C:/Users/eshou/Desktop/TestSetWords/TestSetWords' #change this to whatever you need to
for x in range(1, 6156): #keep this range the same, it will go through the whole xml file
    for y in range(0, len(root[x])): #dont touch this either
        for child in root[x][y]:
            if(child.tag == 'word'):
                first_id = child.attrib['id'].split('-') #this is to append the filepath, you probably don't need to change this
                first_add = first_id[0] 
                second_add = first_id[0] + '-' + first_id[1]
                filepath += '/' + first_add + '/' + second_add + '/' + child.attrib['id'] + '.png'
                img = io.imread(filepath) #takes in the image to this variable
                label = child.attrib['text'] #takes in the text to this variable
                images_labels[0].append(img) #puts it into each array
                images_labels[1].append(label)
                
                #imgs.append(img) #if you need single arrays just uncomment this
                #labels.append(label) #if you need single arrays just uncomment this
                filepath = 'C:/Users/eshou/Desktop/TestSetWords/TestSetWords' #change this to whatever you set up there
                print(child.attrib['id']) 

