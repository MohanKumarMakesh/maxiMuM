def user_directory_path(instance, filename):
    'function to create path for user images'
    return 'user_{0}/{1}'.format(instance.user.id, filename)
