# importing necessary libraries
import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
import re
import numpy

# creating a data frame from the csv file
df = pd.read_csv("../data/data.csv")
# print("All the 356 PR Links:")
# print(df['Pull Request'])

# Filtering only the PR of Apache Company Repository
apacheDataSet = df[df['Repo'].str.contains('/apache')]

# Filtering only the PR of Mozilla Company Repository
mozillaDataSet = df[df['Repo'].str.contains('/mozilla')]

# Filtering only the PR of Google Company Repository
googleDataSet = df[df['Repo'].str.contains('/google')]

# Filtering only the PR of Facebook Company Repository
facebookDataSet = df[df['Repo'].str.contains('/facebook')]


# Using only Apache PR's
pullRequestList = mozillaDataSet['Pull Request'].values.tolist()

print("Length of PR's of Apache:")
print(len(pullRequestList))
print(pullRequestList)

dictw = {'title': [],
         'comment': []
       }
resultDF = pd.DataFrame(dictw)


# scraping the apache pull requests
commitsList = []
filesChangedList = []
green = []
red = []

for i in range(len(pullRequestList)):
    URL = pullRequestList[i]
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html.parser')

    mainTitle = soup.find('h1', attrs={'class': 'gh-header-title mb-2 lh-condensed f1 mr-0 flex-auto break-word'})
    comment = soup.find('div', attrs={'class': 'edit-comment-hide'})

    heading = ""
    if mainTitle:
        for row in mainTitle.findAll('span', attrs={'class': 'js-issue-title'}):
            heading = row.get_text()
            for roww in comment.findAll('td', attrs={'class': 'd-block comment-body markdown-body js-comment-body'}):
                finalComment = roww.get_text() + '.'
            #                 for rowww in roww.find_all(['p', 'li']):
            #                     finalComment=finalComment+rowww.get_text()+'.'
            resultDF.loc[len(resultDF.index)] = [heading, finalComment]
    else:
        resultDF.loc[len(resultDF.index)] = [heading, ""]

    commits = soup.find('span', attrs={'class': 'js-updateable-pull-request-commits-count Counter'})

    if mainTitle and commits:
        commitsList.append(commits.get_text())
    else:
        commitsList.append(0)

    files_changed = soup.find('span', attrs={'id': 'files_tab_counter'})

    if mainTitle and files_changed:
        filesChangedList.append(files_changed.get_text())
    else:
        filesChangedList.append(0)

    code_churn_data = soup.find('div', attrs={'class': 'tabnav-extra float-right d-none d-md-block'})

    if mainTitle and code_churn_data:
        for i in code_churn_data.find_all('span', attrs={'class': 'color-text-success'}):
            green.append(re.sub(r'\D', '', i.get_text()))
        for j in code_churn_data.find_all('span', attrs={'class': 'color-text-danger'}):
            red.append(re.sub(r'\D', '', j.get_text()))
    else:
        green.append(0)
        red.append(0)

resultDF['num_commits']  = list(map(int, commitsList))
resultDF['files_changed']  = list(map(int, filesChangedList))
greenlist = list(map(int, green))
redlist = list(map(int, red))
res_list = []
for i in range(0, len(green)):
    res_list.append(greenlist[i] + redlist[i])

resultDF['code_churn'] = res_list

# resultDF.to_csv(r'../data/result.csv', sep=',', mode='a')

# comment list
comment_list = resultDF['comment'].values.tolist()

#title list
title_list = resultDF['title'].values.tolist()

#Identifying the root cause
rootCause=[]
# regExString=["regex","regular expression"]
# apiURLString=["api","url"]
for index in range(len(comment_list)):
    if "regex" in comment_list[index] or "regex" in title_list[index]:
        rootCause.append("regEx")
    elif "regular expression" in comment_list[index] or "regex" in title_list[index]:
        rootCause.append("regEx")
    elif "URL" in comment_list[index] or "regex" in title_list[index]:
        rootCause.append("API")
    elif "API" in comment_list[index] or "regex" in title_list[index]:
        rootCause.append("API")
    else:
        rootCause.append("Other")

resultDF['Root Cause'] = rootCause


# Identifying Manifestation
manifestation=[]
newFeatureStringList=["add","ADD"]
incorrectBehaviourStringList=["proper","modified","fixed","fix","change","changing","changes","expanding regex","expand"]
compileErrorStringList=["detected","reworked","confusing"]
badsmellrStringList=["refactor","update","updating","parse","Replace","better"]
incorrectComputationStringList=["assertion"]

for index in range(len(comment_list)):
    if any(x in comment_list[index] for x in newFeatureStringList) or any(x in title_list[index] for x in newFeatureStringList):
        manifestation.append("new feature")
    elif any(x in comment_list[index] for x in incorrectComputationStringList) or any(x in title_list[index] for x in incorrectComputationStringList):
         manifestation.append("incorrect computation")
    elif any(x in comment_list[index] for x in badsmellrStringList) or any(x in title_list[index] for x in badsmellrStringList):
         manifestation.append("bad smell")
    elif any(x in comment_list[index] for x in compileErrorStringList) or any(x in title_list[index] for x in compileErrorStringList):
        manifestation.append("compile error")
    elif any(x in comment_list[index] for x in incorrectBehaviourStringList) or any(x in title_list[index] for x in incorrectBehaviourStringList):
         manifestation.append("incorrect behavior")
    else:
        manifestation.append("other failure")

