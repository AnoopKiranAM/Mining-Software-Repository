# Mining-Software-Repository

## Baseline
The following parts are taken from assignment 2: This is a re-creation project of the original paper. “ An empirical study on Regular Expression Bugs” as a part of a course research “Mining Software Repositories (MSR 2020-21)” provided by Softlang Team at Universität Koblenz-Landau. -Anoop Kiran Angadi Manjunatha, Anirudh Kudaragundi Anand Rao.

## MetaData
This project describes the reproduction of the research paper “ An empirical study on Regular Expression Bugs” authored by: Peipei Wang, Chris Brown, Jamie A.Jennings, Kathryn T.Stolee.

In this project, we present an empirical study of 350 merged regex-related pull requests from Apache, Mozilla, Facebook, and Google GitHub repositories. Based on the classification the root causes and manifestations of those bugs,  we show that incorrect regular expression is the dominant behavior is the dominant factor for the cause of regular expression bugs.

DBLP Link: https://dl.acm.org/doi/10.1145/3379597.3387464

## Requirements
Hardware: Windows, Mac or Linux operating system. Good and fast processor.
Software: Anaconda, Python(pip install the required libraries mentioned below), Microsoft Excel.

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
Step 2: Filtering the PR's having only apache as the repository. This is due to the more processing time it used to take if we have all 356 PR's. In order to quicken the process and execution we have restricted our process with PR's of Apache GitHub Repository only. In case we want all the PR's to be included we have to use the initial data frame in the initial block of code and avoid the apache Dataset which is currently being used.
Total No. of PR's used for this analysis: 88 (PR of apache repository)

### Input Data
The input file for the execution is the data.csv file present in data folder. The data.csv file was obtained from the Research Paper. We have used the column by name "Pull Request" present in data.csv for our process. We have utilized all the PR link and using the automated process to obtaine the title, comment, conversation etc..,

### Output Data
Result data which is executed and stored already for a quick loopup:
The result of the execution is stored in the result.csv file which helps us in answering the Research Question 1 of the paper.

## Delta
### Process Delta
Our process includes the Effort of automation and involves more technical things of what the authors have done manually in the actual research paper. We have tried to answer the RQ1 of the paper quite effectively in finding the root cause, manifestation and category of the PR's. As part of RQ1 we have identified the characteristics of problems being addressed in RegEx related PR's. The columns "Root Cause", "Manifestation", "Category" have been identified with similar values as in the paper.
But we were not able to continue the anaysis of the of RQ2 to the end as we require the credentials of the other PR's of other repo used by the authors. Plus it was a combursome task to fetch all the code and analyze if there was RegEx addition(RegEx Add) or RegEx Updation(RegEx Edit) or RegEx Deletion (RegEx Delete) or RegEx API changes in the PR. This is where we faltered and couldnot complete the reproduction of the RQ2. Since we coudnt automate the process of fetching the code of every PR using the PR link, we couldnt not suggest the 10 common fix patters to fix either a RegEx Bug or RegEx API Bug.

### Data Delta:
To understand if  bugs are similar in complexity to other software bugs, author have compared the regex-related PRs (regexPRs) with a public dataset of PRs from GitHub projects that use PRs in their development cycle. But we could't get the dataset of PR's from other projects as we reqired the credentials to be used in pygithub. We have managed to gather the details like number of commits, number of files changes and modified lines of code for the RQ2 analysis. But we failed to compare it with the PR's of other Repo.
Like Wise we found it hard to get all the lines of code being addressed in every PR and then analyze those lines of code to get the common fix patters for the RegEx related Bugs.

## Threat
Authors have begun the study of this regular expression related PR's in order to identify and understand the problems developers face when they are using RegEx while in their development process. They have selected only repositories that have Java, JavaScript or python as the primary language. That resulted in 664 merged pull requests from 195 repositories from 4 different organisations. Finally, after pruning these 664 PR's and filtered out 350 PR's that are only related to RegEx. But these PR's that they have taken was on 1st Feb 2019 or before. Myself and my colleague have identified that this might be a possible threat to validity as we encountered new PR's were in the repository while doing our previous assignment. Some of the PR were related to RegEx and some not. Those PR might have different root cause or manifestations and might give us an altogether new perspective though.

## Traces
From the paper "An Empirical Study on Regular Expression Bugs" - under Threats to Validity
"External Validity. The PRs were sampled on February 1, 2019, and thus reflect the PRs available at a specific date and time. Results may not generalize to PRs sampled from a different period. We used GitHub’s merge status in selecting PRs, which poses a threat to validity [27]. This threat is that additional pull requests may have been merged, and the existence of such pull requests would affect our results if they substantially differ from the ones merged via GitHub. Further study is needed to assess the impact of this threat”. Here, we see that the author have mentioned the Threat explicitly and convey that the additional PR's that were merged after 1st February 2019 might change the research substantially. Thus, we decided to conduct the same research on repositories dealing with RegEx related PR's merged after the quoted date of data collection.

## Feasibility
As stated above, there are too many repositories from the big 4 organisations that are involved in the research which indeed have lot of manual work before identifying the new PR's related to RegEx. Since we are planning to have no language restriction this might be quite feasible as identifying the root cause and manifestation for RegEx related to a particular language will be quite tough. We will try to collect as many PR's as possible and come up with our new analysis. This might be a possible way to check whether the authors threats to validity have can be falsified or if its still preserves.
This might be dependent on how many PR's we going to get and how many of them are related to RegEx off course.

## Implementation
We have automated the process which was manually done in the research paper. We have looped each and every PR. Took the comments, conversations and title and analysed each of them with the Key word to form a Root Cause and Manifestation which was done in research paper. Identified the 3 root cause and manifestation within each type of root cause. Similarly each of the root cause is again carefully sorted into different category just like the authors have done in Research Paper.











