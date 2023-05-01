class FilterData:
    def __init__(self,df) -> None:
        self.df=df
        self.filter_f=None

    def custom_filter(self,row):
        op={
            '>':lambda x,y:x>y,
            '<':lambda x,y:x<y,
            '=':lambda x,y:x==y,
            '>=':lambda x,y:x>=y,
            '<=':lambda x,y:x<=y
        }    
        temp_f=self.filter_f.loc[self.filter_f['filterName'].str.lower()==row[4].lower()]
        f_param=temp_f.values.tolist()
        if f_param:
            if f_param[0][6]:
                if f_param[0][3]=='float':
                    try:
                        if op[f_param[0][6](float(row[6]),float(f_param[0][5]))]:
                            row['flag']
                            row['thresholdvalue']
            else:
                row['flag']='NA'
                row['thresholdvalue']=f_param[0][5] if f_param[0][5] else 0
        else:
            row['Flag']='NA'
            row['thresholdvalue']=0
        return row            
