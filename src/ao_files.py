# -*- coding: utf-8 -*-
# @author: hgy
# @created: 2024/10/10
import os
import sys

def load_files():
    '''
    加载受试文件
    files: 文件路径
    caps: 受试脑电帽子 # EEG caps, old:ANT, new:Greentak
    info: 受试信息 # name of sub
    file_version_info: 文件版本 # 0: old version, 1: new version
    '''
    # file info for first time of subjects
    file_1 = r'D:\work_space\data\raw\ANT_S1_test'
    file_2 = r'D:\work_space\data\raw\ANT_S2_test'
    file_3 = r'D:\work_space\data\raw\ANT_S3_test'
    file_4 = r'D:\work_space\data\raw\ANT_S4_test'
    file_5 = r'D:\work_space\data\raw\ANT_S5_test'
    file_6 = r'D:\work_space\data\raw\ANT_S6_test'
    file_7 = r'D:\work_space\data\raw\ANT_S7_test'
    file_8 = r'D:\work_space\data\raw\ANT_S8_test'
    file_9 = r'D:\work_space\data\raw\ANT_S9_test'
    file_10 = r'D:\work_space\data\raw\ANT_S10_test'
    file_11 = r'D:\work_space\data\raw\ANT_S11_test'
    file_12 = r'D:\work_space\data\raw\ANT_S12_test'
    file_13 = r'D:\work_space\data\raw\ANT_S13_test'
    file_14 = r'D:\work_space\data\raw\ANT_S14_test'
    file_15 = r'D:\work_space\data\raw\ANT_S15_test'
    file_16 = r'D:\work_space\data\raw\ANT_S16_test'
    file_17 = r'D:\work_space\data\raw\ANT_S17_test'
    file_18 = r'D:\work_space\data\raw\ANT_S18_test'
    file_19 = r'D:\work_space\data\raw\ANT_S19_test'
    file_20 = r'D:\work_space\data\raw\ANT_S20_test'

    files_first = [file_1, file_2, file_3, file_4, file_5, file_6, file_7,
                    file_8, file_9, file_10, file_11, file_12, file_13, file_14,
                          file_15, file_16, file_17, file_18, file_19, file_20]
    caps_first = ['old', 'old', 'old', 'old', 'old', 'old', 'new',
                   'new', 'new', 'old', 'old', 'old', 'new', 'old',
                     'old', 'old', 'old', 'old', 'old', 'old']
    subs_first = ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 
                  'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'S14',
                    'S15', 'S16', 'S17', 'S18', 'S19', 'S20']
    versions_first = [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1]
    # file info for second time of subjects

    file_day1_s10 = r'D:\work_space\data\cross\ANT_S10_day1_test'
    file_day1_s11 = r'D:\work_space\data\cross\ANT_S11_day1_test'
    file_day1_s12 = r'D:\work_space\data\cross\ANT_S12_day1_test'
    file_day1_s13 = r'D:\work_space\data\cross\ANT_S13_day1_test'
    file_day1_s14 = r'D:\work_space\data\cross\ANT_S14_day1_test'
    file_day1_s15 = r'D:\work_space\data\cross\ANT_S15_day1_test'
    file_day1_s16 = r'D:\work_space\data\cross\ANT_S16_day1_test'
    file_day1_s17 = r'D:\work_space\data\cross\ANT_S17_day1_test'
    file_day1_s18 = r'D:\work_space\data\cross\ANT_S18_day1_test'
    file_day1_s19 = r'D:\work_space\data\cross\ANT_S19_day1_test'
    file_day1_s20 = r'D:\work_space\data\cross\ANT_S20_day1_test'
    file_day1_s21 = r'D:\work_space\data\cross\ANT_S21_day1_test'
    file_day1_s22 = r'D:\work_space\data\cross\ANT_S22_day1_test'
    
    files_second = [file_day1_s10, file_day1_s11,file_day1_s12, file_day1_s14, 
                    file_day1_s15, file_day1_s16, file_day1_s17, file_day1_s18, 
                    file_day1_s19, file_day1_s20, file_day1_s21, file_day1_s22]
    caps_second = ['old', 'old', 'old', 'old', 
                   'old', 'old', 'old', 'old', 
                   'old', 'old', 'old', 'old']
    subs_second = ['S10', 'S11', 'S12', 'S14', 
                   'S15', 'S16', 'S17', 'S18', 
                   'S19', 'S20', 'S21', 'S22']
    versions_second = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    # file info for third time of subjects

    file_day2_s10 = r'D:\work_space\data\cross\ANT_S10_day2_test'
    file_day2_s11 = r'D:\work_space\data\cross\ANT_S11_day2_test'
    file_day2_s12 = r'D:\work_space\data\cross\ANT_S12_day2_test'
    file_day2_s13 = r'D:\work_space\data\cross\ANT_S13_day2_test'
    file_day2_s14 = r'D:\work_space\data\cross\ANT_S14_day2_test'
    file_day2_s15 = r'D:\work_space\data\cross\ANT_S15_day2_test'
    file_day2_s16 = r'D:\work_space\data\cross\ANT_S16_day2_test'
    file_day2_s17 = r'D:\work_space\data\cross\ANT_S17_day2_test'
    file_day2_s18 = r'D:\work_space\data\cross\ANT_S18_day2_test'
    file_day2_s19 = r'D:\work_space\data\cross\ANT_S19_day2_test'
    file_day2_s20 = r'D:\work_space\data\cross\ANT_S20_day2_test'
    file_day2_s21 = r'D:\work_space\data\cross\ANT_S21_day2_test'
    file_day2_s22 = r'D:\work_space\data\cross\ANT_S22_day2_test'
    
    files_third = [file_day2_s10, file_day2_s11, file_day2_s12, file_day2_s14, 
                   file_day2_s15, file_day2_s16, file_day2_s17, file_day2_s18, 
                   file_day2_s19, file_day2_s20, file_day2_s21, file_day2_s22]
    caps_third = ['old', 'old', 'old', 'old', 
                  'old', 'old', 'old', 'old', 
                  'old', 'old', 'old', 'old']
    subs_third = ['S10', 'S11', 'S12', 'S14', 
                  'S15', 'S16', 'S17', 'S18', 
                  'S19', 'S20', 'S21', 'S22']
    versions_third = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    # create a list of files and their corresponding caps
    infos = {
        'days': ['raw', 'day1', 'day2'],
        'files': [files_first, files_second, files_third],
        'caps': [caps_first, caps_second, caps_third],
        'subs': [subs_first, subs_second, subs_third],
        'versions': [versions_first, versions_second, versions_third]
    }

    return infos

