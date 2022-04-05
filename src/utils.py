def add_rul(df):
    max_cycles = df.groupby('unit_nr',as_index=False).time_cycles.max().rename(columns = {'time_cycles':'max_cycles'})
    df = (df.merge(max_cycles, on = 'unit_nr', how = 'left')
                        .assign(rul = lambda x: x.max_cycles - x.time_cycles)
                        .drop(columns = 'max_cycles'))
    return df

