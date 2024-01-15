# try:
#     file = open('a_file.text')
#     a_dictionary = {'key': 'value'}
#     print(a_dictionary['hekk'])
# except FileNotFoundError:
#     file = open('a_file.text', 'w')
#     file.write('howdy')
# height = float(input('Height: '))
# weight = int(input('Weight: '))
#
# if height > 3:
#     raise TypeError('test')
#
# bmi = weight / height ** 2
# print(bmi)
#
# input = ['Apple', 'Pear', 'Orange']
#
# def make_pie(index):
#
#     try:
#         fruit = input[index]
#     except:
#         print('fruit pie')
#     else:
#         print(fruit + ' pie')
#
# make_pie(4)

facebook_posts = [{'Likes': 21, 'Comments': 2},
                  {'Likes': 13, 'Comments': 2, 'Shares': 1},
                  {'Likes': 33, 'Comments': 8, 'Shares': 3},
                  {'Comments': 4, 'Shares': 2},
                  {'Comments': 1, 'Shares': 1},
                  {'Likes': 19, 'Comments': 3}
                  ]

total_likes = 0
for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        pass

print(total_likes)
