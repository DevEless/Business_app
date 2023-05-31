import django
django.setup()

from business_app.seed import run
from business_app.seed import run2

if __name__== '__main__':
    run()
    run2()
