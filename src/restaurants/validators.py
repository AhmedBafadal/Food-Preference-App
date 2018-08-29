from django.core.exceptions import ValidationError


CATEGORIES = ['Mexican', 'Italian', 'American', 'British', 'French','Turkish', 'Argentinian','South African', 'Indian','Chinese', 'Thai','Japanese', 'Korean', 'Middle Eastern','Mediteranean','Brazilian','Cuban','Carribean','African', 'Other']

def validate_category(value):
    cat = value.capitalize()
    if not value in CATEGORIES and not cat in CATEGORIES:
        raise ValidationError(f"{value} is not a valid category. Please choose between: Mexican, Italian, American, British, French, Turkish, Argentinian, South African, Indian, Chinese, Thai, Japanese, Korean, Middle Eastern, Mediteranean, Brazilian, Cuban, Carribean, African, or Other.")
