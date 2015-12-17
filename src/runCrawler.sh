#!/bin/sh
nohup python3 crawlerApp/SocialStatisticGetter.py > social_getter.txt 2>&1&
while(true)
do
	nohup python3 crawlerApp/CrawlerApp.py > crawler1.log 2>&1&
	nohup python3 crawlerApp/CrawlerApp2.py > crawler2.log 2>&1&
	nohup python3 crawlerApp/CrawlerApp3.py > crawler3.log 2>&1&
	nohup python3 crawlerApp/CrawlerApp4.py > crawler4.log 2>&1&
	nohup python3 crawlerApp/CrawlerApp5.py > crawler5.log 2>&1&
	sleep 3600
done
