Multifaceted Helper
===================
VERSION 1.0

Let's start with the main thing. Namely, the .env.
If you just downloaded the repository from github, rename .sample_env to .env. and sample_data.json to data.json.


Setting up the .env
1. Change to the file
2. In the NAME field, specify the name of your assistant (this is the name by which it will respond without it, it will not execute any command)
3. In the THRESHOLD_NAME and THRESHOLD_COMMANDS fields, specify the percentage of similarity. In the first case, the name in the second command. This is necessary in case you have a bad microphone or the system cannot correctly decipher what you said, this setting will help the code understand what you may have meant. In general, I advise you to leave this parameter untouched, increase it to a maximum of 80-90
4. In the COMMANDS field, you have a link to a file with commands. If you do not understand this, I advise you not to touch it
5. In the API_WEATHER field, specify your api key from the site https://openweathermap.org/api
6. There are 2 parameters in the SAVE_SCREENSHOT field. Parameter 1 determines whether to save the screenshot to the clipboard. 2 parameter determines whether to save it in a folder (the folder is located in the same folder as the source files sample_data.json and .sample_env)
7. The TRANSLATED_TEXT field in this field you need to specify the language into which to translate the text (by default, UK (Ukraine) I advise you not to change)
8. LOGGING_FILE field this field determines whether to log data to a log file (sometimes useful if a bug occurs)

Translated with DeepL.com (free version)

Setting up the data.json
1. You see the key/value
For example, for the example OPEN_BROWSER is a key and the dictionary in which something else is written is the value. Roughly speaking, OPEN_BROWSER is a category
2. It is strictly forbidden to change the category!!!
3. In order to add your own command, just replace the text ‘command for ...’ with the one you want. in another field followed by ‘:’ you need to specify other data (what these data depend on the field, so read carefully!)
4. If there is a note in another field (you can create several), it means that you can create many commands of the same type in this group. For example, if you take the group from the example of paragraph 1, you can create many commands, for example, to open YouTube, telegram, moodle and more