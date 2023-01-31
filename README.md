# Movie_recommender_system

this is the Movie Recommendation Project Which uses the Content Based Recommendation System

#for Ex: there are three Type of Recommendation system.
    
    1.Content based -->  recommendation on the bases of content. 
    2.Collaborative based --> recommendation on the basis of similarity of Viewer.
    3.Hybrid --> combination of both Content based and Collaborative based , Now the companies like youtube , amazon uses the Hybrid approach.

#Take dataset of top 5000 movies on TMDB from kaggle.
  
  perform the preprocessing using PANDAS and NumPY like making the data suitable for Vectorization remove the null values etc.
  
#I use the Text Vectorization in the project with the help of Sklearn
   
    CountVectorizer is a great tool provided by the scikit-learn library in Python. It is used to transform a given text into a vector on the basis
    of the frequency (count) of each word that occurs in the entire text.
    Bag of words technique.
  
#Perform the stemming to reduce the dimension of data with the help of from porterStemmer
  
  The Porter stemming algorithm (or 'Porter stemmer') is a process for removing the commoner morphological and inflexional endings from words in English.
  
  
#For finding the Distance Between Each vector I use the Cosine distance in place of Euclidean distance because 
  
  At high dimensions, Euclidean distance loses pretty much all meaning. However, it's not something that's the fault of Euclidean distance in particular
  
#For converting Model to website I use the streamlit 
    
    Streamlit is an open source app framework in Python language. It helps us create web apps for data science and machine learning in a short time. 
    It is compatible with major Python libraries such as scikit-learn, Keras, PyTorch, SymPy(latex), NumPy, pandas, Matplotlib etc.
    
  this was my whole project please give star if you like the explanation  
