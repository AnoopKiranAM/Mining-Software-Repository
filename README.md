# Mining-Software-Repository

## Baseline
The following parts are taken from assignment 2: 

This is a re-creation project of the original paper. “ An empirical study on Regular Expression Bugs” as a part of a course research “Mining Software Repositories (MSR 2020-21)” provided by Softlang Team at Universität Koblenz-Landau. 

Done By:

-Anoop Kiran Angadi Manjunatha(219203384), 

Anirudh Kudaragundi Anand Rao(219203189).

## MetaData
This project describes the reproduction of the research paper “ An empirical study on Regular Expression Bugs” authored by: Peipei Wang, Chris Brown, Jamie A.Jennings, Kathryn T.Stolee.

In this project, we present an empirical study of 356 merged regex-related pull requests from Apache, Mozilla, Facebook, and Google GitHub repositories. Based on the classification the root causes and manifestations of those bugs,  we show that incorrect regular expression is the dominant behavior for the cause of regular expression bugs.


DBLP Link: https://dl.acm.org/doi/10.1145/3379597.3387464

## Requirements
 * ***Hardware*** : Windows, Mac or Linux operating system. Good and fast processor.

* ***Software***: Anaconda, Python(pip install the required libraires mentioned below), Microsoft Excel

## Process: 
### Steps: 
Step 1: Install below third party libraries using below commands.

