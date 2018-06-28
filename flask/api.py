#app.py passes feature values from user input in index.html to 
#the random forest model loaded into this file. Prediction for 
#animal adoption probability is then made and returned to app.py

import pickle
   
#load random forest model and a template for assembling feature values for prediction
#template has default values for feature values not included in prediction function
#argument list.
rf = pickle.load(open('/home/jieliang/proj3/submission/flask/data/best_rf.pkl', 'rb'))
temp = pickle.load(open('/home/jieliang/proj3/submission/flask/data/flask_X_temp.pkl', 'rb'))



#populate template then make a prediction
def make_soft_prediction(animalType,intake_reproductive,outcome_reproductive,intake_health,outcome_health):
   
        print("This is the soft prediction function")
        X = temp.copy(deep=True)
        
        if animalType == 'cat':
            X['animaltype_CAT'] = 1
        if animalType == 'dog':
            X['animaltype_DOG'] = 1  
        if animalType == 'other':
            X['animaltype_OTHER'] = 1 
            
        if intake_reproductive == "fertile":
            X['reproductivestatusatintake_FERTILE']=1
        else:
            X['reproductivestatusatintake_ALTERED']=1
            
        if outcome_reproductive== "fertile":
            X['reproductivestatusatoutcome_FERTILE']=1
        else:
            X['reproductivestatusatoutcome_ALTERED']=1
            
            
        if intake_health == "healthy":
            X['intakeasilomarstatus_HEALTHY']=1
        else:
            X['intakeasilomarstatus_UNHEALTHY/UNTREATABLE']=1
            
        if outcome_health == "healthy":
            X['outcomeasilomarstatus_HEALTHY']=1
        else:
            X['outcomeasilomarstatus_UNHEALTHY/UNTREATABLE']=1
            
        return rf.predict_proba(X)[0][0]
          
 
