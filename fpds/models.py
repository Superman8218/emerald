from __future__ import unicode_literals

from django.db import models

legend = {
    'modNumber': 'modification_number',
    'transactionNumber': 'transaction_number',
    'solicitationID': 'solicitation_identifier',
    'lastDateToOrder': 'idv_last_date',
    'baseAndExercisedOptionsValue': 'current_contract_value',
    'obligatedAmount': 'obligated_amount',
    'contractingOfficeAgencyID': 'contracting_agency',
    'contractingOfficeID': 'contracting_office',
    'fundingRequestingAgencyID': 'funding_agency_code',
    'fundingRequestingOfficeID': 'funding_office_code',
}

class FpdsMaster(models.Model):

    agency = models.CharField(max_length=50)
    agency_id = models.CharField(max_length=10)
    piid = models.CharField(max_length=6)
    mod_number = models.IntegerField()
    transaction_number = models.IntegerField()
    referenced_idvid_agency_name = models.CharField(max_length=100)
    referenced_idvid_agency_id = models.CharField(max_length=6)
    referenced_idvid_mod_number = models.IntegerField()


    # The unique identifier for each contract, agreement, or order.
    piid = models.CharField(max_length=50)

    # An identifier issued by an agency that uniquely identifies one modification for one contract, agreement, order, etc.
    modification_number = models.CharField(max_length=25)

    # The ID of the IDV that the award is linked to
    referenced_piid = models.CharField(max_length=50) # Fix

    # Tie Breaker for legal, unique transactions that would otherwise have the same key
    transaction_number = models.IntegerField()

    # Identifier used to link agency in FPDS-NG to award information.
    agency_id = models.CharField(max_length=4)

    # Identifier used to link transactions in FPDS-NG to solicitation information.
    solicitation_identifier = models.CharField(max_length=25)

    # The Modification number of the IDV against which the order is placed.
    referenced_idv_modification_number = models.CharField(max_length=25) # Fix

    # The agency ID for the IDV against which the order is placed. When
    # reporting the initial load of a BPA under a FSS, report the agency ID associated
    # with FSS contract number. Leave blank if the IDV is unique, and agency ID is
    # not required to uniquely identify the delivery vehicle.
    referenced_idv_agency_id = models.CharField(max_length=4) # Fix

    # The date that a mutually binding agreement was reached. The date signed by the
    # Contracting Officer or the Contractor, whichever is later.
    date_signed = models.DateField()

    # The date that the parties agree will be the starting date for the contract's
    # requirements. The Effective Date cannot be earlier than the Signed Date on the
    # base document.
    effective_date = models.DateField()

    # Report the contract completion date based on the schedule in the contract. For an
    # initial award, report the scheduled completion date for the base contract and for
    # any options exercised at time of award. For modifications that exercise options,
    # report the revised scheduled completion date for the base contract including
    # exercised options.
    current_completion_date = models.DateField()

    # The estimated or scheduled completion date including the base contract or order
    # and all options (if any) whether the options have been exercised or not.
    ultimate_completion_date = models.DateField()

    # Last date on which an order may be placed against this indefinite delivery vehicle.
    idv_last_date = models.DateField()

    # It is the mutually agreed upon total contract or order value including all options
    # (if any). For Indefinite Delivery Vehicles, the estimated value for all orders
    # expected to be placed against the vehicle. For modifications, the change (positive
    # or negative, if any) in the mutually agreed upon total contract value.
    ultimate_contract_value = models.DecimalField(max_digits=20, decimal_places=2)

    # For a new award/IDV: Enter the total value (in dollars and cents) of the base
    # contract plus all options (if any) that have been exercised at the time of award.
    # For a modification:'Enter the CHANGE (positive or negative, if any) in the
    # current contract value that results from this modification.
    current_contract_value = models.DecimalField(max_digits=20, decimal_places=2)

    # The amount that is obligated or de-obligated by this transaction.
    dollars_obligation = models.DecimalField(max_digits=20, decimal_places=2)

    # The code for the agency of the contracting office that executed or is otherwise responsible for the transaction.
    contracting_agency = models.CharField(max_length=4)

    # The agency supplied code of the contracting office that executes the transaction.
    contracting_office_code = models.CharField(max_length=4)

    # The code for the agency that provided the preponderance of the funds obligated by this transaction
    funding_agency_id = models.CharField(max_length=4)

    # The funding agency provided code that identifies the office that proveded the preponderance of funds.
    # If the Funding Agency is a non-DoD agency, the ocnde is defined by the agency.
    # If the funding agency is a DoD agency, the code is the DoD Activity Address Code
    funding_office_code = models.CharField(max_length=6)

    # Indicates that a foreign government, international organization, or foreign military organization bears some of the cost of the acquisition
    foreign_funding = models.CharField(max_length=1) # Should be restricted to a set number of choices

    # The web site URL for inter agency Indefinite Delivery Vehicles
    url_of_program = models.URLField(max_length=100)

    # Agencies that may place orders against this indefinite delivery vehicle.
    who_can_use = models.CharField(max_length=255) # Choices

    # Maximum dollar amount that can be applied to a single order against the Indefinite Delivery Vehicle.
    maximum_order_limit = models.DecimalField(max_digits=22, decimal_places=2)

    # List of administrative fees charged for using an Indefinite Delivery Vehicle other
    # than Federal Supply Schedule (FSS) Vehicle. The fees can be one of the
    # following format: 1) Fixed, 2) Range - Varies by amount, and 3) Range - Varies
    # by Other Factor.
    fee_for_use_of_service = models.CharField(max_length=3)

    # The value if "Fixed Fee" is chosen for Fee for Use of Service (5D).
    fixed_fee_value = models.CharField(max_length=6)

    # The lower value if "Range" (RVA, RVO) is chosen for Fee for Use of Service
    fee_range_lower_value = models.IntegerField()

    # The upper value if "Range" is chosen for Fee for Use of Service (5D).
    fee_range_upper_value = models.IntegerField()

    # For the initial load of the IDV, describe ordering procedures, unless included in
    # the government website listed in the "Web Site URL" data element (5A).
    ordering_procedure = models.TextField()

    # Actual fee paid in order to use the IDV.
    fee_paid_for_use_of_service = models.DecimalField(max_digits=22, decimal_places=2)

    # The email address of the point of contact for an IDV, contractor, contracting
    # agency, reporting agency, customer, or offset officer.
    email_address = models.EmailField()

    # The type of contract as defined in FAR Part 16 that applies to this procurement.
    type_of_contract_pricing = models.CharField(max_length=1)


# Create your models here.
