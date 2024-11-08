import numpy as np

def sentence_score(user_input,good_words,bad_words):
    """
    This function checks whether the user's messages were mostly positiv
    or negative based on the sentiment scores entered in the user's words.
    

    Args:
        user_input(str) : The last sentence entered by the user.
        good_words(ndarray) : Presentation of positive good words.
        bad_words(ndarray) : Presentation of negative words.

    Returns:
        score (int): The final score of the sentence
    """
    # Removes commas and periods for correct operation.
    user_input = user_input.replace(",", "").replace(".", "")
    # It separates the words from the sentence and puts them in the list.
    new_list = user_input.split()
    # It turns the list into a array
    new_array = np.array(new_list)
    
    score = 0
    
    # One point is added for each positive word and one point is reduced 
    # for each negative word, this is done by examining both the negative 
    #and positive words.
    for i in new_array:
        if i in good_words:
            score+=1
        elif i in bad_words:
            score-=1
    # Returns the final score of the sentence.
    return score


def final_message(final_score):
    """
    According to the final feelings after the whole 
    conversation, the user determines whether the 
    conversation was positive, negative or neutral 
    according to the score of all the messages.
    
    Args:
        final_score(int): The final score of the sentences

    Returns:
        conversation_status (str): Returns the conversation status.
    """
    
    # Checks if the score is higher than zero, 
    # the conversation is positive
    if final_score > 0:
        conversation_status = "positive"
    # Checks if the final score of the sentences is less 
    # than zero, the conversation is negative.
    elif final_score < 0:
        conversation_status = "negative"
    # Naturally, if it is not higher or lower, it is 0, 
    # so it is neutral.
    else:
        conversation_status = "neutral"
        
    return conversation_status


good_words = np.array(["great","happy","good","love","like",\
"excited","lovely","cute","dear","flower"])

bad_words = np.array(["bad","ugly","poor","nasty","sad",\
"depressed","hurt","pain","kill"])

final_score = 0

print("hello! welcome to my first NLP project!")
print("I hope you enjoy, enter 'exit' to stop the loop.")
while True:
    user_input = input("please enter a sentence =").lower()
    
    # Checks whether the user wants to exit or not.
    if user_input == "exit":
        # It sends the final score to be checked whether it
        # is positive or negative or neutral.
        message = final_message(final_score)
        print("the conversation state was", message)
        break
    else:
        # It sends the sentence to the function to check its score
        new_score = sentence_score(user_input,good_words,bad_words)
        final_score += new_score
