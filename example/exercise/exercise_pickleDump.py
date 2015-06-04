import pickle

D={1:1,2:2}
with open('exercise_pickle.txt','wb') as file:
    pickle.dump(D,file)
