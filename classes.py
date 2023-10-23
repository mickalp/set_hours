#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 23:04:52 2023

@author: michal
"""
# =============================================================================
# Wpisz sciezke do pliku ze swoimi roboczo godzianmi
# =============================================================================
file_n = '/Users/michal/Library/CloudStorage/OneDrive-UniversityofGdansk/OneDrive - University of Gdansk (for Students)/agnieszka_gajewicz/split_hours_for_company/set_hours/2023_06_Roboczogodziny_Rozliczenie_czerwiec_2023_AG_MK.xlsx'

# =============================================================================
# Sciezka do pliku z nazwa pliku /path_to_script/work_time_v1.x.py
# =============================================================================
script_path = "/Users/michal/Library/CloudStorage/OneDrive-UniversityofGdansk/OneDrive - University of Gdansk (for Students)/agnieszka_gajewicz/split_hours_for_company/set_hours/work_time_v1.2.py"  # Replace with the path to your script

# =============================================================================
# Sciezka do folderu roboczego
# =============================================================================
pt = "/Users/michal/Library/CloudStorage/OneDrive-UniversityofGdansk/OneDrive - University of Gdansk (for Students)/agnieszka_gajewicz/"

# =============================================================================
# Sciezka w której mają byc zapisywane Twoje pliki
# =============================================================================
pt_to_save = '/Users/michal/Desktop'

# =============================================================================
# Tutaj zamien jeden na zero jesli chcesz wybrac inny miesiac i rok wykonywania skryptu
# niz ten poprzedzjący miesiąc, dla którego godziny zostały uzupełnione
# jezeli godziny są dla miesiąca wrzesien, a skrypt jest uruchamiany w pazdierniku
# nic nie musisz zmieniac
# =============================================================================
def_mnth = 0




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
        parts = time_str
        print(time_str)

        if parts:
            start_parts = time_str.split('.')
            # print(start_parts)
        

            if len(start_parts) == 2 and start_parts[0].isdigit() and \
                start_parts[1].isdigit() and start_parts[1]=='5':
                # print(start_parts[1])
                hour, minute = start_parts
                modified_start_time = f'{hour}:30'

            
            elif len(start_parts) == 2 and start_parts[0].isdigit() and \
                start_parts[1].isdigit() and start_parts[1]=='0':
                hour, minute = start_parts
                modified_start_time = f'{hour}:00'
                
            elif time_str == 0:
                hour = str(start_parts[0])
                modified_start_time = 'Weekend'
            
            # else:
            #     hour = start_parts
            #     # hour = int(start_parts[0])
            #     modified_start_time = f'{hour}:00'
            
            else:
                time_str = str(time_str)
                modified_start_time = f'{time_str}:00'
            

            



        
            # if len(end_parts) == 2 and end_parts[1] == '5' :

            #     hour = end_parts[0]
            #     modifide_end_time = f'{hour}:30'
                
            # else:
            #     hour = end_parts[0]
            #     modifide_end_time = f'{hour}'
                
            final_time = f'{modified_start_time}'
            return final_time
        
                
                
        return time_str

    def modify_column(self, df):
        df[self.column_name] = df[self.column_name].apply(self.modify_time_format)
        
