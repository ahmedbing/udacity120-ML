
from sklearn import linear_model
from sklearn import metrics
import numpy as np

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth,error).
    """

    for x in range(10):
        max =0
        ind_del=0
        for idx , num in enumerate(net_worths):
            dif=num-predictions[idx]
            dif=np.abs(dif)
            if (dif>max):
                max = dif
                ind_del= idx
        ages = np.delete(ages,ind_del)
        net_worths = np.delete(net_worths, ind_del )
        print("Index deleted ", ind_del,"  At iteration = " ,x)
        predictions = np.delete(predictions,ind_del)

    error = np.zeros(90)
    cleaned_data = ages, net_worths, error

    return cleaned_data

