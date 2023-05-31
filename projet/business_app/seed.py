from django_seed import Seed    
from .models import Article
from .models import Project
from faker import Faker
import random

def run():
    Article.objects.all().delete()
    fake = Faker()
    seeder = Seed.seeder()
    seeder.add_entity(Article, 4, {
        'titre': lambda x: fake.sentence(nb_words=3, variable_nb_words=True),
        'image': lambda x: generate_random_image(),
        'description': lambda x: fake.text(max_nb_chars=300)
    })
    inserted_pks = seeder.execute()
    print(inserted_pks)

def run2():
    Project.objects.all().delete()
    fake = Faker()
    seeder = Seed.seeder()
    seeder.add_entity(Project, 15, {
        'titre': lambda x: fake.text(max_nb_chars=50),
        'image': lambda x: generate_random_image(),
        'description': lambda x: fake.text(),
    })
    inserted_pks = seeder.execute()
    print(inserted_pks)


def generate_random_image():
    image_number = random.randint(1, 10)
    image_filename = f"portfolio-{image_number}.jpg"
    return f"business_app/img/{image_filename}"