resultDF['Manifestation'] = manifestation

# Identifying Category

category=[]
acceptingInvalidStringList=["Bugfix for regex","Fix integration test script","SSP mail form"]
incorrectExtractionStringList=["StringExpander regex","fix whitelist","Fix greedy regex"]
dataProcessingStringList=["Add helper script","Add sec","Enabling extraction","Add custom context"]
badSmellStringList=["Refactor","Rename","Optimize"]
regexConfigStringList=["configurable","config"]
regexLikeImplStringList=["REGEXP_EXTRACT","Regex replacement","regex filter"]
rejectingValidStringList=["better regex","RegEx pattern should be updated","replaces the regex"]
codeSmelldStringList=["regex pattern","replace by regular","Remove"]


for index in range(len(comment_list)):
    if any(x in comment_list[index] for x in acceptingInvalidStringList) or any(x in title_list[index] for x in acceptingInvalidStringList):
        category.append("accepting invalid strings(T2)")
    elif any(x in comment_list[index] for x in incorrectExtractionStringList) or any(x in title_list[index] for x in incorrectExtractionStringList):
        category.append("incorrect extraction")
    elif any(x in comment_list[index] for x in dataProcessingStringList) or any(x in title_list[index] for x in dataProcessingStringList):
        category.append("data processing")
    elif any(x in comment_list[index] for x in badSmellStringList) or any(x in title_list[index] for x in badSmellStringList):
        category.append("bad smells")
    elif any(x in comment_list[index] for x in regexConfigStringList) or any(x in title_list[index] for x in regexConfigStringList):
        category.append("regex configuration entry")
    elif any(x in comment_list[index] for x in regexLikeImplStringList) or any(x in title_list[index] for x in regexLikeImplStringList):
        category.append("regex like implementation")
    elif any(x in comment_list[index] for x in rejectingValidStringList) or any(x in title_list[index] for x in rejectingValidStringList):
        category.append("rejecting valid strings (T1)")
    elif any(x in comment_list[index] for x in codeSmelldStringList) or any(x in title_list[index] for x in codeSmelldStringList):
        category.append("code smells")
    else:
        category.append(" ")
resultDF['Category'] = category

#Storing the executed data in a result.csv file.
resultDF.to_csv(r'../data/result.csv', sep=',', mode='a')


# code for Mann-Whitney U test to test the number of commits in both original and obtained data set
from scipy.stats import mannwhitneyu

batch_1 = resultDF['num_commits']
batch_2 = df['num_commits']

# perform mann whitney test
stat, p_value = mannwhitneyu(batch_1, batch_2)
print('Statistics=%.2f, p=%.2f' % (stat, p_value))
# Level of significance
alpha = 0.001
# conclusion
if p_value < alpha:
    print('Significant difference between two samples')
else:
    print('No significant difference between two samples')


# code for Mann-Whitney U test to test the lines of code in both original and obtained data set
# from scipy.stats import mannwhitneyu

# Take batch 1 and batch 2 data as per above example
batch_1 = resultDF['code_churn']
batch_2 = df['code_churn']

# perform mann whitney test
stat, p_value = mannwhitneyu(batch_1, batch_2)
print('Statistics=%.2f, p=%.2f' % (stat, p_value))
# Level of significance
alpha = 0.001
# conclusion
if p_value < alpha:
    print('Significant difference between two samples')
else:
    print('No significant difference between two samples')


# code for Mann-Whitney U test to test the files changed in both original and obtained data set
# from scipy.stats import mannwhitneyu

# Take batch 1 and batch 2 data as per above example
batch_1 = resultDF['files_changed']
batch_2 = df['files_changed']

# perform mann whitney test
stat, p_value = mannwhitneyu(batch_1, batch_2)
print('Statistics=%.2f, p=%.2f' % (stat, p_value))
# Level of significance
alpha = 0.001
# conclusion
if p_value < alpha:
    print('Significant difference between two samples')
else:
    print('No significant difference between two samples')


import matplotlib.pyplot as plt

def generate_distribution_histogram(dataframe,
                                    column_name,
                                    title, x_axis_label, y_axis_label,
                                    label_name,
                                    number_bins = 15):
    plt.hist(dataframe[column_name], bins = number_bins, label = label_name)
    plt.title(title)
    plt.xlabel(x_axis_label)
    plt.ylabel(y_axis_label)
    plt.legend(loc='upper right')
    plt.show()


df_result =resultDF
df_original =df
generate_distribution_histogram(df_result,
                                'num_commits',
                                title = 'Number of commits in executed(calculated) data set',
                                x_axis_label = 'Number of Commits',
                                y_axis_label = 'Frequency',
                                label_name = 'num of commits in executed data set')



generate_distribution_histogram(df_original,
                                'num_commits',
                                title = 'Number of commits in original data set',
                                x_axis_label = 'Number of Commits',
                                y_axis_label = 'Frequency',
                                label_name = 'num of commits in original data set')



generate_distribution_histogram(df_result,
                                'code_churn',
                                title = 'Lines of code changed in executed data set',
                                x_axis_label = 'Lines of code modified',
                                y_axis_label = 'Frequency',
                                label_name = 'Lines of code modified in executed data set')



generate_distribution_histogram(df_original,
                                'code_churn',
                                title = 'Lines of code modified in original data set',
                                x_axis_label = 'Lines of code modified',
                                y_axis_label = 'Frequency',
                                label_name = 'Lines of code modified in original data set')