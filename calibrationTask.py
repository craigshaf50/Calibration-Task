# -*- coding: utf-8 -*-
####################################################
# author: Craig Shaffer
# date revision: 8/31/21
# course: CPSC 363
#
# Calibration Task:
# Takes name, outputs goals for the class
# Takes week number, outputs the date of the monday of that week
#
####################################################

import sys

#initialize variables
option=0 
tempVar=''

#Dictionary with class members and their goals
class_goals={'Craig Shaffer':"Going into this semester, I have taken two computer science courses through Grand View and a simple Principles of Computer Science course in high school. Despite my lack of coursework in the subject, I have practiced building my own projects away from school as a way of improving my skills. Not knowing any of the development processes or correct paths to take, I have been able to recreate simple games like Snake as well as a few larger projects that I hope to go back and improve. \n\t My main goal for this class is to learn more about developing software from start to finish and how to maintain/improve it. By the end of this course, I’d like to be able to make my own small projects and improve on ones that I have started. For example, last year I started working on a fantasy football analytics tool. Right now the functions are basic and can plot player data to compare with the rest of the league. Hopefully, by the end of the semester, I’ll be able to add new features and streamline the development process for these projects. \n\t Another goal I have is to become more confident. I want to have confidence in my abilities and confidence in working in teams. I think working with others will be a huge skill to have when I reach the job market. Practicing programming and communicating with a team will allow me to be more proficient in those areas. By improving, I feel that I will be more confident in myself and my abilities. \n\t Comparing these two main goals with my classmates, there is a lot of overlap. Nearly everyone in the class wants to learn the development process for software for the first time or to learn something new about the development process. Another common theme was confidence in general. Whether it be in a team setting or just in their own abilities, it got brought up several times in the class discussion. Improving in these areas seems to be the main thing the class wants to accomplish in CPSC 363. \n\t Outside of these two, I think that time management and not getting stressed are definitely goals I should look to work towards. Being able to properly time out my tasks and projects will benefit me in the present, as well as later in life. Being able to keep a schedule and time things out will also keep me less stressed. If I know how long things should take I can better plan my work and get more done. The more I can get done the less I have to stress about. I think that these goals should be worked on in every class and not just this one. \n\t Overall, I think that I just want to come out of this course with a better understanding of software development and improve my confidence. I think these are two important areas for my future career in the software-dominated world. If I come out of the semester with these two things, I would consider the semester a major success and be happy with the outcome.",
             'Josue Chigwira':"I want to be able to write software at the end of this semester. I also want to learn new things about software that I do not currently know, like what languages are easy to use to write software. This semester, there are some classes that I am taking because I have to take them or to bring up my credits to full time. This class will help me decide what I want to do with my computer science major after graduation. In some other classes I see success as getting passing grades but in this class success expanding my knowledge and helping decide what I want to do in the future.",
             'Morgan Gant':"Over the summer I took an Intro to Data Science class and it made me want to become a data scientist. I learned that Data Scientists work in teams and the most successful Data Scientists know how each element of their team works. So even though I’m not the most interested in Software development, having knowledge in this area will help me be a better team leader and make my job easier. I also think that having many skills is important so if I can gain software development skills it will make me more well-rounded, a better asset. To make this happen, I want to learn the basics of Software Developing because I know absolutely nothing about it. This includes the different types of software, the history of software, the life cycles, common challenges and any other interesting aspects I learn along the way! This will be the most beneficial if I better my relationships with others in the class. I feel we can learn just as much from our peers as we can a professor, especially when classmates that have personal experience in the field. I have had class with some of these students before but the classes weren’t very interactive so I didn’t get to gauge what knowledge they have to offer. We talked about soft skills like teamwork and communication and the only way to improve on them is to implement them! So, my overall goal is to understand the basics and learn how I can apply it to better myself in my desire of becoming a Data Scientist! \n\t I am a really organized person and work very hard on my schooling. I like to know things ahead of time so I can plan accordingly and I always try to get my work done as early as possible to avoid being stressed. Life does not run on a schedule though, so I know things will change and I will get things thrown at me that might cause panic but if I can accomplish my work in a reasonable timely manner and show my growth throughout the course, I feel that I will be successful no matter what this semester brings.",
             'Evan Callaghan':"For me, success in this class is all about my understanding of the subject matter and being able to take some key ideas away to use in the future. Ideally, I would gain a broad understanding of software development, learn how it is implemented in the real world (workplace), and learn how it can be applied in the field of data analytics. In addition to this, gaining programming experience and improving my soft skills will also help to define success in this course. Working with a team has never been my strong suit, so improving this skill and being able to collaborate with my groupmates will be a great measure for success. \n\t Throughout my time in university, I’ve found that sometimes the idea of success gets linked to the overall course grade. I have had plenty of courses where I achieved a good course grade but wasn’t able to really utilize or remember the content even a few weeks down the road. Even though I had a good grade, I didn’t learn anything that really stuck with me. On the other hand, my favorite classes and the classes that I’ve enjoyed the most are the ones where I learned every single day. These classes are the ones in which I am always engaged in class, always interested in the course content, and always learn useful content that will help me in my future career. Therefore, to me, success in this software development course looks like: gaining a broad understanding of the subject matter; always trying my best to be engaged in class lectures and discussions; learning about how this content will be helpful in my future career path; and collaborating with teammates/groupmates to build my skills in working as a member of a team. \n\t Within a particular course, there are always specific sections or topics that I struggle with more than others. In these tougher weeks, I am not able to participate as much in class or contribute as much to the conversation. Sometimes, this gives me the impression that other students are having more success than I am. I question why I am struggling so much and become anxious in the classroom. However, I have come to realize that success cannot be measured only the one way. I know that there will be topics that I struggle with, but at the end of the course, it is in achieving my end goals above that will signal whether or not I was successful in the class. Sometimes the impression of success is not always accurate, and success can be measured in many different ways.",
             'Madeline Edmonds':"When thinking of success, my definition will always be accomplishing a goal that I have set for myself. These goals can be very specific or broad statements of goals I have set for myself over the semester. \n\t For Software development one of the goals I planned for myself was that I could take the materials I have learned in class and apply them in a professional setting. Many technology facing companies are looking for graduates that can apply pieces of what they learned in an interview while providing real life examples. I want to show y future employers that not only was I a good learner, but I understood what was given to me and how it was used. \n\t Another goal I had was that I wanted to communicate more with my fellow students and build on my teamworking skills. Throughout my time at Grandview I have worked in group projects over Zoom and emails, but I would also like to spend more time in an in person setting. Since I see most of these other students in other classes I want to get to know them more. \n\t My final goal is what I would consider a broad goal of my semester. I want to pass the class with a good grade and have a solid understanding of Software Development to the point that it could open a new field of interest as I pursue internships and jobs. I want to succeed both in grades and personal growth",
             'Jackson Nguyen':"After this course, I expect to learn be able to write the most basic software, not giving up when solving problems especially when it comes to writing code, improve teamwork and communication between each other and be able to define and breaking down tasks into subtasks to help me understand it better, to do it better. So even thought I’m not interested in Software development, but I’m required to take it, having knowledge in this class will help me in the future career and make my job easy.",
             'Danh Tran':"After this course, I expect to learn many things related to developing a software. Software development life cycle (SDLC) is one of them. As I know, SDLC is very important in current software development, and it is a must-know for every developer. Beside SDLC, the frameworks that support SDLC are also of importance. I guess there are frameworks for analyzing, coding, testing, and deploying software. There are many of them. There are frameworks that support SDLC such as Scrum or RAD. Knowing about them could be helpful for finding jobs as a software developer. If we could go further and get to know the popular tools and the trends, the knowledge is helpful for future job security.\n\t Soft skills and experience are also my expectations for the outcome of the course. Putting hands on a project, working with others, and solving problems that arise are beneficial not only for software developers but for all occupations. I hope to experience the software development process. Along the way, collaborating with and learning from others are also anticipated. Nowadays, software projects need a group or groups of individuals to work together, so I want to harden my teamwork skill to be well-prepared for the future. Presentation skills are good to have, and I also think they can be improved during group work and course work.",
             'Gideon Kime':"As far as this class is concerned, success for me will be to successfully achieve the goals of this class, which are to be conversant with software development concepts and practically being able to apply what I have learned in the real world, and of course, to pass with flying colors",
             'Jacob Thomas':"I hope to learn a bunch of new skills and information and apply that knowledge into future circumstances. Also, I wish to not stress out over the class if I am confused on something I don’t know.",
             'Jacob Hillaker':"In this class, I would like to become more confident with the software development process. I want to gain proficiency in timing my tasks and better judging how to divide up my work. I want to develop good actionable tasks with clear success criteria. Additionally, I want to increase my teamwork and communication skills. I would also like to get better at testing my programs. In the end, I would like to just be overall better and more confident in my work",
             'Nick Jones':'Learn to independently develope a basic program, apply myself, and meet one other person',
             'Grant Gonnerman':'By the end of the semester, I hope to understand all the topics that were covered in the class and expand my knowledge and skills in software development and coding so I can be prepared to be successful as I go on in my major and onto a career.',
             'David Beehler':'I am auditing this course to learn something I do not know, expand on, or enhance, some things I think I may know and get new perspectives by looking at things from other students point of view.',
             }

