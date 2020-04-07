def user_profile(first, last, **user_infos):
    profile = {}
    profile['first name'] = first
    profile['last name'] = last
    for k, v in user_infos.items():
        profile[k] = v
    return profile


print(user_profile('Mo', 'Boustta',
                   age=21,
                   profssion='Student',
                   location='Morocco'))
