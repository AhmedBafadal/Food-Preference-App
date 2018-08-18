from django.core.exceptions import ValidationError


CATEGORIES = ['Mexican', 'Italian', 'American', 'British', 'French','Turkish', 'Argentinian','South African', 'Indian','Asian', 'Middle Eastern','Mediteranean','Brazilian','Cuban','Carribean','African']

def validate_category(value):
    cat = value.capitalize()
    if not value in CATEGORIES and not cat in CATEGORIES:
        raise ValidationError(f'{value} is not a valid category,')
