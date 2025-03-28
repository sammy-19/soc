# home/context_processors.py
from content_manager.models import Program, PageSection

def footer_programs(request):
    """
    Makes a limited list of active programs available to all templates.
    """
    # Fetch e.g., 4 active programs for the footer
    programs = Program.objects.filter(is_active=True).order_by('display_order')[:4]
    return {'footer_programs': programs}

def donation_details(request):
    """
    Makes donation details (from PageSection) available to all templates.
    """
    details_keys = [
        'donate_bank_name', 'donate_account_name', 'donate_account_number',
        'donate_branch_code', 'donate_swift_code',
        'donate_momo_mtn_name', 'donate_momo_mtn_number',
        'donate_momo_airtel_name', 'donate_momo_airtel_number',
        'donate_momo_zamtel_name', 'donate_momo_zamtel_number',
        'donate_contact_number', 'donate_instructions'
    ]
    # Fetch sections in one query if possible, then create a dictionary
    sections = PageSection.objects.filter(section_key__in=details_keys)
    details = {section.section_key: section.content for section in sections}

    # You could also fetch individual items safely:
    # details = {
    #     'donate_bank_name': PageSection.objects.filter(section_key='donate_bank_name').first(),
    #     # ... etc ...
    # } # But this makes many queries

    return {'donation_details': details}