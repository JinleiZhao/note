# note
1、（先进入项目文件夹）通过命令 git init 把这个目录变成git可以管理的仓库

git init

2、把文件添加到版本库中，使用命令 git add 单个文件名或.代表所有

git add filename/.  

3、用命令 git commit告诉Git，把文件提交到仓库。引号内为提交说明，若没有新建的文件，则可以直接使用git commit -a -m ""跳过 git add

git commit -m 'first commit'    

4、关联到远程库

git remote add origin 你的远程库地址

如：

git remote add origin https://github.com/JinleiZhao/note.git

5、获取远程库与本地同步合并（如果远程库不为空必须做这一步，否则后面的提交会失败）

git pull --rebase origin master

6、把本地库的内容推送到远程，使用 git push命令，实际上是把当前分支master推送到远程。输入用户名和密码即可。

git push -u origin master

