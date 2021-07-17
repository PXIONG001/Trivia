#Line 2-4 opens programs to play music, display images, and display a chart
import matplotlib.pyplot as plt
import pygame
from PIL import Image


'''
    There will be at least 1 to 3 other functions. 
    Be advised, there will be more to come with other 
    features to come such as adding an account by adding
    a login feature.
'''

# play_the_game function plays the game
def play_the_game(entryfile, exfile):
    count = 0
    sum_correct = 0
    correct_sports_score = 0
    correct_movies_score = 0
    correct_history_score = 0
    correct_music_score = 0
    total_sports_score = 0
    total_movies_score = 0
    total_history_score = 0
    total_music_score = 0

    score = []

    found = False
    
    # The Trivia Begins with a for loop
    for num in range(len(exfile)):
        
        # Enter a file name that is within exfiles
        while True:
            #Asks the user to enter a trivia file to play
            file = input('Enter a trivia file to play: %s---> ' % (entry_file)).lower().strip()

            if file not in exfile:
                print('Invalid file name. Please choose one of the files listed to you to play!')

            else:
                break  

        #When entering a trivia file, the if statement, if true, removes the file in entry_file
        entry_file.remove(file) 
        num_question = 0
        mQuestion = []
        mAnswer = []
        Q1 = []
        Q2 = []
        Q3 = []
        Q4 = []
        Q5 = []
        questions = []
        secret_file = []

        #When while loop is true, the loop is activated to play the trivia file that you request
        while not found:
            infile = open('%s.csv' % (file),'r')
            allRows = infile.read().strip().split('\n') 
            infile.close() 
            found = True
                
            #This causes the file to get created into a list which also creates a nested list as well.        
            for row in allRows:
                if len(row.strip(' ,')) > 0:
                    line = row.split(',')
                    mQuestion.append(line[0])
                    mAnswer.append(line[1])
                    Q1.append(line[2])
                    questions.append(Q1)
                    Q2.append(line[3])
                    questions.append(Q2)
                    Q3.append(line[4])
                    questions.append(Q3)
                    Q4.append(line[5])
                    questions.append(Q4)
                    Q5.append(line[6])
                    questions.append(Q5)
                    secret_file.append(line[7])
            
            ''' Let's remodify this for loop with the if statements. We can try to make it much more shorter. '''
            
            #In this loop, the file input is now sent to this loop where it analyzes the input and chooses the correct if statement to play
            for index in range(len(mQuestion)):
                num_question += 1
                #This prints out the multpile choice answers
                print('%d. %s' % (num_question, questions[index]))
                
                #This plays the history trivia
                if file.lower().strip() == exfile[0].lower().strip():
                    #This opens the image which movies, sports, and historys all have. 
                    img = Image.open('%s' % (secret_file[index]))
                    img.show()
                    aQuestion = input('%s: ' % (mQuestion[index]))
                    if aQuestion.lower().strip() == mAnswer[index].lower().strip():
                        print('correct \n')
                        correct_history_score += 1
                        sum_correct += 1
                    else:
                        print('Incorrect \n')
                    total_history_score += 1
                
                #This plays the movie trivia
                if file.lower().strip() == exfile[1].lower().strip():
                    img = Image.open('%s' % (secret_file[index]))
                    img.show()
                    aQuestion = input('%s: ' % (mQuestion[index]))
                    if aQuestion.lower().strip() == mAnswer[index].lower().strip():
                        print('correct \n')
                        correct_movies_score += 1
                        sum_correct += 1
                    else:
                        print('Incorrect \n')
                    total_movies_score += 1
                
                #This plays the music trivia 
                if file.lower().strip() == exfile[2].lower().strip():
                    #This set of code plays the music and stops the music when the player enters a trivia.
                    pygame.init()
                    pygame.mixer.init()
                    pygame.mixer.music.load('%s' % (secret_file[index]))
                    pygame.mixer.music.play()
                    aQuestion = input('%s: ' % (mQuestion[index]))
                    pygame.mixer.music.stop()
                    if aQuestion.lower().strip() == mAnswer[index].lower().strip():
                        print('correct \n')
                        correct_music_score += 1
                        sum_correct += 1
                    else:
                        print('Incorrect \n')
                    total_music_score += 1
                
                #This plays the sports Trivia        
                if file.lower().strip() == exfile[3].lower().strip():
                    img = Image.open('%s' % (secret_file[index]))
                    img.show()
                    aQuestion = input('%s: ' % (mQuestion[index]))
                    if aQuestion.lower().strip() == mAnswer[index].lower().strip():
                        print('correct \n')
                        correct_sports_score += 1
                        sum_correct += 1
                    else:
                        print('Incorrect \n')
                    total_sports_score += 1
                
                count += 1

    # Once you finished playing the game, the next part 
    # will be getting a feedback on whether their should 
    # be some improvements on the game. Plus, the next part 
    # will give you a result for each categories and the total 
    # for all of the categories which will display a chart with 
    # your results.
    if found:
        review = input('Give us a review on what we can improve on this game, or if you want us to add some stuff into this trivia?')
        outfile = open('Reviews.csv','a') 
        outfile.write('%s' % (review) + ('\n'))
        outfile.close()
        
        historyAxis = float(int(correct_history_score/total_history_score))*100
        score.append(historyAxis)
        moviesAxis = float(int(correct_movies_score/total_movies_score))*100
        score.append(moviesAxis)
        musicAxis = float(int(correct_music_score/total_music_score))*100
        score.append(musicAxis)
        sportsAxis = float(int(correct_sports_score/total_sports_score))*100
        score.append(sportsAxis)
        total_score_Axis = float(int(sum_correct/count))*100
        score.append(total_score_Axis)
        app = 'total'
        exfile.append(app)
        plt.bar(exfile,score, color=['blue', 'red'])
        plt.xlabel('Trivia Categories')
        plt.ylabel('Correct Percentage')
        plt.title('Trivia Results')
        plt.show()



#Line 191-193 and line 195-197 opens the csv file and creates it as a list
infile = open('Exfiles.csv','r')
exfile = infile.read().lower().strip().split('\n')
infile.close()

infile = open('Exfiles.csv','r')
entry_file = infile.read().lower().strip().split('\n')
infile.close()

# A loop where the player can choose to play or not.
while True:

    do_you_want_to_play = input('Enter y or n to play the game: ')

    if do_you_want_to_play == 'y':
        play_the_game(entry_file, exfile)
        statement = False

    elif do_you_want_to_play == 'n':
        print('Goodbye!')
        break

    else:
        print('Invalid input! You must comply and enter either y or n!')