# ML Repository
### Fraud Detection System Development using Deep Neural Network for Reported Transactional Data

#### Bangkit Academy Final Capstone Project

* Data Cleaning - Cleaning_coba.ipynb

* Feature Engineering - Feature_coba.ipynb

* Modelling 
	* with Logistic Regression - Modelling_coba.ipynb
	* with K Nearest Neighbor - Modelling_KNN_coba.ipynb
	* with Sequential - Modelling_LogReg_Keras.ipynb
	* with Gradient Boosted Tree - Modelling_GBT.ipynb (run using collab)
	
* Input Normalisation - Input_Normalisation.ipynb

* Testing Model Prediction - Test_Prediction.ipynb

=========================================================

* Saved Models: saved_models
	* log_reg_export - TensorFlow Model of Logistic Regression
	* log_reg_keras.h5 - Keras Model of Logistic Regression
	* log_reg_keras_source_drop.h5 - Keras Model with 1 'source' column dropped, Sequential Model
	
* Deployed Models: deployed_models
	* log_reg w source - Logistic Regression with 'source' column
	* log_reg wo source - Logistic Regression without 'source column
	
=========================================================

* Dependencies: recommended versions
	* Python 3.6.13
	* Anaconda 23.1.0
	* Jupyter Notebook 6.4.10
	* TensorFlow 2.2.0
	* TensorFlowjs 3.18.0
	* Keras 2.6.0
	* TensorFlow Decision Forests 1.3.0
	* Scikit-learn 0.24.2
	* Pandas 1.1.0 
