import os
import django
import sys

# Add the path to your project to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))  # Adjust the path
sys.path.append(project_root)

# Set the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'arborfindr.settings'  # Correct path to settings

# Set up Django
django.setup()

# Your import and logic here
import json
from arborfindr.models import ArboristCompany, ArboristReview, ServicesType
from django.utils.dateparse import parse_datetime

from models import Homeowner

# Load data from JSON file
with open('C:\\Users\\corey james\\Documents\\CJProjects\\treesbegone\\NewProject\\arborfindr\\pikes_peak.json', 'r') as f:
    data = json.load(f)

# Data structure from JSON
company_data = data.get("company")
review_data = data.get("review")

# Insert ArboristCompany data
company_name = company_data["name"]
company_city, company_state = company_data["location"].split(", ")

# Create ArboristCompany object
arborist_company = ArboristCompany.objects.create(
    company_name=company_name,
    company_city=company_city,
    company_state=company_state,
    experience="5 years",  # Static data
    company_price=100,
)

# Insert ArboristReview data
reviewer_name = review_data["reviewer"].strip("- ").strip()  # Remove unwanted characters
review_text = review_data["review_text"].strip()

# Get Homeowner object
homeowner = Homeowner.objects.get(user__username=reviewer_name)

# Create ArboristReview object
ArboristReview.objects.create(
    arborist_company=arborist_company,
    user=homeowner,
    rating=5,
    review_text=review_text,
)

# Insert ServicesType data
services = company_data["services"]
services_type = ServicesType.objects.create(
    arborist=arborist_company,
    tree_pruning=services[0],
    tree_removal=services[1],
    tree_planting=services[2],
    pesticide_applications=services[3],
    soil_management=services[4],
    tree_protection=services[5],
    tree_risk_management=services[6],
    tree_biology=services[7],
)

print("Pikes Peak Service data successfully imported to db")


