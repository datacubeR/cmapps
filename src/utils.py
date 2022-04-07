import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
sns.set()

def add_rul(df):
    max_cycles = df.groupby('unit_nr',as_index=False).time_cycles.max().rename(columns = {'time_cycles':'max_cycles'})
    df = (df.merge(max_cycles, on = 'unit_nr', how = 'left')
                        .assign(rul = lambda x: x.max_cycles - x.time_cycles)
                        .drop(columns = 'max_cycles'))
    return df

def plot_oof(y, y_pred, figsize = (5,5), s = 2, path = None):
    plt.figure(figsize=figsize)
    plt.scatter(y, y_pred, s=s, color='r')
    plt.plot([plt.xlim()[0], plt.xlim()[1]], [plt.xlim()[0], plt.xlim()[1]], '--', color='k')
    plt.gca().set_aspect('equal')
    plt.xlabel('Ground Truth')
    plt.ylabel('Prediction')
    plt.title('True vs Fitted Curve')
    if path is None:
        plt.show()
    else:
        plt.savefig(path, bbox_inches='tight')
        plt.close()
        
        
def plot_importance(model, variable_names, path = None):
    ax =(pd.Series(model.coef_.ravel(), 
                index = variable_names)
        .sort_values(ascending=False)
        .plot(kind = 'bar', title = 'Variable Importance'))
    
    if path is None:
        plt.show()
    else:
        plt.savefig(path, bbox_inches='tight')
        plt.close()
    
