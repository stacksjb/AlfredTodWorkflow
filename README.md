# Alfred Tod Workflow
An Alfred (https://www.alfredapp.com) Wrapper for the TOD Application (https://github.com/alanvardy/tod) that allows you to quickly add tasks to your Todoist Inbox using Todoist Natural Language Processing

As it uses Natural Language Processing, you can add to any inbox, add any tag, or use any date that NLP accepts - for example, "Laundry tuesday @House #Cleaning p3" would create a task for Laundry, due tuesday, with the label of @House, in the project of Cleaning, and a priority of p3

Installation:
1) Install TOD using the steps found at https://github.com/alanvardy/tod
2) Configure your API key and timezone (run tod -l from the command line, following the prompts)
3) Install the Alfred Workflow
4) Create tasks with "Todo taskname", where taskname is the task in natural language input, for example 'clean my room on tuesday at 1pm p2' or 'call my Mom p1'
(See https://www.leightonprice.com/todoist/dates.html for some great examples)

All credit goes to @alanvardy and his great TOD CLI program (https://github.com/alanvardy/tod), which I found to create tasks extrememly quickly and effeciently - This is simply an Alfred wrapper to create tasks using that application.