#Dictionary for weeks and dates
week_dates={'1':'8/23',
            '2':'8/30',
            '3':'9/6',
            '4':'9/13',
            '5':'9/20',
            '6':'9/27',
            '7':'10/4',
            '8':'10/11',
            '9':'10/18',
            '10':'10/25',
            '11':'11/1',
            '12':'11/8',
            '13':'11/15',
            '14':'11/22',
            '15':'11/29',
            '16':'12/6'}

#stops the infinite loop
def exit_application():
   print("Exiting the application...")
   print("---------------------------------------------------")
   sys.exit() #function call to quit the code

#displays the all the entries in the class_goals dictionary
def display_class_goals():
    print(class_goals)
    print("---------------------------------------------------")
   
#infinite loop to display options for user
while(True):
   print("CPSC 363 Calibration Exercise")
   print("Option 1 - proceed to class goals")
   print("Option 2 - proceed to Mondays of the semester")
   print("Option 3 - exit application")
   
   #gets the user input for choice of function
   option = input("enter your choice >> ")
   #to exit the application/stop the code
   if (option == '3'):
       exit_application()
   #to print dates of the monday of each week
   elif (option == '2'):
       tempVar=input("Enter the week of the semester >> ")
       if (tempVar in week_dates):
           print("The date of the Monday in week", tempVar, "is", week_dates[tempVar])
           print("---------------------------------------------------")
       else:
           print("Error: The week does not exist in this semester")
           print("---------------------------------------------------")
   #to print goal statments of students
   elif (option == '1'):
       tempVar=input("Enter the name of the person's goal statement you want to access >> ")
       if (tempVar in class_goals):
           print("The goal statement of the student (", tempVar, ") is:\n\t", class_goals[tempVar])
           print("---------------------------------------------------")
       else:
           print("Error: The person does not exist in the class or was not entered correctly")
           print("---------------------------------------------------")
   else:
       print("Your input is invalid. Please enter either 1, 2, or 3 to choose an option")
       print("---------------------------------------------------")

   
   