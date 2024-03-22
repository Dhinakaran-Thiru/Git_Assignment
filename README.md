# GitRepo-assignment
Question 1
*At first i have created new repository in github file,In that i create a new file and commit changes(git commit -m "messages")
*then,i viewed that commit history --
*i open the same file in pycharm terminal make some changes in it ,then commit and push it to remote repo
*i used git status to check my file is modified or not
*After i edited the same document in that remote repo and commit changes 
*then in local repo i fetched the changes then i pull the file from the remote repository

Question 2
*i just clone that repository using git clone "https://file link"
*then i created new branch using git checkout -b newbranch-it will switch to the new Branch
*after i added new file in local repository using notepad question2.py
*then commit changes to the new branch and push it to the remote repo and 
*switch back to main branch using git checkout main
*after i merged using git merge 
*then i used git pull to check whether any other files are addded
*then i commit changes  and push it to the original branch

Question 3
*At first i have created new feature branch using git checkout -b newbranch1
*it switched to new branch ,there i created one file ,add and commmit the changes to the new branch
*i pushed that to that new branch.Atfer i created pull request in remote repo and merge repo
*in main branch there i used same file and edited it,add and commit the file in the master branch
*then i try to push the file (pull request conflict) there i am using git rebase) there i can using (pull git) then adding the same files(git add .),then commit and then i pushed the same file in main branch.

Question 4
*i created a feature branch  using git checkout -b switching into another branch i edited the same files 3 times and commited to the every single time on the feature branch
*then i am using git log to check for commit id ,after that i am coming into the main branch after i cherry picked using  git cherry-pick commit id

Question 5
*create a feature branch and switch to the new branch,IN that i created new file and i edited three times and commited changes in it
*then i use git log command to search for commit id ,using that commit id i done my git revert commit id and git reset commit id
