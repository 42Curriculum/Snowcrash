# Snowcrash

This project is an introduction to the great wide world of security.

The project is separated in 14 levels, each accessible through a password.Each level is a new user and directory that you have to log into. Your goal is to complete all 14 levels. The passwords can be found using multiple techniques, most of them epxloiting the security flaws present in the level directory (whether it be a flaw in a program or a running background process or simply  not so well encrypted password file)

![](https://github.com/42Curriculum/Snowcrash/blob/master/snowcrash.PNG)

As of now I have completed all 10 normal levels + the 5 bonus levels, altough I haven't corrected this project yet.

It also turns out that the answer to the very last bonus problem is also a "general solution". For most of these levels, the password can be found by running the getflag executable. But it is unnacessible to you and you have to use loopholes through other programs or system tasks to acess it. The very last level requires you to use the gdb debugger to change the getflag progam and thus get the password.

