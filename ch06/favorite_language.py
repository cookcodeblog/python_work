# 6-6 Favorite Language

favorite_language = {
    'William': 'Python',
    'Tome': 'Bash',
    'Lily': 'JavaScript',
    'Peiqi': 'English'
}

to_survey_names = ['William', 'Tome', 'Lucy', 'Lilei', 'Jimmy', 'Peiqi', 'Jobs']

for name in to_survey_names:
    if name in favorite_language.keys():
        print(name.title() + ", Thanks for joining favorite language survey!")
    else:
        print(name.title() + ", What is your favorite language?")

