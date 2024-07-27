# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/EnrollmentRequest
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import domainresource, fhirtypes


class EnrollmentRequest(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Enroll in coverage.
    This resource provides the insurance enrollment details to the insurer
    regarding a specified coverage.
    """

    __resource_type__ = "EnrollmentRequest"

    candidate: fhirtypes.ReferenceType = Field(
        None,
        alias="candidate",
        title="The subject to be enrolled",
        description="Patient Resource.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Patient"],
        },
    )

    coverage: fhirtypes.ReferenceType = Field(
        None,
        alias="coverage",
        title="Insurance information",
        description="Reference to the program or plan identification, underwriter or payor.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Coverage"],
        },
    )

    created: fhirtypes.DateTimeType = Field(
        None,
        alias="created",
        title="Creation date",
        description="The date when this resource was created.",
        json_schema_extra={
            "element_property": True,
        },
    )
    created__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_created", title="Extension field for ``created``."
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Business Identifier",
        description="The Response business identifier.",
        json_schema_extra={
            "element_property": True,
        },
    )

    insurer: fhirtypes.ReferenceType = Field(
        None,
        alias="insurer",
        title="Target",
        description="The Insurer who is target  of the request.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    provider: fhirtypes.ReferenceType = Field(
        None,
        alias="provider",
        title="Responsible practitioner",
        description=(
            "The practitioner who is responsible for the services rendered to the "
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

    status: fhirtypes.CodeType = Field(
        None,
        alias="status",
        title="active | cancelled | draft | entered-in-error",
        description="The status of the resource instance.",
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["active", "cancelled", "draft", "entered-in-error"],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``EnrollmentRequest`` according specification,
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
            "status",
            "created",
            "insurer",
            "provider",
            "candidate",
            "coverage",
        ]
