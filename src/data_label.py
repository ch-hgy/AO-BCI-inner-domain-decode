# -*- coding: utf-8 -*-
# @author: hgy
# @created: 2024/10/10
import os
import numpy as np
import scipy.io as scio
from scipy.signal import butter, filtfilt

# -----------------------------------load files-----------------------------------

def charge_data_event(file_data, file_event):
    '''
    检查数据文件和事件文件是否匹配
    '''
    file_light = 0
    for data_pth, event_pth in zip(file_data, file_event):
        if data_pth[:-14] != event_pth[:-14]:
            file_light = 1
            break

    if file_light == 0:
        return True
    else:
        return False

def fileload(pth_subject):
    '''
    加载最初版本的文件 按照实验流程过滤文件
    '''
    list_pth = os.listdir(pth_subject)
    list_pth.sort(key=lambda x: int(x[-18:-14]))  # sort by number
    # print(f'list_pth: {list_pth}')

    # create container
    event_s = 'stimevent'
    event_para1, data_para1 = [], []
    event_para2, data_para2 = [], []
    event_para3, data_para3 = [], []

    for i, index in enumerate(list_pth):
        index = os.path.join(pth_subject, index)
        if i < 8:
            if event_s in index:
                event_para1.append(index)
            else:
                data_para1.append(index)
        elif i < 16:
            if event_s in index:
                event_para2.append(index)
            else:
                data_para2.append(index)
        elif i < 24:
            if event_s in index:
                event_para3.append(index)
            else:
                data_para3.append(index)

    # files inspection between data and event
    result = []
    result.append(charge_data_event(data_para1, event_para1))
    result.append(charge_data_event(data_para2, event_para2))
    result.append(charge_data_event(data_para3, event_para3))
    if False in result:
        print("data and event file not match, file load error!")
        quit()
    # else:
    #     print("file load success!")

    return event_para1, data_para1, event_para2, data_para2, event_para3, data_para3

def fileload_ant(pth_subject):
    '''
    加载新版本的文件 按照文件变量过滤文件
    '''
    list_pth = os.listdir(pth_subject)
    list_pth.sort(key=lambda x: int(x[-18:-14]))  # sort by number
    # load total MAT data
    event_s = 'stimevent'
    event, data = [], []
    for pth in list_pth:
        if event_s in pth:
            event.append(pth)
        else:
            data.append(pth)
    event_para1, data_para1 = [], []
    event_para2, data_para2 = [], []
    event_para3, data_para3 = [], []
    for event_i, data_i in zip(event, data):
        event_i, data_i = os.path.join(pth_subject, event_i), os.path.join(pth_subject, data_i)  # add path
        event_info = scio.loadmat(event_i)['stimevent'][0][0]

        L_R = event_info['L_or_R']
        stim = event_info['stimMode']
        feedback = event_info['IsFeedback']
        if feedback == 0:
            if stim == 7:
                event_para2.append(event_i)
                data_para2.append(data_i)
            elif stim == 6:
                if L_R == 2:
                    event_para1.append(event_i)
                    data_para1.append(data_i)
                elif L_R == 1:
                    event_para3.append(event_i)
                    data_para3.append(data_i)
    # files inspection between data and event
    result = []
    result.append(charge_data_event(data_para1, event_para1))
    result.append(charge_data_event(data_para2, event_para2))
    result.append(charge_data_event(data_para3, event_para3))
    if False in result:
        print("data and event file not match, file load error!")
        quit()
    # else:
    #     print("file load success!")
    return event_para1, data_para1, event_para2, data_para2, event_para3, data_para3


# read files with feedback
def fileload_feedback(filename):
    '''
    老版本文件加载方式
    基于实验流程进行加载
    '''
    list_pth = os.listdir(filename)
    list_pth.sort(key=lambda x: int(x[-18:-14]))
    fb_list_pth = list_pth[24:]
    len_file = len(fb_list_pth)/2
    mark_len = len_file if len_file % 2 == 0 else len_file + 1
    # create container
    event_s = 'stimevent'
    event_fb_para1 = []
    data_fb_para1 = []
    event_fb_para3 = []
    data_fb_para3 = []
    
    for i, index in enumerate(fb_list_pth):
        index = os.path.join(filename, index)
        if i < mark_len:
            if event_s in index:
                event_fb_para1.append(index)
            else:
                data_fb_para1.append(index)
        else:
            if event_s in index:
                event_fb_para3.append(index)
            else:
                data_fb_para3.append(index)
    print(f'event_fb_para1: {event_fb_para1}')
    print(f'data_fb_para1: {data_fb_para1}')
    print(f'event_fb_para3: {event_fb_para3}')
    print(f'data_fb_para3: {data_fb_para3}')
    # files inspection between data and event
    result = []
    result.append(charge_data_event(data_fb_para1, event_fb_para1))
    result.append(charge_data_event(data_fb_para3, event_fb_para3))
    if False in result:
        print("data and event file not match, file load error!")
        quit()
    # else:
    #     print("file load success!")

    return event_fb_para1, data_fb_para1, event_fb_para3, data_fb_para3

