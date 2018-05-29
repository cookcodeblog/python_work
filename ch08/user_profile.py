# 8-13 User Profile


def build_profile(last_name, first_name, **description):
    """Two star means accept dictionary parameter (each key-value pair is a parameter)"""
    profile = {'last_name': last_name, 'first_name': first_name}
    for k, v in description.items():
        profile[k] = v
    return profile


# key-value pair format is "<key>=<value>"
william = build_profile("William", "Lin", age=32, married=True, children=2)
print(william)

