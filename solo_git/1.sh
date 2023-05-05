mkdir git_repo_2
cd git_repo_2
git init .
touch numbers.txt
echo "4
5
6
7" >> ./numbers.txt
git add numbers.txt
git commit -m 'Added numbers.txt'

git checkout -b branch1234567
rm ./numbers.txt
touch ./numbers.txt
echo "1
2
3
4
5
6
7" >> ./numbers.txt
git add .
git commit -m 'Add more exciting numbers'
git checkout main

git checkout -b branch4567890
rm -rf ./numbers.txt
touch numbers.txt
echo "4  
5  
6  
7  
8  
9  
0" >> ./numbers.txt
git add .
git commit -m 'Another super exciting feature'
git checkout main
git merge branch1234567
git merge branch4567890