def fileload_feedback_ant(filename):
    '''
    新版本文件加载方式
    基于stimevent记录信息进行加载
    '''
    list_pth = os.listdir(filename)
    list_pth.sort(key=lambda x: int(x[-18:-14]))

    # load total mat
    event_s = 'stimevent'
    event, data = [], []
    for pth in list_pth:
        if event_s in pth:
            event.append(pth)
        else:
            data.append(pth)
    feedback_event_para1, feedback_data_para1 = [], []
    feedback_event_para3, feedback_data_para3 = [], []

    for event_i, data_i in zip(event, data):
        event_i, data_i = os.path.join(filename, event_i), os.path.join(filename, data_i)  # add path
        event_info = scio.loadmat(event_i)['stimevent'][0][0]
        L_R = event_info['L_or_R']
        stim = event_info['stimMode']
        feedback = event_info['IsFeedback']
        if feedback == 1:
            if stim == 6 and L_R == 2:
                feedback_event_para1.append(event_i)
                feedback_data_para1.append(data_i)
            elif stim == 6 and L_R == 1:
                feedback_event_para3.append(event_i)
                feedback_data_para3.append(data_i)
    print(f'feedback_data_para1: {feedback_data_para1}')
    print(f'feedback_data_para3: {feedback_data_para3}')
    print(f'feedback_event_para1: {feedback_event_para1}')
    print(f'feedback_event_para3: {feedback_event_para3}')
    # files inspection between data and event
    result = []
    result.append(charge_data_event(feedback_data_para1, feedback_event_para1))
    result.append(charge_data_event(feedback_data_para3, feedback_event_para3))
    if False in result:
        print("data and event file not match, file load error!")
        quit()
    # else:
    #     print("file load success!")

    return feedback_event_para1, feedback_data_para1, feedback_event_para3, feedback_data_para3

# -----------------------------------basic functions-----------------------------------

# get electrodes index of EEG channels
def electrode_index(electrodes):
    '''
    get electrode index from electrodes list
    '''
    all_electrodes = ['Fp1', 'Fpz', 'Fp2', 
    'F7', 'F3', 'Fz', 'F4', 'F8', 
    'FC5', 'FC1', 'FC2', 'FC6', 
    'PO3', 'T7', 'C3', 'Cz', 'C4', 'T8', 'PO4', 
    'CP5', 'CP1', 'CP2', 'CP6', 
    'PO7', 'P3', 'Pz', 'P4', 'PO8', 
    'POz', 
    'O1', 'Oz', 'O2']
    index = [i for i in range(len(all_electrodes)) if all_electrodes[i] in electrodes]
    
    return index

# loss function
def loss(y_label, p_label):
    flag = 0
    if len(y_label) != len(p_label):
        print("y_label and p_label must have the same length")
        quit()
    for i in range(len(y_label)):
        if y_label[i] == p_label[i]:
            flag += 1

    return flag / len(y_label)

def get_online_acc(event_files):
    '''
    获取在线准确率
    '''
    acc = []
    for event in (event_files):
        # load total MAT data
        event_iter = scio.loadmat(event)['stimevent'][0][0]

        # get data we need
        right_label = [i.item() for i in event_iter['stimnum'][:, 0] if i != 0]  # delete zero item
        online_label = [i.item() for i in event_iter['stimnum'][:, 1] if i != 0]
        acc.append(np.round(100*loss(right_label, online_label), 2))

    return acc

# data mean and keep its shape
def data_mean(data1, data2):
    data = data1 + data2
    return np.array([i / 2 for i in data])


# data concatenate
def data_concatenate(data1, data2, keep_axis=0):
    return np.concatenate((data1, data2), axis=keep_axis)

def EventData(pth_event):
    '''
    获取采样时间点/采样数据点
    '''
    # load total MAT data
    event = scio.loadmat(pth_event)['stimevent'][0][0]

    # get data we need
    toc = [i.item() for i in event['toc'][..., 0] if i != 0]  # delete zero item
    stimnum = [i.item() for i in event['stimnum'][:, 0] if i != 0]  # delete zero item
    return toc, stimnum

def get_freq(event):
    '''
    获取刺激频率
    '''
    return scio.loadmat(event)['stimevent'][0][0]['fps']

# load data matrix
def EEGData(pth_data):
    data_comp = scio.loadmat(pth_data)['data_comp2']
    return data_comp

