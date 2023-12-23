#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 1 23:04:52 2023

@author: michal
"""

import os

# Configuration Parameters
file_n = 'path/to/your/file.xlsx'
script_path = os.path.join(os.path.dirname(__file__), 'work_time_v1.2.py')
working_folder = 'path/to/working/folder'
save_folder = 'path/to/save/folder'
def_mnth = 0

# ...

class CuttingDataFrame:
    def __init__(self, start_columns, end_columns, last_col, df_name):
        self.start_columns = start_columns
        self.end_columns = end_columns
        self.last_col = last_col
        self.df_name = df_name

    def drop_columns(self):
        self.df_name.drop(
            self.df_name.columns[self.start_columns:self.end_columns],
            inplace=True,
            axis=1
        )

        self.df_name.drop(
            self.df_name.columns[self.last_col:],
            inplace=True,
            axis=1
        )
        return self.df_name

# ...

class TimeFormatModifier:
    def __init__(self, column_name):
        self.column_name = column_name

    @staticmethod
    def modify_time_format(time_str):
        # Implementation remains the same

    def modify_column(self, df):
        df[self.column_name] = df[self.column_name].apply(self.modify_time_format)

if __name__ == "__main__":
    # Your main code here
