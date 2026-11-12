#orchestrator layer :Entry points
from src.data_ingestion import data_ingestion
from src.data_preprocessing import data_preprocessing
from src.model_build import model_build

def main(): #function definition 
# step 1 Data ingestion 
  df = data_ingestion()
  #step 2 Data preprocessing and cleaning 
  X_train_scaled,X_test_scaled,y_train,y_test = data_preprocessing(df)
  #step 3 model building 
  score = model_build(X_train_scaled,X_test_scaled,y_train,y_test)
  print(f'R2 Score:{score}')

main() # function calling 