mkdir git_lab1_lesson2
cd git_lab1_lesson2
git clone https://github.com/YandexLyceum/human.git .
git branch -l
cat human.txt
git checkout -b boots_buttons
git merge origin/boots -m 'merge boots'
git merge origin/buttons -m 'merge buttons'
cat human.txt
git checkout master

git merge origin/hat -m 'merge head'
git merge boots_buttons -m 'merge botts and buttons'
git remote add coder8080_repo https://github.com/coder8080/human
git push coder8080_repo
git log

