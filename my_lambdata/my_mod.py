# my_lambdata/my_mod.py

# 1) Train/val/test split for a df
# 2) Replace NaN values with a float

# Enter target in quotes
def split(df, target):
    from sklearn.model_selection import train_test_split

    train, val = train_test_split(df, train_size=0.80, test_size=0.20,
                    stratify=df[target],
                    random_state=42)

    val, test = train_test_split(val, train_size=0.80, test_size=0.20,
                    stratify=val[target],
                    random_state=42)

    return train.shape, val.shape, test.shape

def nans(df):
    df.fillna(999, inplace=True)
    return df.isna().sum()

def enlarge(n):
    """
    This multiplies a number by 100.
    """
    return n * 100

#print('JUNK')
#print('GLOBAL SCOPE')

#y = float(input('PLEASE INPUT A NUMBER TO ENLARGE: '))
#print(enlarge(y))

if __name__ == '__main__':
    # only if run from the command line, invoke
    # the following code:
    # otherwise, don't

    print('JUNK')
    print('GLOBAL SCOPE')

    y = float(input('PLEASE INPUT A NUMBER TO ENLARGE: '))
    print(enlarge(y))

