In order to run nlp_1(no_stem) you need to download dataset csv file which is output_no_stem.csv( first dataset after cleaning) , then you should run all cells .

In order to run nlp_1 you need to download dataset csv file which is output2-3.csv( first dataset after cleaning) , then you should run all cells .

Also, you need to download list.txt(text file contains Arabic stop words) for both notebooks.
Then, you can test each model individually with any tweet you want in output_preprocess notebook. You need to to run data preprocessing methods and load tf-idf first. In Each model, you can write whatever arabic tweet you want and you will see it after cleaning and then you will see it’s sentiment.

For sarcasm detection and sentiment analysis, you need to download ArSarcasm_train and Arsarcasm_test. Then, you need to run all cells. There is a part at the ned of the notebook which contains testing each model individually where you can put any arabic tweet you want and each model will classify into neutral, positive and negative and deter whether it’s sarcastic or not. 