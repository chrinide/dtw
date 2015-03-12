from pandas.io.data import DataReader
from datetime import datetime
import numpy as np
import dtw
import util

f = DataReader("F",  "yahoo", datetime(2000,1,1), datetime(2012,1,1))

f_2008=f[f.index.year==2008]
f_2009=f[f.index.year==2009]

#X = np.array(f_2009.Volume.values)
#Y = np.array(f_2008.Volume.values)
#print(X.size,Y.size)

ts1 = np.array([0.57311057,0.66785286,0.6204376,0.64280256,0.69667441,0.60423623,0.64343652,0.61178161])
ts2 = np.array([0.61543759,0.58163419,0.62914481,0.62535561,0.62036891,0.61944155,0.63006706,0.58448635])
#ts1 = shrunk_short(ts1)
#print(ts1)
#print(ts1.size)
#print(ts.size)

def fast_dtw(ts1,ts2,radius,distance="ecludian"):
    radius if radius > 0 else 0
    
    min_t_size = radius +2
    # set resolution factor
    resolation_factor = 2
    #base case for recursive call
    if ts1.size <= min_t_size or ts2.size <= min_t_size:
        return dtw.dtw(ts1,ts2)
    
    # shrunk time series
    shrunk_x,agg_point_size_x = util.shrunk_timeseries(ts1,round(ts1.size/resolation_factor)) 
    shrunk_y,agg_point_size_y = util.shrunk_timeseries(ts2,round(ts2.size/resolation_factor))
    
    min_cost,min_cost_path = dtw.dtw(shrunk_x,shrunk_y)
    result_window = dtw.search_window(ts1,ts2,shrunk_x,shrunk_y,min_cost_path,radius,agg_point_size_x,agg_point_size_y)
    
    print("minimum cost: ",min_cost)
    print("minimum cost path: ",min_cost_path)
    print(result_window)
    '''
    shrunk_x = util.shrunk_short(X) 
    shrunk_y = util.shrunk_short(Y)
    '''
    #print(shrunk_x)
    
    
    
    # call recursively on every shrunked time series
    # return dtw calculations


fast_dtw(ts1, ts2, 2)