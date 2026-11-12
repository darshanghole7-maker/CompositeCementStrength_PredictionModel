# Data preprocessing and cleaning

def data_preprocessing(df):

  '''
  step 1 :feature enginerring selection

  step 2 : split the dataset into independence and dependent columns i.e x and y

  step 3 : use train and test split i.e split the dataset into seen and unseen
  (seen data: train data and unseen data a;test data)

  step 4 : use scaling technique/normalization technique
  (standardscaler/minmaxscaler/robustscaler)

  step 5 : return seen and unseen data
  '''
  # feature engineering : which creating the new features from existing feature

  df['Water_Binder_Ratio'] = df['Water  (component 4)(kg in a m^3 mixture)'] / (df['Cement (component 1)(kg in a m^3 mixture)']
                                                                                + df['Blast Furnace Slag (component 2)(kg in a m^3 mixture)']
                                                                                + df['Fly Ash (component 3)(kg in a m^3 mixture)'])

  target_col = "Concrete compressive strength(MPa, megapascals) "
  X = df.drop(columns = [target_col]) # independent columns
  y = df[target_col]                  # dependent column

  # step 3 : split the dataset into seen and unseen (train and test data)
  from sklearn.preprocessing import  MinMaxScaler,RobustScaler,StandardScaler
  from sklearn.model_selection import train_test_split
  X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.3,random_state = 1)


  X_train.shape,X_test.shape,y_train.shape,y_test.shape

  # step 4: Use scaling/normalization technique
  '''
  * scaling for the training data : fit_transform()
  * scaling for the testing data : transform()

  '''
  sc = MinMaxScaler()
  X_train_scaled = sc.fit_transform(X_train) #seen data
  X_test_scaled = sc.transform(X_test) # unseen data

  return X_train_scaled,X_test_scaled,y_train,y_test
