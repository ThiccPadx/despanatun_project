0) You need PyCharm with PyCharm

1) from PyCharm run schengen.py or national.py 

2) Chrome window will open, you need to install 3rd party anticaptacha.crx (included) extension to it

2.1) Open Extensions (on that chrome window)
2.2) Enable Developer mode
2.3) Click Load unpacked
2.4) Select "anticaptcha" folder from project folder
2.5) Click Open
2.6) A logo with pidr in glasses should appear top right(anticapcha extension) click on it and find a fieald for account key field and enter your key then click save(at the very bottom)

3) Everything is ready you may test the alert sound by uncommenting playAlert() from source code. 


*) Every time you run the script first open the e-konsulat website, if it asks for a pre-captcha complete it, then make sure the language is set to English(One time is enough). Then press enter in the Terminal for the script to start.

*) To disable audio feedback for everything except when a place is found remove bash("spd-say " + text) line
#) The script will save log to logs/log.txt you can change log file in source code


