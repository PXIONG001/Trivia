if file.lower().strip() == exfile[index].lower().strip() and file.lower().strip() != 'music':
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