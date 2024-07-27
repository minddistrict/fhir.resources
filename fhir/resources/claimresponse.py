# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ClaimResponse
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import domainresource, fhirtypes


class ClaimResponse(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Response to a claim predetermination or preauthorization.
    This resource provides the adjudication details from the processing of a
    Claim resource.
    """

    __resource_type__ = "ClaimResponse"

    addItem: typing.List[fhirtypes.ClaimResponseAddItemType] = Field(
        None,
        alias="addItem",
        title="Insurer added line items",
        description=(
            "The first-tier service adjudications for payor added product or "
            "service lines."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    adjudication: typing.List[fhirtypes.ClaimResponseItemAdjudicationType] = Field(
        None,
        alias="adjudication",
        title="Header-level adjudication",
        description=(
            "The adjudication results which are presented at the header level "
            "rather than at the line-item or add-item levels."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    communicationRequest: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="communicationRequest",
        title="Request for additional information",
        description="Request for additional supporting or authorizing information.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["CommunicationRequest"],
        },
    )

    created: fhirtypes.DateTimeType = Field(
        None,
        alias="created",
        title="Response creation date",
        description="The date this resource was created.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    created__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_created", title="Extension field for ``created``."
    )

    decision: fhirtypes.CodeableConceptType = Field(
        None,
        alias="decision",
        title="Result of the adjudication",
        description=(
            "The result of the claim, predetermination, or preauthorization "
            "adjudication."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    diagnosisRelatedGroup: fhirtypes.CodeableConceptType = Field(
        None,
        alias="diagnosisRelatedGroup",
        title="Package billing code",
        description=(
            "A package billing code or bundle code used to group products and "
            "services to a particular health condition (such as heart attack) which"
            " is based on a predetermined grouping code system."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    disposition: fhirtypes.StringType = Field(
        None,
        alias="disposition",
        title="Disposition Message",
        description="A human readable description of the status of the adjudication.",
        json_schema_extra={
            "element_property": True,
        },
    )
    disposition__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_disposition", title="Extension field for ``disposition``."
    )

    encounter: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="encounter",
        title="Encounters associated with the listed treatments",
        description="Healthcare encounters related to this claim.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Encounter"],
        },
    )

    error: typing.List[fhirtypes.ClaimResponseErrorType] = Field(
        None,
        alias="error",
        title="Processing errors",
        description="Errors encountered during the processing of the adjudication.",
        json_schema_extra={
            "element_property": True,
        },
    )

    event: typing.List[fhirtypes.ClaimResponseEventType] = Field(
        None,
        alias="event",
        title="Event information",
        description="Information code for an event with a corresponding date or period.",
        json_schema_extra={
            "element_property": True,
        },
    )

    form: fhirtypes.AttachmentType = Field(
        None,
        alias="form",
        title="Printed reference or actual form",
        description=(
            "The actual form, by reference or inclusion, for printing the content "
            "or an EOB."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    formCode: fhirtypes.CodeableConceptType = Field(
        None,
        alias="formCode",
        title="Printed form identifier",
        description="A code for the form to be used for printing the content.",
        json_schema_extra={
            "element_property": True,
        },
    )

    fundsReserve: fhirtypes.CodeableConceptType = Field(
        None,
        alias="fundsReserve",
        title="Funds reserved status",
        description=(
            "A code, used only on a response to a preauthorization, to indicate "
            "whether the benefits payable have been reserved and for whom."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Business Identifier for a claim response",
        description="A unique identifier assigned to this claim response.",
        json_schema_extra={
            "element_property": True,
        },
    )

    insurance: typing.List[fhirtypes.ClaimResponseInsuranceType] = Field(
        None,
        alias="insurance",
        title="Patient insurance information",
        description=(
            "Financial instruments for reimbursement for the health care products "
            "and services specified on the claim."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    insurer: fhirtypes.ReferenceType = Field(
        None,
        alias="insurer",
        title="Party responsible for reimbursement",
        description=(
            "The party responsible for authorization, adjudication and "
            "reimbursement."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    item: typing.List[fhirtypes.ClaimResponseItemType] = Field(
        None,
        alias="item",
        title="Adjudication for claim line items",
        description=(
            "A claim line. Either a simple (a product or service) or a 'group' of "
            "details which can also be a simple items or groups of sub-details."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    outcome: fhirtypes.CodeType = Field(
        None,
        alias="outcome",
        title="queued | complete | error | partial",
        description=(
            "The outcome of the claim, predetermination, or preauthorization "
            "processing."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["queued", "complete", "error", "partial"],
        },
    )
    outcome__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_outcome", title="Extension field for ``outcome``."
    )

    patient: fhirtypes.ReferenceType = Field(
        ...,
        alias="patient",
        title="The recipient of the products and services",
        description=(
            "The party to whom the professional services and/or products have been "
            "supplied or are being considered and for whom actual for facast "
            "reimbursement is sought."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Patient"],
        },
    )

    payeeType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="payeeType",
        title="Party to be paid any benefits payable",
        description="Type of Party to be reimbursed: subscriber, provider, other.",
        json_schema_extra={
            "element_property": True,
        },
    )

    payment: fhirtypes.ClaimResponsePaymentType = Field(
        None,
        alias="payment",
        title="Payment Details",
        description="Payment details for the adjudication of the claim.",
        json_schema_extra={
            "element_property": True,
        },
    )

    preAuthPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="preAuthPeriod",
        title="Preauthorization reference effective period",
        description="The time frame during which this authorization is effective.",
        json_schema_extra={
            "element_property": True,
        },
    )

    preAuthRef: fhirtypes.StringType = Field(
        None,
        alias="preAuthRef",
        title="Preauthorization reference",
        description=(
            "Reference from the Insurer which is used in later communications which"
            " refers to this adjudication."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    preAuthRef__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_preAuthRef", title="Extension field for ``preAuthRef``."
    )

    processNote: typing.List[fhirtypes.ClaimResponseProcessNoteType] = Field(
        None,
        alias="processNote",
        title="Note concerning adjudication",
        description=(
            "A note that describes or explains adjudication results in a human "
            "readable form."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    request: fhirtypes.ReferenceType = Field(
        None,
        alias="request",
        title="Id of resource triggering adjudication",
        description="Original request resource reference.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Claim"],
        },
    )

    requestor: fhirtypes.ReferenceType = Field(
        None,
        alias="requestor",
        title="Party responsible for the claim",
        description=(
            "The provider which is responsible for the claim, predetermination or "
            "preauthorization."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Practitioner",
                "PractitionerRole",
                "Organization",
            ],
        },
    )

    status: fhirtypes.CodeType = Field(
        None,
        alias="status",
        title="active | cancelled | draft | entered-in-error",
        description="The status of the resource instance.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["active", "cancelled", "draft", "entered-in-error"],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    subType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="subType",
        title="More granular claim type",
        description=(
            "A finer grained suite of claim type codes which may convey additional "
            "information such as Inpatient vs Outpatient and/or a specialty "
            "service."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    total: typing.List[fhirtypes.ClaimResponseTotalType] = Field(
        None,
        alias="total",
        title="Adjudication totals",
        description="Categorized monetary totals for the adjudication.",
        json_schema_extra={
            "element_property": True,
        },
    )

    traceNumber: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="traceNumber",
        title="Number for tracking",
        description=(
            "Trace number for tracking purposes. May be defined at the jurisdiction"
            " level or between trading partners."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="More granular claim type",
        description=(
            "A finer grained suite of claim type codes which may convey additional "
            "information such as Inpatient vs Outpatient and/or a specialty "
            "service."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    use: fhirtypes.CodeType = Field(
        None,
        alias="use",
        title="claim | preauthorization | predetermination",
        description=(
            "A code to indicate whether the nature of the request is: Claim - A "
            "request to an Insurer to adjudicate the supplied charges for health "
            "care goods and services under the identified policy and to pay the "
            "determined Benefit amount, if any; Preauthorization - A request to an "
            "Insurer to adjudicate the supplied proposed future charges for health "
            "care goods and services under the identified policy and to approve the"
            " services and provide the expected benefit amounts and potentially to "
            "reserve funds to pay the benefits when Claims for the indicated "
            "services are later submitted; or, Pre-determination - A request to an "
            "Insurer to adjudicate the supplied 'what if' charges for health care "
            "goods and services under the identified policy and report back what "
            "the Benefit payable would be had the services actually been provided."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["claim", "preauthorization", "predetermination"],
        },
    )
    use__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_use", title="Extension field for ``use``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClaimResponse`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "meta",
            "implicitRules",
            "language",
            "text",
            "contained",
            "extension",
            "modifierExtension",
            "identifier",
            "traceNumber",
            "status",
            "type",
            "subType",
            "use",
            "patient",
            "created",
            "insurer",
            "requestor",
            "request",
            "outcome",
            "decision",
            "disposition",
            "preAuthRef",
            "preAuthPeriod",
            "event",
            "payeeType",
            "encounter",
            "diagnosisRelatedGroup",
            "item",
            "addItem",
            "adjudication",
            "total",
            "payment",
            "fundsReserve",
            "formCode",
            "form",
            "processNote",
            "communicationRequest",
            "insurance",
            "error",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [
            ("created", "created__ext"),
            ("outcome", "outcome__ext"),
            ("status", "status__ext"),
            ("use", "use__ext"),
        ]
        return required_fields


from . import backboneelement


class ClaimResponseAddItem(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Insurer added line items.
    The first-tier service adjudications for payor added product or service
    lines.
    """

    __resource_type__ = "ClaimResponseAddItem"

    adjudication: typing.List[fhirtypes.ClaimResponseItemAdjudicationType] = Field(
        None,
        alias="adjudication",
        title="Added items adjudication",
        description="The adjudication results.",
        json_schema_extra={
            "element_property": True,
        },
    )

    bodySite: typing.List[fhirtypes.ClaimResponseAddItemBodySiteType] = Field(
        None,
        alias="bodySite",
        title="Anatomical location",
        description="Physical location where the service is performed or applies.",
        json_schema_extra={
            "element_property": True,
        },
    )

    detail: typing.List[fhirtypes.ClaimResponseAddItemDetailType] = Field(
        None,
        alias="detail",
        title="Insurer added line details",
        description="The second-tier service adjudications for payor added services.",
        json_schema_extra={
            "element_property": True,
        },
    )

    detailSequence: typing.List[typing.Optional[fhirtypes.PositiveIntType]] = Field(
        None,
        alias="detailSequence",
        title="Detail sequence number",
        description=(
            "The sequence number of the details within the claim item which this "
            "line is intended to replace."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    detailSequence__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None, alias="_detailSequence", title="Extension field for ``detailSequence``."
    )

    factor: fhirtypes.DecimalType = Field(
        None,
        alias="factor",
        title="Price scaling factor",
        description=(
            "A real number that represents a multiplier used in determining the "
            "overall value of services delivered and/or goods received. The concept"
            " of a Factor allows for a discount or surcharge multiplier to be "
            "applied to a monetary amount."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    factor__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_factor", title="Extension field for ``factor``."
    )

    itemSequence: typing.List[typing.Optional[fhirtypes.PositiveIntType]] = Field(
        None,
        alias="itemSequence",
        title="Item sequence number",
        description="Claim items which this service line is intended to replace.",
        json_schema_extra={
            "element_property": True,
        },
    )
    itemSequence__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None, alias="_itemSequence", title="Extension field for ``itemSequence``."
    )

    locationAddress: fhirtypes.AddressType = Field(
        None,
        alias="locationAddress",
        title="Place of service or where product was supplied",
        description="Where the product or service was provided.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e location[x]
            "one_of_many": "location",
            "one_of_many_required": False,
        },
    )

    locationCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="locationCodeableConcept",
        title="Place of service or where product was supplied",
        description="Where the product or service was provided.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e location[x]
            "one_of_many": "location",
            "one_of_many_required": False,
        },
    )

    locationReference: fhirtypes.ReferenceType = Field(
        None,
        alias="locationReference",
        title="Place of service or where product was supplied",
        description="Where the product or service was provided.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e location[x]
            "one_of_many": "location",
            "one_of_many_required": False,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Location"],
        },
    )

    modifier: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="modifier",
        title="Service/Product billing modifiers",
        description=(
            "Item typification or modifiers codes to convey additional context for "
            "the product or service."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    net: fhirtypes.MoneyType = Field(
        None,
        alias="net",
        title="Total item cost",
        description=(
            "The total amount claimed for the group (if a grouper) or the addItem. "
            "Net = unit price * quantity * factor."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    noteNumber: typing.List[typing.Optional[fhirtypes.PositiveIntType]] = Field(
        None,
        alias="noteNumber",
        title="Applicable note numbers",
        description=(
            "The numbers associated with notes below which apply to the "
            "adjudication of this item."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    noteNumber__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_noteNumber", title="Extension field for ``noteNumber``.")

    productOrService: fhirtypes.CodeableConceptType = Field(
        None,
        alias="productOrService",
        title="Billing, service, product, or drug code",
        description=(
            "When the value is a group code then this item collects a set of "
            "related item details, otherwise this contains the product, service, "
            "drug or other billing code for the item. This element may be the start"
            " of a range of .productOrService codes used in conjunction with "
            ".productOrServiceEnd or it may be a solo element where "
            ".productOrServiceEnd is not used."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    productOrServiceEnd: fhirtypes.CodeableConceptType = Field(
        None,
        alias="productOrServiceEnd",
        title="End of a range of codes",
        description=(
            "This contains the end of a range of product, service, drug or other "
            "billing codes for the item. This element is not used when the "
            ".productOrService is a group code. This value may only be present when"
            " a .productOfService code has been provided to convey the start of the"
            " range. Typically this value may be used only with preauthorizations "
            "and not with claims."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    programCode: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="programCode",
        title="Program the product or service is provided under",
        description="Identifies the program under which this may be recovered.",
        json_schema_extra={
            "element_property": True,
        },
    )

    provider: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="provider",
        title="Authorized providers",
        description=(
            "The providers who are authorized for the services rendered to the "
            "patient."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Practitioner",
                "PractitionerRole",
                "Organization",
            ],
        },
    )

    quantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantity",
        title="Count of products or services",
        description="The number of repetitions of a service or product.",
        json_schema_extra={
            "element_property": True,
        },
    )

    request: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="request",
        title="Request or Referral for Service",
        description="Request or Referral for Goods or Service to be rendered.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "DeviceRequest",
                "MedicationRequest",
                "NutritionOrder",
                "ServiceRequest",
                "SupplyRequest",
                "VisionPrescription",
            ],
        },
    )

    revenue: fhirtypes.CodeableConceptType = Field(
        None,
        alias="revenue",
        title="Revenue or cost center code",
        description=(
            "The type of revenue or cost center providing the product and/or "
            "service."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    reviewOutcome: fhirtypes.ClaimResponseItemReviewOutcomeType = Field(
        None,
        alias="reviewOutcome",
        title="Added items adjudication results",
        description=(
            "The high-level results of the adjudication if adjudication has been "
            "performed."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    servicedDate: fhirtypes.DateType = Field(
        None,
        alias="servicedDate",
        title="Date or dates of service or product delivery",
        description=(
            "The date or dates when the service or product was supplied, performed "
            "or completed."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e serviced[x]
            "one_of_many": "serviced",
            "one_of_many_required": False,
        },
    )
    servicedDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_servicedDate", title="Extension field for ``servicedDate``."
    )

    servicedPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="servicedPeriod",
        title="Date or dates of service or product delivery",
        description=(
            "The date or dates when the service or product was supplied, performed "
            "or completed."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e serviced[x]
            "one_of_many": "serviced",
            "one_of_many_required": False,
        },
    )

    subdetailSequence: typing.List[typing.Optional[fhirtypes.PositiveIntType]] = Field(
        None,
        alias="subdetailSequence",
        title="Subdetail sequence number",
        description=(
            "The sequence number of the sub-details within the details within the "
            "claim item which this line is intended to replace."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    subdetailSequence__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None,
        alias="_subdetailSequence",
        title="Extension field for ``subdetailSequence``.",
    )

    tax: fhirtypes.MoneyType = Field(
        None,
        alias="tax",
        title="Total tax",
        description="The total of taxes applicable for this product or service.",
        json_schema_extra={
            "element_property": True,
        },
    )

    traceNumber: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="traceNumber",
        title="Number for tracking",
        description=(
            "Trace number for tracking purposes. May be defined at the jurisdiction"
            " level or between trading partners."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    unitPrice: fhirtypes.MoneyType = Field(
        None,
        alias="unitPrice",
        title="Fee, charge or cost per item",
        description=(
            "If the item is not a group then this is the fee for the product or "
            "service, otherwise this is the total of the fees for the details of "
            "the group."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClaimResponseAddItem`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "itemSequence",
            "detailSequence",
            "subdetailSequence",
            "traceNumber",
            "provider",
            "revenue",
            "productOrService",
            "productOrServiceEnd",
            "request",
            "modifier",
            "programCode",
            "servicedDate",
            "servicedPeriod",
            "locationCodeableConcept",
            "locationAddress",
            "locationReference",
            "quantity",
            "unitPrice",
            "factor",
            "tax",
            "net",
            "bodySite",
            "noteNumber",
            "reviewOutcome",
            "adjudication",
            "detail",
        ]

    def get_one_of_many_fields(self) -> typing.Dict[str, typing.List[str]]:
        """https://www.hl7.org/fhir/formats.html#choice
        A few elements have a choice of more than one data type for their content.
        All such elements have a name that takes the form nnn[x].
        The "nnn" part of the name is constant, and the "[x]" is replaced with
        the title-cased name of the type that is actually used.
        The table view shows each of these names explicitly.

        Elements that have a choice of data type cannot repeat - they must have a
        maximum cardinality of 1. When constructing an instance of an element with a
        choice of types, the authoring system must create a single element with a
        data type chosen from among the list of permitted data types.
        """
        one_of_many_fields = {
            "location": [
                "locationAddress",
                "locationCodeableConcept",
                "locationReference",
            ],
            "serviced": ["servicedDate", "servicedPeriod"],
        }
        return one_of_many_fields


class ClaimResponseAddItemBodySite(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Anatomical location.
    Physical location where the service is performed or applies.
    """

    __resource_type__ = "ClaimResponseAddItemBodySite"

    site: typing.List[fhirtypes.CodeableReferenceType] = Field(
        ...,
        alias="site",
        title="Location",
        description="Physical service site on the patient (limb, tooth, etc.).",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["BodyStructure"],
        },
    )

    subSite: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="subSite",
        title="Sub-location",
        description=(
            "A region or surface of the bodySite, e.g. limb region or tooth "
            "surface(s)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClaimResponseAddItemBodySite`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "site", "subSite"]


class ClaimResponseAddItemDetail(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Insurer added line details.
    The second-tier service adjudications for payor added services.
    """

    __resource_type__ = "ClaimResponseAddItemDetail"

    adjudication: typing.List[fhirtypes.ClaimResponseItemAdjudicationType] = Field(
        None,
        alias="adjudication",
        title="Added items detail adjudication",
        description="The adjudication results.",
        json_schema_extra={
            "element_property": True,
        },
    )

    factor: fhirtypes.DecimalType = Field(
        None,
        alias="factor",
        title="Price scaling factor",
        description=(
            "A real number that represents a multiplier used in determining the "
            "overall value of services delivered and/or goods received. The concept"
            " of a Factor allows for a discount or surcharge multiplier to be "
            "applied to a monetary amount."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    factor__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_factor", title="Extension field for ``factor``."
    )

    modifier: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="modifier",
        title="Service/Product billing modifiers",
        description=(
            "Item typification or modifiers codes to convey additional context for "
            "the product or service."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    net: fhirtypes.MoneyType = Field(
        None,
        alias="net",
        title="Total item cost",
        description=(
            "The total amount claimed for the group (if a grouper) or the "
            "addItem.detail. Net = unit price * quantity * factor."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    noteNumber: typing.List[typing.Optional[fhirtypes.PositiveIntType]] = Field(
        None,
        alias="noteNumber",
        title="Applicable note numbers",
        description=(
            "The numbers associated with notes below which apply to the "
            "adjudication of this item."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    noteNumber__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_noteNumber", title="Extension field for ``noteNumber``.")

    productOrService: fhirtypes.CodeableConceptType = Field(
        None,
        alias="productOrService",
        title="Billing, service, product, or drug code",
        description=(
            "When the value is a group code then this item collects a set of "
            "related item details, otherwise this contains the product, service, "
            "drug or other billing code for the item. This element may be the start"
            " of a range of .productOrService codes used in conjunction with "
            ".productOrServiceEnd or it may be a solo element where "
            ".productOrServiceEnd is not used."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    productOrServiceEnd: fhirtypes.CodeableConceptType = Field(
        None,
        alias="productOrServiceEnd",
        title="End of a range of codes",
        description=(
            "This contains the end of a range of product, service, drug or other "
            "billing codes for the item. This element is not used when the "
            ".productOrService is a group code. This value may only be present when"
            " a .productOfService code has been provided to convey the start of the"
            " range. Typically this value may be used only with preauthorizations "
            "and not with claims."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    quantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantity",
        title="Count of products or services",
        description="The number of repetitions of a service or product.",
        json_schema_extra={
            "element_property": True,
        },
    )

    revenue: fhirtypes.CodeableConceptType = Field(
        None,
        alias="revenue",
        title="Revenue or cost center code",
        description=(
            "The type of revenue or cost center providing the product and/or "
            "service."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    reviewOutcome: fhirtypes.ClaimResponseItemReviewOutcomeType = Field(
        None,
        alias="reviewOutcome",
        title="Added items detail level adjudication results",
        description=(
            "The high-level results of the adjudication if adjudication has been "
            "performed."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    subDetail: typing.List[fhirtypes.ClaimResponseAddItemDetailSubDetailType] = Field(
        None,
        alias="subDetail",
        title="Insurer added line items",
        description="The third-tier service adjudications for payor added services.",
        json_schema_extra={
            "element_property": True,
        },
    )

    tax: fhirtypes.MoneyType = Field(
        None,
        alias="tax",
        title="Total tax",
        description="The total of taxes applicable for this product or service.",
        json_schema_extra={
            "element_property": True,
        },
    )

    traceNumber: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="traceNumber",
        title="Number for tracking",
        description=(
            "Trace number for tracking purposes. May be defined at the jurisdiction"
            " level or between trading partners."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    unitPrice: fhirtypes.MoneyType = Field(
        None,
        alias="unitPrice",
        title="Fee, charge or cost per item",
        description=(
            "If the item is not a group then this is the fee for the product or "
            "service, otherwise this is the total of the fees for the details of "
            "the group."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClaimResponseAddItemDetail`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "traceNumber",
            "revenue",
            "productOrService",
            "productOrServiceEnd",
            "modifier",
            "quantity",
            "unitPrice",
            "factor",
            "tax",
            "net",
            "noteNumber",
            "reviewOutcome",
            "adjudication",
            "subDetail",
        ]


class ClaimResponseAddItemDetailSubDetail(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Insurer added line items.
    The third-tier service adjudications for payor added services.
    """

    __resource_type__ = "ClaimResponseAddItemDetailSubDetail"

    adjudication: typing.List[fhirtypes.ClaimResponseItemAdjudicationType] = Field(
        None,
        alias="adjudication",
        title="Added items subdetail adjudication",
        description="The adjudication results.",
        json_schema_extra={
            "element_property": True,
        },
    )

    factor: fhirtypes.DecimalType = Field(
        None,
        alias="factor",
        title="Price scaling factor",
        description=(
            "A real number that represents a multiplier used in determining the "
            "overall value of services delivered and/or goods received. The concept"
            " of a Factor allows for a discount or surcharge multiplier to be "
            "applied to a monetary amount."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    factor__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_factor", title="Extension field for ``factor``."
    )

    modifier: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="modifier",
        title="Service/Product billing modifiers",
        description=(
            "Item typification or modifiers codes to convey additional context for "
            "the product or service."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    net: fhirtypes.MoneyType = Field(
        None,
        alias="net",
        title="Total item cost",
        description=(
            "The total amount claimed for the addItem.detail.subDetail. Net = unit "
            "price * quantity * factor."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    noteNumber: typing.List[typing.Optional[fhirtypes.PositiveIntType]] = Field(
        None,
        alias="noteNumber",
        title="Applicable note numbers",
        description=(
            "The numbers associated with notes below which apply to the "
            "adjudication of this item."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    noteNumber__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_noteNumber", title="Extension field for ``noteNumber``.")

    productOrService: fhirtypes.CodeableConceptType = Field(
        None,
        alias="productOrService",
        title="Billing, service, product, or drug code",
        description=(
            "When the value is a group code then this item collects a set of "
            "related item details, otherwise this contains the product, service, "
            "drug or other billing code for the item. This element may be the start"
            " of a range of .productOrService codes used in conjunction with "
            ".productOrServiceEnd or it may be a solo element where "
            ".productOrServiceEnd is not used."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    productOrServiceEnd: fhirtypes.CodeableConceptType = Field(
        None,
        alias="productOrServiceEnd",
        title="End of a range of codes",
        description=(
            "This contains the end of a range of product, service, drug or other "
            "billing codes for the item. This element is not used when the "
            ".productOrService is a group code. This value may only be present when"
            " a .productOfService code has been provided to convey the start of the"
            " range. Typically this value may be used only with preauthorizations "
            "and not with claims."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    quantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantity",
        title="Count of products or services",
        description="The number of repetitions of a service or product.",
        json_schema_extra={
            "element_property": True,
        },
    )

    revenue: fhirtypes.CodeableConceptType = Field(
        None,
        alias="revenue",
        title="Revenue or cost center code",
        description=(
            "The type of revenue or cost center providing the product and/or "
            "service."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    reviewOutcome: fhirtypes.ClaimResponseItemReviewOutcomeType = Field(
        None,
        alias="reviewOutcome",
        title="Added items subdetail level adjudication results",
        description=(
            "The high-level results of the adjudication if adjudication has been "
            "performed."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    tax: fhirtypes.MoneyType = Field(
        None,
        alias="tax",
        title="Total tax",
        description="The total of taxes applicable for this product or service.",
        json_schema_extra={
            "element_property": True,
        },
    )

    traceNumber: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="traceNumber",
        title="Number for tracking",
        description=(
            "Trace number for tracking purposes. May be defined at the jurisdiction"
            " level or between trading partners."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    unitPrice: fhirtypes.MoneyType = Field(
        None,
        alias="unitPrice",
        title="Fee, charge or cost per item",
        description=(
            "If the item is not a group then this is the fee for the product or "
            "service, otherwise this is the total of the fees for the details of "
            "the group."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClaimResponseAddItemDetailSubDetail`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "traceNumber",
            "revenue",
            "productOrService",
            "productOrServiceEnd",
            "modifier",
            "quantity",
            "unitPrice",
            "factor",
            "tax",
            "net",
            "noteNumber",
            "reviewOutcome",
            "adjudication",
        ]


class ClaimResponseError(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Processing errors.
    Errors encountered during the processing of the adjudication.
    """

    __resource_type__ = "ClaimResponseError"

    code: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="code",
        title="Error code detailing processing issues",
        description=(
            "An error code, from a specified code system, which details why the "
            "claim could not be adjudicated."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    detailSequence: fhirtypes.PositiveIntType = Field(
        None,
        alias="detailSequence",
        title="Detail sequence number",
        description=(
            "The sequence number of the detail within the line item submitted which"
            " contains the error. This value is omitted when the error occurs "
            "outside of the item structure."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    detailSequence__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_detailSequence", title="Extension field for ``detailSequence``."
    )

    expression: typing.List[typing.Optional[fhirtypes.StringType]] = Field(
        None,
        alias="expression",
        title="FHIRPath of element(s) related to issue",
        description=(
            "A [simple subset of FHIRPath](fhirpath.html#simple) limited to element"
            " names, repetition indicators and the default child accessor that "
            "identifies one of the elements in the resource that caused this issue "
            "to be raised."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    expression__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_expression", title="Extension field for ``expression``.")

    itemSequence: fhirtypes.PositiveIntType = Field(
        None,
        alias="itemSequence",
        title="Item sequence number",
        description=(
            "The sequence number of the line item submitted which contains the "
            "error. This value is omitted when the error occurs outside of the item"
            " structure."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    itemSequence__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_itemSequence", title="Extension field for ``itemSequence``."
    )

    subDetailSequence: fhirtypes.PositiveIntType = Field(
        None,
        alias="subDetailSequence",
        title="Subdetail sequence number",
        description=(
            "The sequence number of the sub-detail within the detail within the "
            "line item submitted which contains the error. This value is omitted "
            "when the error occurs outside of the item structure."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    subDetailSequence__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_subDetailSequence",
        title="Extension field for ``subDetailSequence``.",
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClaimResponseError`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "itemSequence",
            "detailSequence",
            "subDetailSequence",
            "code",
            "expression",
        ]


class ClaimResponseEvent(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Event information.
    Information code for an event with a corresponding date or period.
    """

    __resource_type__ = "ClaimResponseEvent"

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Specific event",
        description="A coded event such as when a service is expected or a card printed.",
        json_schema_extra={
            "element_property": True,
        },
    )

    whenDateTime: fhirtypes.DateTimeType = Field(
        None,
        alias="whenDateTime",
        title="Occurance date or period",
        description=(
            "A date or period in the past or future indicating when the event "
            "occurred or is expectd to occur."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e when[x]
            "one_of_many": "when",
            "one_of_many_required": True,
        },
    )
    whenDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_whenDateTime", title="Extension field for ``whenDateTime``."
    )

    whenPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="whenPeriod",
        title="Occurance date or period",
        description=(
            "A date or period in the past or future indicating when the event "
            "occurred or is expectd to occur."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e when[x]
            "one_of_many": "when",
            "one_of_many_required": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClaimResponseEvent`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "type",
            "whenDateTime",
            "whenPeriod",
        ]

    def get_one_of_many_fields(self) -> typing.Dict[str, typing.List[str]]:
        """https://www.hl7.org/fhir/formats.html#choice
        A few elements have a choice of more than one data type for their content.
        All such elements have a name that takes the form nnn[x].
        The "nnn" part of the name is constant, and the "[x]" is replaced with
        the title-cased name of the type that is actually used.
        The table view shows each of these names explicitly.

        Elements that have a choice of data type cannot repeat - they must have a
        maximum cardinality of 1. When constructing an instance of an element with a
        choice of types, the authoring system must create a single element with a
        data type chosen from among the list of permitted data types.
        """
        one_of_many_fields = {"when": ["whenDateTime", "whenPeriod"]}
        return one_of_many_fields


class ClaimResponseInsurance(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Patient insurance information.
    Financial instruments for reimbursement for the health care products and
    services specified on the claim.
    """

    __resource_type__ = "ClaimResponseInsurance"

    businessArrangement: fhirtypes.StringType = Field(
        None,
        alias="businessArrangement",
        title="Additional provider contract number",
        description=(
            "A business agreement number established between the provider and the "
            "insurer for special business processing purposes."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    businessArrangement__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_businessArrangement",
        title="Extension field for ``businessArrangement``.",
    )

    claimResponse: fhirtypes.ReferenceType = Field(
        None,
        alias="claimResponse",
        title="Adjudication results",
        description=(
            "The result of the adjudication of the line items for the Coverage "
            "specified in this insurance."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ClaimResponse"],
        },
    )

    coverage: fhirtypes.ReferenceType = Field(
        ...,
        alias="coverage",
        title="Insurance information",
        description=(
            "Reference to the insurance card level information contained in the "
            "Coverage resource. The coverage issuing insurer will use these details"
            " to locate the patient's actual coverage within the insurer's "
            "information system."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Coverage"],
        },
    )

    focal: bool = Field(
        None,
        alias="focal",
        title="Coverage to be used for adjudication",
        description=(
            "A flag to indicate that this Coverage is to be used for adjudication "
            "of this claim when set to true."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    focal__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_focal", title="Extension field for ``focal``."
    )

    sequence: fhirtypes.PositiveIntType = Field(
        None,
        alias="sequence",
        title="Insurance instance identifier",
        description=(
            "A number to uniquely identify insurance entries and provide a sequence"
            " of coverages to convey coordination of benefit order."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_sequence", title="Extension field for ``sequence``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClaimResponseInsurance`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "sequence",
            "focal",
            "coverage",
            "businessArrangement",
            "claimResponse",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("focal", "focal__ext"), ("sequence", "sequence__ext")]
        return required_fields


class ClaimResponseItem(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Adjudication for claim line items.
    A claim line. Either a simple (a product or service) or a 'group' of
    details which can also be a simple items or groups of sub-details.
    """

    __resource_type__ = "ClaimResponseItem"

    adjudication: typing.List[fhirtypes.ClaimResponseItemAdjudicationType] = Field(
        None,
        alias="adjudication",
        title="Adjudication details",
        description=(
            "If this item is a group then the values here are a summary of the "
            "adjudication of the detail items. If this item is a simple product or "
            "service then this is the result of the adjudication of this item."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    detail: typing.List[fhirtypes.ClaimResponseItemDetailType] = Field(
        None,
        alias="detail",
        title="Adjudication for claim details",
        description=(
            "A claim detail. Either a simple (a product or service) or a 'group' of"
            " sub-details which are simple items."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    itemSequence: fhirtypes.PositiveIntType = Field(
        None,
        alias="itemSequence",
        title="Claim item instance identifier",
        description="A number to uniquely reference the claim item entries.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    itemSequence__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_itemSequence", title="Extension field for ``itemSequence``."
    )

    noteNumber: typing.List[typing.Optional[fhirtypes.PositiveIntType]] = Field(
        None,
        alias="noteNumber",
        title="Applicable note numbers",
        description=(
            "The numbers associated with notes below which apply to the "
            "adjudication of this item."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    noteNumber__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_noteNumber", title="Extension field for ``noteNumber``.")

    reviewOutcome: fhirtypes.ClaimResponseItemReviewOutcomeType = Field(
        None,
        alias="reviewOutcome",
        title="Adjudication results",
        description=(
            "The high-level results of the adjudication if adjudication has been "
            "performed."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    traceNumber: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="traceNumber",
        title="Number for tracking",
        description=(
            "Trace number for tracking purposes. May be defined at the jurisdiction"
            " level or between trading partners."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClaimResponseItem`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "itemSequence",
            "traceNumber",
            "noteNumber",
            "reviewOutcome",
            "adjudication",
            "detail",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("itemSequence", "itemSequence__ext")]
        return required_fields


class ClaimResponseItemAdjudication(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Adjudication details.
    If this item is a group then the values here are a summary of the
    adjudication of the detail items. If this item is a simple product or
    service then this is the result of the adjudication of this item.
    """

    __resource_type__ = "ClaimResponseItemAdjudication"

    amount: fhirtypes.MoneyType = Field(
        None,
        alias="amount",
        title="Monetary amount",
        description="Monetary amount associated with the category.",
        json_schema_extra={
            "element_property": True,
        },
    )

    category: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="category",
        title="Type of adjudication information",
        description=(
            "A code to indicate the information type of this adjudication record. "
            "Information types may include the value submitted, maximum values or "
            "percentages allowed or payable under the plan, amounts that: the "
            "patient is responsible for in aggregate or pertaining to this item; "
            "amounts paid by other coverages; and, the benefit payable for this "
            "item."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    quantity: fhirtypes.QuantityType = Field(
        None,
        alias="quantity",
        title="Non-monetary value",
        description=(
            "A non-monetary value associated with the category. Mutually exclusive "
            "to the amount element above."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    reason: fhirtypes.CodeableConceptType = Field(
        None,
        alias="reason",
        title="Explanation of adjudication outcome",
        description=(
            "A code supporting the understanding of the adjudication result and "
            "explaining variance from expected amount."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClaimResponseItemAdjudication`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "category",
            "reason",
            "amount",
            "quantity",
        ]


class ClaimResponseItemDetail(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Adjudication for claim details.
    A claim detail. Either a simple (a product or service) or a 'group' of sub-
    details which are simple items.
    """

    __resource_type__ = "ClaimResponseItemDetail"

    adjudication: typing.List[fhirtypes.ClaimResponseItemAdjudicationType] = Field(
        None,
        alias="adjudication",
        title="Detail level adjudication details",
        description="The adjudication results.",
        json_schema_extra={
            "element_property": True,
        },
    )

    detailSequence: fhirtypes.PositiveIntType = Field(
        None,
        alias="detailSequence",
        title="Claim detail instance identifier",
        description="A number to uniquely reference the claim detail entry.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    detailSequence__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_detailSequence", title="Extension field for ``detailSequence``."
    )

    noteNumber: typing.List[typing.Optional[fhirtypes.PositiveIntType]] = Field(
        None,
        alias="noteNumber",
        title="Applicable note numbers",
        description=(
            "The numbers associated with notes below which apply to the "
            "adjudication of this item."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    noteNumber__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_noteNumber", title="Extension field for ``noteNumber``.")

    reviewOutcome: fhirtypes.ClaimResponseItemReviewOutcomeType = Field(
        None,
        alias="reviewOutcome",
        title="Detail level adjudication results",
        description=(
            "The high-level results of the adjudication if adjudication has been "
            "performed."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    subDetail: typing.List[fhirtypes.ClaimResponseItemDetailSubDetailType] = Field(
        None,
        alias="subDetail",
        title="Adjudication for claim sub-details",
        description="A sub-detail adjudication of a simple product or service.",
        json_schema_extra={
            "element_property": True,
        },
    )

    traceNumber: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="traceNumber",
        title="Number for tracking",
        description=(
            "Trace number for tracking purposes. May be defined at the jurisdiction"
            " level or between trading partners."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClaimResponseItemDetail`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "detailSequence",
            "traceNumber",
            "noteNumber",
            "reviewOutcome",
            "adjudication",
            "subDetail",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("detailSequence", "detailSequence__ext")]
        return required_fields


class ClaimResponseItemDetailSubDetail(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Adjudication for claim sub-details.
    A sub-detail adjudication of a simple product or service.
    """

    __resource_type__ = "ClaimResponseItemDetailSubDetail"

    adjudication: typing.List[fhirtypes.ClaimResponseItemAdjudicationType] = Field(
        None,
        alias="adjudication",
        title="Subdetail level adjudication details",
        description="The adjudication results.",
        json_schema_extra={
            "element_property": True,
        },
    )

    noteNumber: typing.List[typing.Optional[fhirtypes.PositiveIntType]] = Field(
        None,
        alias="noteNumber",
        title="Applicable note numbers",
        description=(
            "The numbers associated with notes below which apply to the "
            "adjudication of this item."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    noteNumber__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_noteNumber", title="Extension field for ``noteNumber``.")

    reviewOutcome: fhirtypes.ClaimResponseItemReviewOutcomeType = Field(
        None,
        alias="reviewOutcome",
        title="Subdetail level adjudication results",
        description=(
            "The high-level results of the adjudication if adjudication has been "
            "performed."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    subDetailSequence: fhirtypes.PositiveIntType = Field(
        None,
        alias="subDetailSequence",
        title="Claim sub-detail instance identifier",
        description="A number to uniquely reference the claim sub-detail entry.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    subDetailSequence__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_subDetailSequence",
        title="Extension field for ``subDetailSequence``.",
    )

    traceNumber: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="traceNumber",
        title="Number for tracking",
        description=(
            "Trace number for tracking purposes. May be defined at the jurisdiction"
            " level or between trading partners."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClaimResponseItemDetailSubDetail`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "subDetailSequence",
            "traceNumber",
            "noteNumber",
            "reviewOutcome",
            "adjudication",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("subDetailSequence", "subDetailSequence__ext")]
        return required_fields


class ClaimResponseItemReviewOutcome(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Adjudication results.
    The high-level results of the adjudication if adjudication has been
    performed.
    """

    __resource_type__ = "ClaimResponseItemReviewOutcome"

    decision: fhirtypes.CodeableConceptType = Field(
        None,
        alias="decision",
        title="Result of the adjudication",
        description=(
            "The result of the claim, predetermination, or preauthorization "
            "adjudication."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    preAuthPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="preAuthPeriod",
        title="Preauthorization reference effective period",
        description="The time frame during which this authorization is effective.",
        json_schema_extra={
            "element_property": True,
        },
    )

    preAuthRef: fhirtypes.StringType = Field(
        None,
        alias="preAuthRef",
        title="Preauthorization reference",
        description=(
            "Reference from the Insurer which is used in later communications which"
            " refers to this adjudication."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    preAuthRef__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_preAuthRef", title="Extension field for ``preAuthRef``."
    )

    reason: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reason",
        title="Reason for result of the adjudication",
        description=(
            "The reasons for the result of the claim, predetermination, or "
            "preauthorization adjudication."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClaimResponseItemReviewOutcome`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "decision",
            "reason",
            "preAuthRef",
            "preAuthPeriod",
        ]


class ClaimResponsePayment(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Payment Details.
    Payment details for the adjudication of the claim.
    """

    __resource_type__ = "ClaimResponsePayment"

    adjustment: fhirtypes.MoneyType = Field(
        None,
        alias="adjustment",
        title="Payment adjustment for non-claim issues",
        description=(
            "Total amount of all adjustments to this payment included in this "
            "transaction which are not related to this claim's adjudication."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    adjustmentReason: fhirtypes.CodeableConceptType = Field(
        None,
        alias="adjustmentReason",
        title="Explanation for the adjustment",
        description="Reason for the payment adjustment.",
        json_schema_extra={
            "element_property": True,
        },
    )

    amount: fhirtypes.MoneyType = Field(
        ...,
        alias="amount",
        title="Payable amount after adjustment",
        description="Benefits payable less any payment adjustment.",
        json_schema_extra={
            "element_property": True,
        },
    )

    date: fhirtypes.DateType = Field(
        None,
        alias="date",
        title="Expected date of payment",
        description=(
            "Estimated date the payment will be issued or the actual issue date of "
            "payment."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Business identifier for the payment",
        description="Issuer's unique identifier for the payment instrument.",
        json_schema_extra={
            "element_property": True,
        },
    )

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Partial or complete payment",
        description=(
            "Whether this represents partial or complete payment of the benefits "
            "payable."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClaimResponsePayment`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "type",
            "adjustment",
            "adjustmentReason",
            "date",
            "amount",
            "identifier",
        ]


class ClaimResponseProcessNote(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Note concerning adjudication.
    A note that describes or explains adjudication results in a human readable
    form.
    """

    __resource_type__ = "ClaimResponseProcessNote"

    language: fhirtypes.CodeableConceptType = Field(
        None,
        alias="language",
        title="Language of the text",
        description="A code to define the language used in the text of the note.",
        json_schema_extra={
            "element_property": True,
        },
    )

    number: fhirtypes.PositiveIntType = Field(
        None,
        alias="number",
        title="Note instance identifier",
        description="A number to uniquely identify a note entry.",
        json_schema_extra={
            "element_property": True,
        },
    )
    number__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_number", title="Extension field for ``number``."
    )

    text: fhirtypes.StringType = Field(
        None,
        alias="text",
        title="Note explanatory text",
        description="The explanation or description associated with the processing.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    text__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_text", title="Extension field for ``text``."
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Note purpose",
        description="The business purpose of the note text.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClaimResponseProcessNote`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "number",
            "type",
            "text",
            "language",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("text", "text__ext")]
        return required_fields


class ClaimResponseTotal(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Adjudication totals.
    Categorized monetary totals for the adjudication.
    """

    __resource_type__ = "ClaimResponseTotal"

    amount: fhirtypes.MoneyType = Field(
        ...,
        alias="amount",
        title="Financial total for the category",
        description="Monetary total amount associated with the category.",
        json_schema_extra={
            "element_property": True,
        },
    )

    category: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="category",
        title="Type of adjudication information",
        description=(
            "A code to indicate the information type of this adjudication record. "
            "Information types may include: the value submitted, maximum values or "
            "percentages allowed or payable under the plan, amounts that the "
            "patient is responsible for in aggregate or pertaining to this item, "
            "amounts paid by other coverages, and the benefit payable for this "
            "item."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ClaimResponseTotal`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "category", "amount"]
