date=`date`
/usr/bin/git add .
/usr/bin/git commit -am "$date"
git pull --rebase origin master
/usr/bin/git push
