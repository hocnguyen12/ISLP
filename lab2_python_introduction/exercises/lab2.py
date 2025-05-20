import pandas as pd

if __name__ == '__main__':
    college = pd.read_csv("../../ALL CSV FILES - 2nd Edition/College.csv")
    college3 = college._rename({'Unnamed: 0': 'College'}, axis=1)
    college3 = college3.set_index('College')
    college = college3
    print(college)

    print(pd.DataFrame.describe(college))

