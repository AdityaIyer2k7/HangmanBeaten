For a more raw experience, use the "main" program. Do not edit the "words" and "masterletters" text files as they contain all the words and suggestions. For the complete and dusted experience, use mainSimple. You can make your own program with the functions in the "userTestProg.py" program.


--------Function information--------

Functions in userTestProg:

-wordsIn(): This function reads the words in words.txt and returns them in array form

-charCtrl(pos,charUp,charDown,lm,outPrint): This function finds words that contain correct letters in correct places. pos requires the position of the correct letter. charUp and charDown require the capital and small versions of the letters. lm requires the array of all the words. outPrint is a boolean variable that decides to print the number of remaining words or not. This function returns good words in array form.

-charRem(charUp,charDown,lm,outPrint): This function finds words that contain wrong letters and removes them. charUp and charDown require the capital and small versions of the wrong letters. lm requires the array of all the words. outPrint is a boolean variable that decides to print the number of remaining words or not. This function returns good words in array form.