def DataDeal(col_index, toc, data_comp, dots, fs):
    data_use = []
    # column slice
    data_comp = np.array(data_comp[..., col_index])  # extract column

    for time_iter in toc:
        value = int(time_iter * fs)
        data = data_comp[int(value):int(value + dots), ...].T
        data_use.append(data)
    # print(f'shape of data_use: {np.shape(data_use)}')

    return data_use

# prepare butetr bandpass filter
def butter_bandpass_filter(data, lowcut, highcut, fs, order=6):
    '''
    巴特沃斯带通滤波器
    lowcut: 低通滤波器截止频率
    highcut: 高通滤波器截止频率
    fs: 采样率
    '''
    if lowcut <= 0 or highcut <= 0:
        raise ValueError("lowcut and highcut must be positive")
    if lowcut >= highcut:
        raise ValueError("lowcut must be less than highcut")
    if fs <= 0:
        raise ValueError("Sampling frequency fs must be positive")
    if not isinstance(data, (list, np.ndarray)):
        raise ValueError("data must be a list or numpy array")
    if np.array(data).size == 0:
        raise ValueError("data must not be empty")

    fa = 0.5 * fs
    low = lowcut / fa
    high = highcut / fa
    b, a = butter(order, [low, high], btype='band') # type: ignore
    y = filtfilt(b, a, data)
    return y

# function of generate reference sin signal
def generate_mscca_references(freqs, srate, T, phases, n_harmonics: int = 1):
    '''
    生成参考正余弦信号
    freqs: 频率
    srate: 采样率
    T: 信号长度
    phases: 相位
    n_harmonics: 正弦波的数量
    '''
    freqs = freqs.flatten()
    if isinstance(freqs, int) or isinstance(freqs, float):
        freqs = [freqs]
    freqs = np.array(freqs)[:, np.newaxis]
    if phases is None:
        phases = 0
    if isinstance(phases, int) or isinstance(phases, float):
        phases = [phases]
    phases = np.array(phases)[:, np.newaxis]
    t = np.linspace(0, T, int(T * srate))

    Yf = []
    for i in range(n_harmonics):
        if i % 2 == 0:
            Yf.append(np.stack([
                np.sin(2 * np.pi * freqs * t + np.pi * phases),  # different phases pre-defined
                np.cos(2 * np.pi * freqs * t + np.pi * phases),
            ], axis=1))
        else:
            Yf.append(np.stack([
                np.sin(4 * np.pi * freqs * t + np.pi * phases),  # different phases pre-defined
                np.cos(4 * np.pi * freqs * t + np.pi * phases),
            ], axis=1))

    Yf = np.concatenate(Yf, axis=1)
    return Yf

def reference_s(freq, fs, time):
    '''
    创建参考正余弦信号
    '''
    return generate_mscca_references(freq, srate=fs, T=time, phases=None, n_harmonics=2)
# -----------------------------------load datas and labels-----------------------------------

# data concatenate for raw data
def raw_data(event, data, fs, time, cap):
    '''
    raw data without filter and any other process
    '''
    dot = time * fs
    raw_temp = []
    label_temp = []
    # choose channels
    # ANT
    if cap == 'old':
        electrodes = ['PO7', 'P3', 'Pz', 'P4', 'POz', 'O1', 'Oz', 'O2']
        cols = electrode_index(electrodes)
    # GREENTEK
    elif cap == 'new':
        electrodes = ['PO3', 'PO4', 'PO7', 'Pz', 'P4', 'POz', 'O1', 'Oz', 'O2']
        # electrodes = ['PO3', 'PO4', 'PO7', 'Pz', 'P4', 'POz', 'O1', 'Oz'] # cross equipments
        cols = electrode_index(electrodes)
    # all electrodes
    else:
        cols = [i for i in range(32)]

    for i in range((len(event))):
        toc, stimnum = EventData(event[i])
        data_tmp = EEGData(data[i])
        data_deal = DataDeal(cols, toc, data_tmp, dot, fs)
        if i == 0:
            raw_temp = data_deal
            label_temp = stimnum
        else:
            raw_temp = data_concatenate(data_deal, raw_temp, keep_axis=0)
            label_temp = data_concatenate(stimnum, label_temp, keep_axis=0)

    raw_data = np.array(raw_temp)
    label = np.array(label_temp)

    return raw_data, label

