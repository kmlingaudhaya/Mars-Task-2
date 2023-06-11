# SUMMARY OF TASK #2 
## **Table of contents**
1. Search Modify and Copy
2. Append Date and Time
3. Password Generation
    1. Methode 1
    2. Methode 2
4. Transposer
5. Robot question.
6. Pixal Percentage Calculator
7. Black and White
<hr>

## SEARCH MODIFY AND COPY

In this quesiton, I basically learned how to 
1. Read user input 
2. Check the existence of directory
3. File manipulation
4. Echoing message
<hr>

## APPEND DATE AND TIME

Learned to use the current_date command which displays the date as mentioned below.

current_date=$(date +"%Y-%m-%d %H:%M:%S")
<hr>

## PASSWORD GENERATER

Here in this question I was asked to generate a random password in two different ways.
1. First case I defined a character set containing the required characters. In the code I have included all alphabets and numbers, but it can be just alphabets or just numbers as per our requirement.The shuf command is used to randomly shuffle or sample input lines. In this case, it shuffles the lines containing individual characters randomly.
2. In the second case, I used openssl command to randomly generate bytes and convert them into hexadecimal format.
<hr>

## TRANSPOSER OF A MATRIX

IFS stands for Internal Field Separator.By default, the value of IFS is set to a whitespace (space, tab, and newline) character. When a command or input string is processed, Bash splits the input into fields using IFS as the delimiter.
<hr>

## PIXAL PERCENTAGE CALCULATOR

To execute this, I have imported the matplotlib library.

In the line height, width, _ = labrat.shape, the .shape attribute of the labrat matrix returns a tuple representing the shape or dimensions of the matrix. The tuple contains three values:

height: This corresponds to the height of the image, representing the number of rows in the matrix.

width: This represents the width of the image, indicating the number of columns in the matrix.

The underscore _ is a conventional placeholder variable used to disregard the third value in the tuple. In this case, the third value represents the number of color channels (typically 3 for RGB images). Since it was not relevent, i just ignored that.

r > threshold[0] and g > threshold[1] and b > threshold[2] , later we access each pixal using nested loop and compare them with the threshold values and assign their type accordingl in the list pixal types.

typeA_percentage = (pixel_types.count('typeA') / total_pixels) * 100  - In this line we calculatee the percentage of pixal A in the image. And later we print the obtained value.
<hr>

## BLACK AND WHITE

(0.21 * r + 0.72 * g + 0.07 * b) - Brightness is defined by the above expression. And I chose 160/3 as my reference brightness level.

        if (0.21 * r + 0.72 * g + 0.07 * b) / 3 > brightnessLevel:
        
            modified_labrat[i, j] = [0, 0, 0]
            
        else:
        
            modified_labrat[i, j] = [255, 255, 255]
            
And later using nested for loop, I iterate over each element and determine if the brightness level is more than my chosen level or not. If it is more, I change the pixal color to black, else change the pixal color to white.  
<hr>

## CLONING REPOSITORIES

    git clone <paste the url of the required repository>
    
## PUSHING INTO GITHUB USING TEERMINAL

First we move the required file to the current working git directory. That can be done using
    
    mv question1.sh question2.sh question3.1.sh question3.2.sh question4.sh question5.sh question6.py question7.py <address of the local git directory where you want to move the file>
    
First navigate to the directory where your all files are present and then move the files from there. 

### ADD COMMIT AND PUSH

Next we use the command,
    
    git add *
The git add command adds a change in the working directory to the staging area. It tells Git that you want to include updates to a particular file in the next commit.   

Next we commit the changes using 

    git commit
This prompts you to enter a commit message.

And finally we push the file to the remote directory using 

    git push
    
 <hr>  
 
 ## SCREENSHOTS OF HOW I PUSHED MY FILES TO GITHUB USING TERMINAL COMMANDS

Creation of a local folder

![Screenshot from 2023-06-10 22-26-05](https://github.com/kmlingaudhaya/Mars-Task-2/assets/134930329/08f87076-a98f-45f5-9a36-761c844caaa3)

Using the above mentioned git command to clone the repository locally to the folder that was created in above step.

![Screenshot from 2023-06-10 23-41-59](https://github.com/kmlingaudhaya/Mars-Task-2/assets/134930329/f001c866-f224-4391-89f0-ebf525b73d12)

And using add, commit and push command we can push the files to github.

![Screenshot from 2023-06-10 23-42-54](https://github.com/kmlingaudhaya/Mars-Task-2/assets/134930329/d525e052-8062-4f05-9764-58a40e595055)
