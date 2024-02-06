#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data = pd.DataFrame()

for i in range(1,7):
    if i < 3:
        data = pd.concat([data, pd.read_csv(f"Ganison_dataset_{i}.csv")])
    else:
        data = pd.concat([data, pd.read_csv(f"ganison_dataset_{i}.csv")])

data.head()


# In[3]:


data.info()


# In[4]:


data['year_lvl_name'] = data.year.apply(str) + "_" + data['Year Level'].apply(str)


# In[5]:


data = data.drop(columns=[
    'awarDistinction', 
    'participant_count', 
    'credit_count', 
    'distinct_count', 
    'high_distinct_count', 
    'strength_status', 
    'school_percentile', 
    'total_area_assessed_score', 
    'student_area_assessed_score', 
    'student_total_assessed',
    'sydney_participants',
    'sydney_average_score'
])


# In[6]:


data.info()


# In[7]:


data = data.drop(columns=['Year Level', 'year'])

data.head()


# In[8]:


data['school_name'].unique()


# In[9]:


data.size


# In[10]:


answer_data = [(1, 'A'), (2, 'B'), (3, 'C'), (4, 'D')]
def get_answer_index(answer):
    for id, item in answer_data:
        if item == answer:
            return id
data['AnswerID'] = data['Answers'].map(lambda x: get_answer_index(x))
data['CorrectAnswerID'] = data['Correct Answers'].map(lambda x: get_answer_index(x))


# In[11]:


data.head()


# In[12]:


data['StudentID'] = data['First Name'].map(lambda x: x.split()[-1])

data.head()


# In[13]:


student_data = list()

for fName, lName in list(data[['First Name', 'Last Name']].drop_duplicates().itertuples(index=False, name=None)):
    student_data.append((fName.split()[-1], f"{fName} {lName}"))


# In[14]:


data.head()


# In[15]:


data = data.drop(columns=['First Name', 'Last Name'])


# In[16]:


data.head()


# In[17]:


index = 1
subject_data = list()

for subject in data['Subject'].unique():
    subject_data.append((index, subject))
    index += 1

def get_subject_index(subject):
    for id, item in subject_data:
        if item == subject:
            return id

data['SubjectID'] = data['Subject'].map(lambda x: get_subject_index(x))

data = data.drop(columns=['Subject'])


# In[18]:


index = 1
school_data = list()

for school in data['school_name'].unique():
    school_data.append((index, school))
    index += 1

def get_school_index(school):
    for id, item in school_data:
        if item == school:
            return id

data['SchoolID'] = data['school_name'].map(lambda x: get_school_index(x))

data = data.drop(columns=['school_name'])


# In[19]:


index = 1
award_data = list()

for award in data['award'].unique():
    award_data.append((index, award))
    index += 1

def get_award_index(award):
    for id, item in award_data:
        if item == award:
            return id

data['AwardID'] = data['award'].map(lambda x: get_award_index(x))

data = data.drop(columns=['award'])


# In[20]:


award_data


# In[21]:


index = 1
class_data = list()

for cls in data['Class'].unique():
    class_data.append((index, cls))
    index += 1

def get_class_index(cls):
    for id, item in class_data:
        if item == cls:
            return id

data['ClassID'] = data['Class'].map(lambda x: get_class_index(x))


# In[22]:


class_data


# In[23]:


data = data.drop(columns='Class')
data.head()


# In[24]:


index = 1
assessment_area_data = list()

for area in data['Assessment Areas'].unique():
    assessment_area_data.append((index, area))
    index += 1

def get_area_index(area):
    for id, item in assessment_area_data:
        if item == area:
            return id

data['AreaID'] = data['Assessment Areas'].map(lambda x: get_area_index(x))

data.head()


# In[25]:


assessment_area_data


# In[26]:


data = data.drop(columns='Assessment Areas')
data.head()


# In[27]:


print("School Data:", school_data)


# In[28]:


print("Student Data:", student_data[0:5])


# In[29]:


print("Subject Data: ", subject_data)


# In[30]:


print("Area Data", assessment_area_data)


# In[31]:


print("Class Data:", class_data)


# In[32]:


print("Award Data:", award_data)


# In[33]:


import json


# In[34]:


def to_json_file(arr, columns, model_name, file_name):
    assert len(arr[0]) == len(columns)
    new_list = list()
    for data in arr:
        dict = {}
        for i in range(len(columns)):
            if pd.isna(data[i]):
                dict[columns[i]] = None
            else:
                dict[columns[i]] = data[i]
        fixture = {
            'model': model_name,
            'fields': dict
        } 
        new_list.append(fixture)
    
    json_data = json.dumps(new_list)
    f = open(file_name, 'w')
    f.write(json_data)
    f.close()


# In[35]:


to_json_file(student_data, ["id", "name"], "tests.Student", "tests/fixtures/student.json")


# In[36]:


to_json_file(school_data, ["id", "name"], "tests.School", "tests/fixtures/school.json")


# In[37]:


to_json_file(subject_data, ["id", "name"], "tests.Subject", "tests/fixtures/subject.json")


# In[38]:


to_json_file(assessment_area_data, ["id", "name"], "tests.AssessmentArea", "tests/fixtures/area.json")


# In[39]:


to_json_file(class_data, ["id", "name"], "tests.Class", "tests/fixtures/class.json")


# In[40]:


to_json_file(list(filter(lambda x: not pd.isna(x[1]),award_data)), ["id", "name"], "tests.Award", "tests/fixtures/award.json")


# In[41]:


s = data.groupby('SubjectID').student_score.sum()
a = zip(s, s.index)
d = {}
for x,y in a:
    d[y] = x

d


# In[42]:


def func(l):
    p = list(l)
    p.append(d[l[0]])
    return tuple(p)
new_sub = map(func, subject_data)
a = list(new_sub)


# In[43]:


to_json_file(a, ["id", "name","score"], "tests.Subject", "tests/fixtures/subject.json")


# In[ ]:




