if file.lower().strip() == exfile[index].lower().strip() and file.lower().strip() != 'music':
    img = Image.open('%s' % (secret_file[index]))
    img.show()
    aQuestion = input('%s: ' % (mQuestion[index]))
    if aQuestion.lower().strip() == mAnswer[index].lower().strip():
        print('correct \n')

        if file.lower().strip() == 'movie':
            correct_movies_score += 1

        elif file.lower().strip() == 'history':
            correct_history_score += 1
        
        elif file.lower().strip() == 'sports':
            correct_sport_score += 1

        sum_correct += 1
    else:
        print('Incorrect \n')

        if file.lower().strip() == 'movie':
            total_movies_score += 1

        elif file.lower().strip() == 'history':
            total_history_score += 1
        
        elif file.lower().strip() == 'sports':
            total_sport_score += 1
