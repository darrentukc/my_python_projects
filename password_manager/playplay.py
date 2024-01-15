import pandas as pd

# df = pd.DataFrame(columns=['website', 'email/username', 'password'])
# df.to_csv('test.csv', index=False)
#
# df = pd.read_csv('data.csv')
# df.loc[df['website'] == 'amazon', 'password'] = 'new_passwprd'
#
# print(df)

new_website = 'google'
new_email = 'darrentu@engbeefood.com'
new_password = '345'

with open('data.txt', 'r+') as file:
    line = file.readlines()
    website_list = [item.split('|')[0].strip() for item in line]
    print(website_list)
    if new_website in website_list:
        new_df = df[df['website'] == new_website]
        print(new_df)
    # username_list = [item.split('|')[1].strip() for item in line]