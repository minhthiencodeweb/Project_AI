import os

filepath=(r'C:\Users\PC_MINH THIEN\PycharmProjects\PythonProjectAI2\attend.csv')

if os.path.exists(filepath) == True:
    os.remove('attend.csv')
