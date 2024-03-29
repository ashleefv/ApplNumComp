# **Lesson 1: Git for Version Control**

This lesson focuses on Git for version control.

Note: the instructions are provided for using Bitbucket as the site for hosting version control repositories. Alternatively, GitHub may be used instead.

## **Motivation for Version Control**
["Final".doc](http://phdcomics.com/comics/archive_print.php?comicid=1531)

## **Instructional Videos**

* [Git and Bitbucket](https://www.youtube.com/watch?v=3KS6TaJPeHo&feature=emb_title)

[![](http://img.youtube.com/vi/3KS6TaJPeHo/0.jpg)](http://www.youtube.com/watch?v=3KS6TaJPeHo "Bitbucket")

* [Linking to Bitbucket repositories](https://www.youtube.com/watch?v=euEwNW4v82M&feature=emb_title)

[![](http://img.youtube.com/vi/euEwNW4v82M/0.jpg)](http://www.youtube.com/watch?v=euEwNW4v82M "Linking Local Folder")

* [Standard Git commands](https://www.youtube.com/watch?v=rfBZTlGImg8&feature=emb_title)

[![](http://img.youtube.com/vi/rfBZTlGImg8/0.jpg)](http://www.youtube.com/watch?v=rfBZTlGImg8 "Daily Git Commands")

## **Set Up Version Control Software: Git and Bitbucket**
* Create an account on bitbucket.org with your university email address (this allows for unlimited private repositories as a default). 
* [Download and install Git following the online instructions](https://www.atlassian.com/git/tutorials/install-git). Note the instructions include how to configure your username and email address AND how to automatically save your password (credentials). These are often overlooked but are really helpful. 
* Create two empty folders on the computer that are completely dedicated to tracking personal computational assignments and synchronous class activities. Do not put other class files or personal files in these folders. Also, do not put one of these folders inside the other.
    - Folder 1: name it FirstnameLastnameApplNumComp (change firstname and lastname to own name). ApplNumComp is a shortened reference to our course name. Students will control everything in this folder and submit their homework through this folder.
    - Folder 2: name it CHEclassFa20. This folder is how to share coursenotes, examples, problems, etc. In class activity files are shared in this folder. Course instructor controls this shared folder.
* Follow [these instructions](https://support.atlassian.com/bitbucket-cloud/docs/create-a-git-repository/) to create a sample Bitbucket repository.
* Create a Bitbucket repository. It is recommended to name it the same as the first folder created on the local device. In general, these names do not have to match, but it is really helpful when you are getting started or if you anticipate have several version controlled folders.
* In the CHEclassFa20 folder on your computer, open Git bash there or use cd to change directory to get to that folder. Then type the following commands (case-sensitive) to link to Dr. Ford Versypt's online repository for sharing in-class problems.
```
$ git init
$ git remote add origin https://username@bitbucket.org/ashleefv/CHEclassFa20.git
$ git pull origin master
```
* If you get an error about the repository not existing, check that you've inserted your username correctly (capitilization, punctuation, and spelling all matter for this to work properly). Type the following to reset, the try the second and third commands above again.
```
$ git remote rm origin
```
## **Reflection**
  * Do you have any experiences like that pictured in the ["Final".doc](http://phdcomics.com/comics/archive_print.php?comicid=1531) cartoon? If so, briefly describe one of your experiences. If not, why might an experience like this be challenging?
  * Did you encounter any challenges or errors in the Set Up Version Control Software section?

## **Activity**

* Using your bitbucket.org account, go to the repository named FirstnameLastnameApplNumComp (change firstname and lastname to own name, and ApplNumComp to own version of shortened course name). This should have been created previously.
* Setup the repository to have a local directory on personal computer and connect the local directory to the online repository.  
* Open Git Bash in a specific file location and type the following
```
$ git init
$ git remote add origin https://yourusername@bitbucket.org/yourusername/repositoryname.git
$ git pull origin master
```
where yourusername is your personal username for bitbucket and repositoryname is the name of the repository exactly as you created it (capitalization, punctuation, and spelling matter). This should give you a copy of all of the files in this directory in your local folder where you where when you typed git init.
* Create a new subfolder called Practice in your FirstnameLastnameApplNumComp folder on your computer.
* Add any document or image file (preferably a small file) to the FirstnameLastnameApplNumComp/Practice folder.
* Get this file into your FirstnameLastnameApplNumComp repository on bitbucket.
* Can't get this to work? [See tips here](https://github.com/ashleefv/ApplNumComp/blob/master/README_UsingGitOnBitbucket.md#how-do-i-use-git-on-a-regular-basis). Still not working? Contact Dr. Ford Versypt.
  
## **References for Further Exploration**
* [README for Using Git on Bitbucket](https://github.com/ashleefv/ApplNumComp/blob/master/README_UsingGitOnBitbucket.md)
* Basic to advanced Git features and commands: https://git-scm.com/book/en/v2
* [Quick intro to UNIX shell commands](https://swcarpentry.github.io/shell-novice/reference/)
* J. D. Blischak, E. R. Davenport, and G. Wilson, A quick introduction to version control with Git and GitHub, PLoS Computational Biology, 12(1):e1004668 https://doi.org/10.1371/journal.pcbi.1004668
* For more practice see the [Software Carpentry Git Tutorial](http://swcarpentry.github.io/git-novice/)

## **Next Lesson**
  * [L02 LaTeX Basics](/L02%20LaTeX%20Basics.md)
