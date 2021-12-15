
# Table of Contents

1.  [Background](#org6d88e6c)
2.  [Examples](#org4d032c7)
3.  [Resources to use](#orgf76edbb)
4.  [Task](#org6109c0f)
5.  [Target Audience](#orgb6b8b35)
6.  [Technical Constraints](#orgc9f4e0a)
7.  [Evaluation Criteria](#org90e0ed1)



<a id="org6d88e6c"></a>

# Background

We have an eccentric Scrabble playing client who sometimes requests us to write software that can help them train for their Scrabble matches, and the client has a new request.

This time around, they would like to be able to run a specific program, that given a sentence, will replace each word in the sentence with another word starting with the same letter that is the same length. If a particular word can&rsquo;t be found that matches the criteria above, then the original word should be returned. Another requirement is that the same input should return a different output each time. Said another way, the word that is picked should be any random word that fulfills the criteria.


<a id="org4d032c7"></a>

# Examples

Given the sentence **lightly fried fish are delicious**, the program may return **likable frier frog arm delegated**. Running it again may yield **lenient fuses foam any digressed**.


<a id="orgf76edbb"></a>

# Resources to use

The client trains for his Scrabble matches using the 58000 word list here: <http://www.mieliestronk.com/corncob_lowercase.txt>. The solution should therefore use this same word list to generate the new sentences.


<a id="org6109c0f"></a>

# Task

Create a solution that will allow our client to input their sentence and get their desired output.


<a id="orgb6b8b35"></a>

# Target Audience

Assume the client is of moderate technical competence (for example they know how to paste commands into a terminal), but is not a developer themselves, so you should clearly explain how to get the solution working on their own machine.


<a id="orgc9f4e0a"></a>

# Technical Constraints

This is an open ended question that can be achieved with any technology or approach you are comfortable with, but since this is an evaluation for a development position, we assume that some code will be involved, so we require the solution to be submitted in the form of a git repository on a hosted source control platform like Github, Gitlab, Bitbucket etc.


<a id="org90e0ed1"></a>

# Evaluation Criteria

The purpose of this task is for us to understand the way you think and work and to allow us to get some insight into your technical abilities. Please do not spend more than a few hours on this task - perfection is neither expected nor desired, but a working (or almost working) solution is.

Good luck! If you have any questions about this task, feel free to get in touch with the person that sent this evaluation your way.

# Instructions for the User

Depending on the operating system you use will determine how the commands will
function.
   
   ##1. Click the link in the repository to clone the repository, select the http url and copy it.  Here is the url:

      https://gitlab.com/brsk-uk/technical-assessment.git
      
      
   ##2. Cloing the repository 
      In an IDE of your choice (I used Pycharm), you can either click on Version control if you downloaded the plug-in and clone the repository by pasting
      the link you just copied.  Alternatively, open up a new terminal, make sure you are in a directory where the repository you are about to download can
      exist.  Type in the following command in the terminal:
      
      git clone <paste the URL link you just copied>
      
      
   ##3. Activating the virtual environment 
      Once you've successfully cloned the repository, ensure you are in the directory called 'technical-assessment'.  Once there you can activate
      the virtual environment by typing in the following command in the command line:  
      
      source venv/bin/activate
      
      If for whatever reason you don't have all the software requirements then also run the following command:
      
      pip install requirements.txt
      
   ##4. Downloading the word bank 
      Change into the directory 'workbench'.  Then, run the following command:
      
      python3 create_file_of_scrabble_words.py  

      If you use Pycharm you won't need to run this command, once you open the file 'create_file_of_scrabble_words.py'
      there will be a little green arrow for you to click on to run it.
      
   ##5. Taking your time 
      Step 4 might take a bit of time to finish, it all depends on your hardware requirements and how fast your internet connection is.
      
   ##6. Playing the game 
      From within the same directory as in step 4, run the following command:
      
      python3 scrabble_game.py

      You will be asked to enter a sentence of your  choice, just type in the sentence and hit enter.  You will see that the sentence you typed in is displayed word for word as well as a new sentence with a replacement for each word, that is if a 
      replacement could be found, if not, the word itself is replaced by itself.

