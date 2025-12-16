# AO-BCI-inner-domain-decode
load data and label of different paradigms from matlab files. Decoding them by TDCA.  
### 1. files structure
ao_files: the path of bci files in own computer.  
create_xlsx: save the result to xlsx file. the result should be a list.  
data_label: load data and label from matlab files by different rules.  
gene_idx: generate index of data and label by set random seed.  

### 2. how to use?
a. open anaconda:  
conda create -n your_env_name python=3.10  
conda activate your_env_name  
D:  
cd the_requirements_txt_path  
pip install -r requirements.txt  

b. run the test.ipynb  
