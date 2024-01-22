import random
import string


def new_id(size=8, chars=string.ascii_uppercase + string.digits):
    return "".join(random.choices(chars, k=size))
