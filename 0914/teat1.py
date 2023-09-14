import pandas as pd

# 設定 CSV 檔案的路徑
#csv_file_path_1 = 'list1.csv'
#csv_file_path_2 = 'list2.csv'


# 使用 pandas 的 read_csv 函式讀取 CSV 檔案並將其轉換為 DataFrame
df_1 = pd.read_csv('list1.csv')
df_2 = pd.read_csv('list2.csv')
# 從 DataFrame 中取出學生名稱欄位，假設欄位名稱為 '學生名稱'，你可以根據實際情況調整
student_names_1 = df_1['Name']
student_names_2 = df_2['Name']


# 將學生名稱轉換為 set 資料型態
student_names_1_set = set(student_names_1)
student_names_2_set = set(student_names_2)

#print(student_names_1_set)
#print(student_names_2_set)
print('The union of 2 sets:')
print(student_names_1_set & student_names_2_set)