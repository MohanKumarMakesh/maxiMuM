def user_listing_path(instance, filename):
    'function to create path for car images'
    return 'user_{0}/listing/{1}'.format(instance.seller.user.id, filename)
