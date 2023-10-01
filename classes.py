#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 23:04:52 2023

@author: michal
"""

# Class to cutting orginal data into smaller portions
# Start columns and end columns is range from the left side of dataframe
# For example if start_columns =0, end_columns=5, 
# five columns from left side will be droped
# Last col should be add from the right side with -
# i.e -5 ; five columns droped from right side


class cutting_df:
    def __init__(self, start_columns, end_columns, last_col, df_name):
        self.start_columns = start_columns
        self.end_columns = end_columns
        self.last_col = last_col
        self.df_name = df_name
        
        
    def dropin(self, start_columns, end_columns, last_col, df_name):
        self.df_name.drop(
        self.df_name.columns[self.start_columns:self.end_columns], inplace = True,
        axis=1
        )
        
        self.df_name.drop(
        self.df_name.columns[self.last_col:], inplace = True,
        axis=1
        )
        return self.df_name


class TimeFormatModifier:
    def __init__(self, column_name):
        self.column_name = column_name

    @staticmethod
    def modify_time_format(time_str):
        week = time_str
        print(week)
        parts = time_str.split('-')
        print(parts)
        if len(parts) == 2:
            start_time, end_time = parts
            start_parts = start_time.split('.')
            end_parts = end_time.split('.')
            
        

            if len(start_parts) == 2 and start_parts[0].isdigit() and \
                start_parts[1].isdigit() and start_parts[1]=='5':
                # print(start_parts[1])
                hour, minute = start_parts
                modified_start_time = f'{hour}:30'

            
            # elif len(start_parts) == 2 and start_parts[0].isdigit() and \
            #     start_parts[1].isdigit() and start_parts[1]=='0':
            #     hour, minute = start_parts
            #     modified_start_time = f'{hour}:00'

            
            else:
                hour = start_parts[0]
                modified_start_time = f'{hour}'

        
            if len(end_parts) == 2 and end_parts[1] == '5' :

                hour = end_parts[0]
                modifide_end_time = f'{hour}:30'
                
            else:
                hour = end_parts[0]
                modifide_end_time = f'{hour}'
                
            final_time = f'{modified_start_time}-{modifide_end_time}'
            return final_time
        
                
                
        return time_str

    def modify_column(self, df):
        df[self.column_name] = df[self.column_name].apply(self.modify_time_format)
        