def mean_action_data(data, label):
    '''
    获取每个动作的平均数据
    data: shape(n_trials, 1500, 8)
    label: shape(8, )
    return: shape(8, 1500)
    '''
    # get unique label
    y_label = np.unique(label)
    data_1, data_2, data_3, data_4 = [], [], [], []

    # get data for each label
    for i in range(len(label)):
        if label[i] == y_label[0]:
            data_1.append(data[i])
        elif label[i] == y_label[1]:
            data_2.append(data[i])
        elif label[i] == y_label[2]:
            data_3.append(data[i])
        elif label[i] == y_label[3]:
            data_4.append(data[i])
    data_1 = np.stack([data[i] for i in range(len(label)) if label[i] == y_label[0]], axis=0)
    data_2 = np.stack([data[i] for i in range(len(label)) if label[i] == y_label[1]], axis=0)
    data_3 = np.stack([data[i] for i in range(len(label)) if label[i] == y_label[2]], axis=0)
    data_4 = np.stack([data[i] for i in range(len(label)) if label[i] == y_label[3]], axis=0)
    
    # shape(8,1500)
    data_1, data_2, data_3, data_4 = np.array(data_1.mean(axis=0)), \
        np.array(data_2.mean(axis=0)), np.array(data_3.mean(axis=0)), np.array(data_4.mean(axis=0))

    return data_1, data_2, data_3, data_4

# data concatenate
def filter_data(event, data, fs, time, cap):
    dot = time * fs
    low_pass = 3
    high_pass = 30

    filtered_temp = []
    label_temp = []
    # choose channels
    # ANT
    if cap == 'old':
        electrodes = ['PO7', 'P3', 'Pz', 'P4', 'POz', 'O1', 'Oz', 'O2'] # visual area electrodes
        # electrodes = ['FC5', 'FC1', 'FC2', 'FC6', 'C3', 'C4', 'Cz', 'CP5', 'CP6', 'CP1', 'CP2', 'CPz'] # motor area electrodes
        # electrodes = ['FC1', 'FC2', 'C3', 'C4', 'Cz', 'CP1', 'CP2', 'CPz'] # motor area electrodes
        cols = electrode_index(electrodes)
    # GREENTEK
    elif cap == 'new':
        # electrodes = ['PO3', 'PO4', 'PO7', 'Pz', 'PO8', 'POz', 'O1', 'Oz', 'O2'] # visual area electrodes
        electrodes = ['PO3', 'PO4', 'PO7', 'Pz', 'POz', 'O1', 'Oz', 'O2'] # cross subjects
        # electrodes = ['FC5', 'FC1', 'FC2', 'FC6', 'C3', 'C4', 'Cz', 'CP5', 'CP6', 'CP1', 'CP2', 'CPz'] # motor area electrodes
        # electrodes = ['FC1', 'FC2', 'C3', 'C4', 'Cz', 'CP1', 'CP2', 'CPz'] # motor area electrodes
        cols = electrode_index(electrodes)

    for i in range((len(event))):
        toc, stimnum = EventData(event[i])
        data_tmp = EEGData(data[i])
        data_deal = DataDeal(cols, toc, data_tmp, dot, fs)
        if i == 0:
            filtered_temp = butter_bandpass_filter(data_deal, low_pass, high_pass, fs, order=6)
            label_temp = stimnum
        else:
            filtered_temp = data_concatenate(butter_bandpass_filter(data_deal, low_pass, high_pass, fs, order=6),
                                             filtered_temp, keep_axis=0)
            label_temp = data_concatenate(stimnum, label_temp, keep_axis=0)

    filtered_data = np.array(filtered_temp)
    label = np.array(label_temp)

    return filtered_data, label

# data concatenate for feedback
def feedback_data(event, data, fs, time, cap):
    dot = time * fs
    low_pass = 3
    high_pass = 30

    filtered_temp = []
    label_temp = []
    # ANT
    if cap == 'old':
        electrodes = ['PO7', 'P3', 'Pz', 'P4', 'POz', 'O1', 'Oz', 'O2']
        cols = electrode_index(electrodes)
    # GREENTEK
    elif cap == 'new':
        electrodes = ['PO3', 'PO4', 'PO7', 'Pz', 'P4', 'POz', 'O1', 'Oz', 'O2']
        # electrodes = ['PO3', 'PO4', 'PO7', 'Pz', 'P4', 'POz', 'O1', 'Oz'] # cross equipments
        cols = electrode_index(electrodes)

    for i in range((len(event))):
        toc, stimnum = EventData(event[i])
        data_tmp = EEGData(data[i])
        data_deal = DataDeal(cols, toc, data_tmp, dot, fs)
        if i == 0:
            filtered_temp = butter_bandpass_filter(data_deal, low_pass, high_pass, fs, order=6)
            label_temp = stimnum
        else:
            filtered_temp = data_concatenate(butter_bandpass_filter(data_deal, low_pass, high_pass, fs, order=6),
                                             filtered_temp, keep_axis=0)
            label_temp = data_concatenate(stimnum, label_temp, keep_axis=0)

    feedback_data = np.array(filtered_temp)
    label = np.array(label_temp)

    return feedback_data, label