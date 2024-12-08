from arborfindr.models import ArboristCompany, ArboristReview, ServiceType
from models.pikes_peak_db import company_name, arborist_company, review_text


def save_to_db(results):

    """
    save Google API results to db
    :param results: list of dictionaries with data
    """

    for result in results:

        company, created = ArboristCompany.objects.update_or_create(
            company_name=result['title'], # create company name here
            defaults={
                'company_city': result['city_state'].split(", ")[0],  # Extract city
                'company_state': result['city_state'].split(", ")[1] if ", " in result['city_state'] else "N/A",

            }
        )

        for services_type in result['types_of_service']:
            service, _ = ServiceType.objects.get_or_create(name=services_type)
            company.services.add(service) # links service to company

        for review in result['reviews']:
            ArboristReview.objects.create(
                arborist_company=company,
                review_text=review['text'], # reviewer name isn't connected to this review
                user=None,
            )

        company.save() # saves updates to company