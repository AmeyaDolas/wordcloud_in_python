#!/usr/bin/env python
# coding: utf-8

# In[1]:


#ENTER LOCATION OF INPUT TEXT FILE in line 9


#import required libraries
import wordcloud
from matplotlib import pyplot as plt

#open the .txt file to be used to generate the word-cloud
file_contents=open("C:\\Users\\OWNER\\Documents\\textproject\\hp.txt").read() #enter location of text file
#file_contents is a BIG STRING OF ALL WORDS IN THE FILE INCLUDING ALL PUNCTUATIONS AND EVERYTHING ELSE. 
#It is a string of ALL file contents

def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i","for","he","she", "me", "my",     "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them",     "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being",     "have", "has", "had", "do", "does", "did", "but", "at","us", "by", "with", "from", "here", "when", "where", "how",     "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor","in","on", "too", "very", "can", "will", "just"]
    
    
    
    #step 1 : create a new string of the whole file by skipping all punctuations.
    #step 2 : create a list of all words by using the new string created
    #step 3 : create a new list of all words which are lowercase. Use the list in step2 to create this new list by converting 
    #each word in that list to lowercase and appending it to the new list
    #step 4 : create a new list by appending words of list in step3 to this new list. skip all uninteresting words and numbers.
    #to check if a word is a number use isnumeric() function.
    #step 5: using the final list in step 4, create a dictionary which consist of word-frequencies, i.e, how many times each
    #word appears in the final list. Name this dictionary as 'freq'
    #step 6: execute the code
    strr=str(file_contents)   #text file converted into string in variable strr
    
    punc=list('''!()-[]{};:'"\,<>./?@#$%^&*_~''')  #created punc containing list of punctuations
    
    #step1
    for i in punc:
        strr=strr.replace(i,'')
    newstrr=str(strr)
    
    #step 2
    l1=newstrr.split()
    
    #step3
    l2=[]                   #created new list l2 which contains elements of l1 in lower case
    for i in l1:
        l2.append(i.lower())
    
    #step4
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i","for","he","she", "me", "my",     "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them",     "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being",     "have", "has", "had", "do", "does", "did", "but", "at","us", "by", "with", "from", "here", "when", "where", "how",     "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor","in","on", "too", "very", "can", "will", "just"]
    l3=[x for x in l2 if x not in uninteresting_words]  #created list l3 which does not contain unintresting words
    
    final_list=[x for x in l3 if not x.isdigit()]       #created list final_list which does not contain digits
    
    #step5
    freq=dict()
    for i in final_list:
        if i in freq:                                #created dictionary freq which contains frequency of each key
            freq[i]=freq[i]+1
        else:
            freq[i]=1
    
    

    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(freq)
    return cloud.to_array()

myimage = calculate_frequencies(file_contents)
plt.figure(figsize=(50,80))
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()


# In[ ]:




