#check slug value

from django.utils.text import slugify
import random , string

def random_string_generator(chars=10, letters=string.ascii_lowercase + string.ascii_uppercase + string.digits):
    return (''.join(random.choice(letters) for i in range(10)))

def check_slug_unique(instance, new_slug=None):
    if new_slug:
        slug = new_slug
    else:
        slug = random_string_generator(chars=10)

    temp = instance.__class__
    query = temp.objects.filter(slug=slug).exists()
    if query:
        slug = random_string_generator(chars=10)
        #recursive
        return check_slug_unique(instance, new_slug=slug)
    # print(slug)
    return slug