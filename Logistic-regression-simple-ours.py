#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Φέρε τη βιβλιοθήκη pandas και δώσε ψευδώνυμο pd
#Η βιβλιοθήκη pandas μας βοηθάει να φτιάξουμε έναν πίνακα με τα δεδομένα μας
import pandas as pd
#Διάβασε το αρχείο csv
mydata = pd.read_csv("Covid-Dataset-with-numbers.csv")


# In[2]:


mydata.head(10)


# In[3]:


myfeatures = mydata.iloc[:, 0:-1]

#myfeatures.shape
#mydata.shape
mytargets = mydata.iloc[:, -1]
mytargets.head()
#myfeatures.head()


# In[4]:


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(myfeatures, mytargets, test_size=0.25, random_state=0)


# In[5]:


from sklearn.linear_model import LogisticRegression


# In[6]:


logisticRegr = LogisticRegression()


# In[7]:


logisticRegr.fit(x_train, y_train)


# In[8]:


#x_test.head()


# In[9]:


#mytest.shape


# In[10]:


for sample_id in range(0, 20):
    print("id: {}".format(sample_id))
    mytest = x_test.iloc[sample_id, :]
    #mytest.head()
    #predicted_value = logisticRegr.predict(mytest.reshape(1,-1))
    #https://stackoverflow.com/questions/53723928/attributeerror-series-object-has-no-attribute-reshape
    predicted_value = logisticRegr.predict(mytest.values.reshape(1, -1))
    predicted_probs = logisticRegr.predict_proba(mytest.values.reshape(1,-1))
    #The returned estimates for all classes are ordered by the label of classes.
    print(predicted_probs)
    print("predicted_value: {}".format(predicted_value))
    print(predicted_probs[0][predicted_value])
    print("actual value: {}".format(y_test.iloc[sample_id]))


# In[ ]:




