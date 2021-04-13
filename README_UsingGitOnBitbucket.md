# README for Using Git on Bitbucket

This README serves as an example of the documentation that is normally provided by software developers including scientists and engineers involved in computational science and engineering to document whatever steps are necessary to get your application up and running.

## Purpose
This repository is intended for downloading course sample files quickly and gaining familiarity with bitbucket and git.

## Setup
* Set up git for your operating system. https://www.atlassian.com/git/tutorials/install-git
* Create an account on bitbucket.org with your university email account. It is strongly recommended that you set your username to the part of your email address that precedes the @ sign.
* Set up your own git repository: https://confluence.atlassian.com/bitbucket/create-a-git-repository-759857290.html
* Open Git Bash in a specific file location and type the following
```
$ git init
$ git remote add origin https://username@bitbucket.org/hostusername/repositoryname.git
$ git pull origin master
```
where username is your personal username for bitbucket, hostusername is the username of whoever created the shared project, and repositoryname is the name of the repository. This should give you a copy of all of the files in this directory in your local folder where you where when you typed git init.
* You can repeat this process on multiple computers.

## How do I use Git on a regular basis?
```
$ cd C:/localdirectoryonyourcomputer
$ git status
# if anything has been updated local only
$ git pull origin master
# if anything local has not been added for tracking
$ git add filenamethatneedstobeaddedtoproject
# if anything needs to be saved to the Git repository
$ git commit -m 'Commit message indicating the purpose of the update'
$ git push origin master
```
