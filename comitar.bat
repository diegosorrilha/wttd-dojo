echo %date% %time:~0,8% - %1 e %2 >> dojo.log
git add .
git commit -am "%1 e %2"
git push origin master
