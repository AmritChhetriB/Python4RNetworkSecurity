	Created by Amrit Chhetri, Cyber Security Researcher,Rosefinch
	-----------------------------------------------------------------


Create a new Baseline repository
======================================================
echo "# Python Forensics" >> PythonForensics-Readme.md
git init
git add *.*
git commit -m "Sample commit"
git branch -M main
git remote add origin <URL>
git push -u origin main
git push origin main --force

Adding new folder and contents in specified location
====================================================
git add Datasets/*.*
git commit -m "Folder commit"
git branch -M main
git remote add origin <URL>
git push -u origin main

Committing only changes- ALL CHANGES:
=======================
git add *.*
git commit -m "Folder commit"
git branch -M main
git remote add origin <URL>
git push -u origin main


Committing only changes- Specific:
=======================
git add Datasets/*.*
git commit -m "Folder commit"
git branch -M main
git remote add origin <url>
git push -u origin main

Free References:
1. https://git-scm.com/doc


