
## Linear Regression: 
         Is used for finding linear relationship between target  and one or more predictors.

# Simple Linear Regression

          Simple linear regression is useful for finding relationship between two continuous variables.

One is predictor or independent variable(X) and other is response or dependent variable(Y)

         Y' =β0+β1X                          

         y'=predicted label, β1= bias(y intercept) β2= slope

This technique is used for forecasting, time series modelling and finding the causal effect relationship between the variables.

Eg: Relationship between rash driving and number of road accidents by a driver is best studied through regression.

# Multi Linear Regression:
         Multi linear regression is useful for finding relationship amoung many continuous variables.
            
            *Multi Linear Regression = Many Independent Variables with One Dependent Variable
            
          Y' =β0+β1X+β2X+β3X+......+β(n-1)X+βnX

# Multi Linear Regression Data Preparation:

         1. Generate a list of Independent(Features) and Dependent(Lables) Variables
         2. Collect the data on the variables
         3. Check the relationship between the Independent and Dependent Variables using Scatterplot and Correlations
         4. Check the relationship amoung the Independent's  Variables using Scatterplot and Correlations
         5. (Optional) Conduct the simple linear regression for each Independent and Dependent Varibales
         6. Use Non-redundant independent Variables in the analysis to find the best fitting model
         7. Use the best fitting model to make predictions about the dependent variables
         
 # Note: 
 	Adding more independent variables (Features) leads to the overfitting problem.
 
 # Relationship between the Independent and Dependent Variables:
 
 
                                             x1-------------------------------->
 
   Independent Varibales                                 x2  ------------ >                              Y  Dependent Varibales
                                    
                                             x3-------------------------------- >     
                                             
                                             3 Relationships to analyze
                                             
 # Images/Figure 1
   
 # Note:
 	Independent Variables which does not has any correlation with the dependent variable,should not consider to the fitting     model.
 
 # Relationship amoung the Independent's  Variables:
  
                                             x1----------> x2
 
   Independent Varibales:                                 x2  --------> x3
                                    
                                             x3----------> x1
                                             
                                             3 Relationships to analyze
                                             
# Images/Figure 2                                    
         
 # Note: 
 	Any Independent variable with high corellation with other variable is a  Multicolinearity 
	Multicolinearity variables should not used in the model, only one variable should be used.


                  
         
         