•	Install python 3.9.2 (mac) or for windows (https://www.python.org/downloads/)

•	Install numpy 1.17.2 (pip install numpy==1.17.2)

•	Install pandas 0.25.1 (pip install pandas==0.25.1)

•	Install matplotlib 3.1.1 (pip install matplotlib==3.1.1)

•	Install GitPython 3.1.0 (pip install Git Python==3.1.0)

•	Install Beautiful Soup (pip install beautifulSoup4)

## Data
### Data-Preprocessing
Total No. of Pull Requests in the beginning: 356

Step 1: Filtering the PR's which has java, java script and python as the main languages of code.

Step 2: Filtering the PR's having only apache as the repository. This is due to the more processing time it used to take if we have all 356 PR's. In order to quicken the process and execution we have restricted our process with PR's of Google GitHub Repository only. 

In case we want all the PR's to be included we have to use the initial data frame in the initial block of code and avoid the Google Dataset which is currently being used. (Uncomment line 33 and comment line 30 in Assignment-3.py file)
Total No. of PR's used for this analysis: 88 (PR of apache repository)

### Input Data
The input file for the execution is the data.csv file present in data folder. The data.csv file was obtained from the Research Paper. We have used the column by name "Pull Request" present in data.csv for our process. We have utilized all the PR link and using the automated process to obtaine the title, comment, conversation etc..,

### Output Data
Result data which is executed and stored before already for a quick loopup by name finalResult.csv:

The result of the execution is stored in the finalResult.csv file which helps us in answering the Research Question 1 of the paper.

## Delta
### Process Delta
Our process includes the Effort of automation and involves more technical things of what the authors have done manually in the actual research paper. 
We have tried to answer the RQ1 of the paper quite effectively in finding the root cause, manifestation and category of the PR's. As part of RQ1 we have identified the characteristics of problems being addressed in RegEx related PR's. The columns "Root Cause", "Manifestation", "Category" have been identified with similar values as in the original paper.

But we were not able to continue the anaysis of the of RQ2 to the end as we require the credentials of the other PR's of other repo used by the authors. Plus it was a combursome task to fetch all the code and analyze if there was RegEx addition(RegEx Add) or RegEx Updation(RegEx Edit) or RegEx Deletion (RegEx Delete) or RegEx API changes in the PR. This is where we faltered and could not complete the reproduction of the RQ2, as a result of that we couldnt not suggest the 10 common fix patters to fix either a RegEx Bug or RegEx API Bug.

### Data Delta:
To understand if  bugs are similar in complexity to other software bugs, author have compared the regex-related PRs (regexPRs) with a public dataset of PRs from GitHub projects that use PRs in their development cycle. But we could't get the dataset of PR's from other projects as we reqired the credentials to be used in pygithub. 

We have managed to gather the details like number of commits, number of files changes and modified lines of code for the RQ2 analysis. But we failed to compare it with the PR's of other Repository
Like Wise we found it hard to get all the lines of code being addressed in every PR and then analyze those lines of code to get the common fix patters for the RegEx related Bugs.


# :pencil: Experiment

## Threat
In this assignment 3, we would investigate one of the threats to External validity found in "An Empirical Study on Regular Expression Bugs“ paper. The threat and the rationale behind it are as follows:

Authors have begun the study of this regular expression related PR's in order to identify and understand the problems developers face when they are using RegEx while in their development process. They have selected only repositories that have Java, JavaScript or python as the primary language. That resulted in 664 merged pull requests from 195 repositories from 4 different organisations. Finally, after pruning these 664 PR's and filtered out 356 PR's that are only related to **Regular Expression**. But these PR's that they have used was dated on or before 1st Feb 2019. 

Myself and my colleague have identified that this might be a possible threat to validity as we encountered new PR's were in the repository while doing our previous assignment. This threat is that additional pull requests may have been merged, and the existence of such pull requests would  effect our results if they substantially differ from the ones merged via GitHub. Which we also encountered in assignment 2 that some of the PR's were related to RegEx and some were not. Those PR might have different root cause or manifestations and might give us an altogether new perspective of our result.

## Traces
From the paper "An Empirical Study on Regular Expression Bugs" - under Threats to Validity

"External Validity": The PRs were sampled on February 1, 2019, and thus reflect the PRs available at a specific date and time. Results may not generalize to PRs sampled from a different period. We used GitHub’s merge status in selecting PRs, which poses a threat to validity [27]. This threat is that additional pull requests may have been merged, and the existence of such pull requests would affect our results if they substantially differ from the ones merged via GitHub. Further study is needed to assess the impact of this threat”. 

Here, we see that the author have mentioned the Threat explicitly and convey that the additional PR's that were merged after 1st February 2019 might change the research result substantially. Thus, we decided to conduct the same research on repositories dealing with RegEx related PR's merged after the quoted date of data collection.

## Feasibility
As stated above, there are too many repositories from the big 4 organisations that are involved in the research which indeed involves lot of manual work before identifying the new PR's related to RegEx and we have tried to automate those in this assignment. Since we are planning to have no language restriction as the original PR's are all filtered and have only 3 languages in them, this might be quite feasible for identifying the root cause and manifestation for those PR's. We will try to collect as many PR's as possible and come up with our new analysis. This might be a possible way to check whether the authors threats to validity can be falsified or if its still preserves.
This might be dependent on how many PR's we going to get and how many of them are related to RegEx and how many are still alive.

## :gear: Implementation

* We have automated the process which was manually done in the research paper. We have looped each and every PR's. Took the comments, conversations and title and analysed each of them with the Key word to form a Root Cause, Manifestation and category which was done in research paper. 

* Identified the 3 root cause and manifestation within each type of root cause successfully. Similarly each of the root cause is again carefully sorted into different category just like the authors have done in Research Paper. We have reproduced them and have the result stored in finalResult.csv file.

* We have first filtered the PR's of Google repository and have identified the PR's which are still alive and are taking us to github page. There were some PR's which lead us to 404 page error now. We even have displayed those PR's in console.

![alt text](https://github.com/AnoopKiranAM/Mining-Software-Repository/blob/main/images/404Error.JPG)

* As part of finding solution to threat that we have mentioned above we then found PR's that were raised or created after the date mentioned by author (February 1, 2019). We found very few PR's in this case there were not many of them in Google Repository. 

![alt text](https://github.com/AnoopKiranAM/Mining-Software-Repository/blob/main/images/date.JPG)

*To have the solution for the Threat we have added more key words in our detection of the Root Cause Manifestation and Category. We actually wanted to work with all the 356 PR's but the automation process was quite slow which delayed our findings. 

![alt text](https://github.com/AnoopKiranAM/Mining-Software-Repository/blob/main/images/keywords.JPG)

* This has indeed helped in identifying the root cause, Manifestation and category of each PR's and made our analysis more accurate of what the authors has done manually.

* We have taken few of the suggestion and inputs given in the reply post of our Second Assignment post by our fellow colleagues and have implemented few more key elements as part of the solution and solve the threat that the author had.

* Towards the end of the code execution we have depicted the 2 different results: one before the date (February 1, 2019) and one after the date (February 1, 2019) with our solution working fine for solving the Threat. We can see that the result is pretty much same with minor variations.


# :chart_with_upwards_trend: Result

* As part of the result, first we have to get the PR's which are created or updated on the specified date mentioned by author in threats. 

* We have identified those PR's and those which are dead for some or the other reason.

*The graph below show the result of the old execution and the current execution. 


![alt text](https://github.com/AnoopKiranAM/Mining-Software-Repository/blob/main/images/Graph1.JPG)

![alt text](https://github.com/AnoopKiranAM/Mining-Software-Repository/blob/main/images/Graph2.JPG)



* we can see that the results are pretty much similar and have almost the same number of commits, files changed and line of code edited in the newly obtained PR's

* We have used the Mann-Whitney-Wilcoxon Test to investigate whether the dataset, regexPRs, and the allPRs dataset have the same distribution with proper score. And as show below the result also depicts that we have low p score with the alpha value being 0.001, which shows that there is no significant difference between the samples.


```
# code for Mann-Whitney U test to test the number of commits in old and newly obtained data set

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
```

Result of Mann-Whitney-Wilcoxon Test: 

![alt text](https://github.com/AnoopKiranAM/Mining-Software-Repository/blob/main/images/mann.JPG)


* I have done the same test on 3 different columns of the results namely commits, lines of code edited and files changed to verify if we have the same result or not.

* I have represented the graph like above on lines of code edited columns as well and we can see the result is almost the same.

* We would like to conclude that the Threat the author mentioned was true but it didnt cause a major difference in the result.


# :blue_book: Requirements 

* The requirements for this task do not surpass the assignment 2.In fact most heavy processes take place in assginment 2.

* In the previous assignment we have jupyter notebook file as part of the reproduction effort. This time we have .py file and if the file is runned by any IDE like Pycharm or something then we need to install the packages before to avoid the error.

* The packages needed are mentioned in the requirements.txt file

* Other requirements are pretty much same in terms of hardware and software as before which includes:

    * ***Hardware*** : Windows, Mac or Linux operating system. Good and fast processor.
    * ***Software***: Anaconda, Python(pip install the required libraires mentioned below), Microsoft Excel, Pycharm

# :heavy_check_mark: Process

* The process pretty much remains the same as in Assignment 2 and will start off with installing all the softwares as mentioned in the requirements.txt file.

### Install below third party libraries using below commands.

* Install python 3.9.2 (mac) or for windows (https://www.python.org/downloads/)

* Install numpy 1.17.2 (pip install numpy==1.17.2)

* Install pandas 0.25.1 (pip install pandas==0.25.1)

* Install matplotlib 3.1.1 (pip install matplotlib==3.1.1)

* Install GitPython 3.1.0 (pip install Git Python==3.1.0)

* Install Beautiful Soup (pip install beautifulSoup4)

* ***Execution*** of the Assignment-3.py file will yeild the result which can be used for the detection of the Threats mentioned by author.


## Data
### Data-Preprocessing
Total No. of Pull Requests in the beginning: 356

* Filtering the PR's which has java, java script and python as the main languages of code (Which the author has done by himself we had a check again on that in the csv file)

* Filtering the PR's having only google as the repository.

* To have the new PR's in our solution to the Threat mentioned by Authors, we have filters all the PR's which were rasied after February 1 2019.

* We did have a filteration of those links which lead to 404 error for some reason. Those pages were not accessible so we had to filter them as well as shown above.


### Input Data
The input file for the execution is the [data.csv](https://github.com/AnoopKiranAM/Mining-Software-Repository/blob/main/data/data.csv)  file present in data folder. The data.csv file was obtained from the Research Paper.

### Output Data
Result data which is executed and stored before already for a quick loopup by name:  [finalResult.csv](https://github.com/AnoopKiranAM/Mining-Software-Repository/blob/main/data/finalResult.csv)

The result of the new execution done by the user is stored in the Result.csv file which helps us in analyzing the solution for the External Validity Threats mentioned in paper by Author






