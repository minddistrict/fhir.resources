# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/BiologicallyDerivedProduct
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import domainresource, fhirtypes


class BiologicallyDerivedProduct(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    This resource reflects an instance of a biologically derived product.
    This resource reflects an instance of a biologically derived product. A
    material substance originating from a biological entity intended to be
    transplanted or infused
    into another (possibly the same) biological entity.
    """

    __resource_type__ = "BiologicallyDerivedProduct"

    biologicalSourceEvent: fhirtypes.IdentifierType = Field(
        None,
        alias="biologicalSourceEvent",
        title=(
            "An identifier that supports traceability to the event during which "
            "material in this product from one or more biological entities was "
            "obtained or pooled"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    collection: fhirtypes.BiologicallyDerivedProductCollectionType = Field(
        None,
        alias="collection",
        title="How this product was collected",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    division: fhirtypes.StringType = Field(
        None,
        alias="division",
        title="A unique identifier for an aliquot of a product",
        description=(
            "A unique identifier for an aliquot of a product.  Used to distinguish "
            "individual aliquots of a product carrying the same biologicalSource "
            "and productCode identifiers."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    division__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_division", title="Extension field for ``division``."
    )

    expirationDate: fhirtypes.DateTimeType = Field(
        None,
        alias="expirationDate",
        title="Date, and where relevant time, of expiration",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    expirationDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_expirationDate", title="Extension field for ``expirationDate``."
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Instance identifier",
        description=(
            "Unique instance identifiers assigned to a biologically derived "
            "product. Note: This is a business identifier, not a resource "
            "identifier."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    parent: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="parent",
        title="The parent biologically-derived product",
        description="Parent product (if any) for this biologically-derived product.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["BiologicallyDerivedProduct"],
        },
    )

    processingFacility: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="processingFacility",
        title=(
            "Processing facilities responsible for the labeling and distribution of"
            " this biologically derived product"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Organization"],
        },
    )

    productCategory: fhirtypes.CodingType = Field(
        None,
        alias="productCategory",
        title="organ | tissue | fluid | cells | biologicalAgent",
        description="Broad category of this product.",
        json_schema_extra={
            "element_property": True,
        },
    )

    productCode: fhirtypes.CodeableConceptType = Field(
        None,
        alias="productCode",
        title="A code that identifies the kind of this biologically derived product",
        description=(
            "A codified value that systematically supports characterization and "
            "classification of medical products of human origin inclusive of "
            "processing conditions such as additives, volumes and handling "
            "conditions."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    productStatus: fhirtypes.CodingType = Field(
        None,
        alias="productStatus",
        title="available | unavailable",
        description="Whether the product is currently available.",
        json_schema_extra={
            "element_property": True,
        },
    )

    property: typing.List[fhirtypes.BiologicallyDerivedProductPropertyType] = Field(
        None,
        alias="property",
        title=(
            "A property that is specific to this BiologicallyDerviedProduct " "instance"
        ),
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )

    request: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="request",
        title="Request to obtain and/or infuse this product",
        description="Request to obtain and/or infuse this biologically derived product.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["ServiceRequest"],
        },
    )

    storageTempRequirements: fhirtypes.RangeType = Field(
        None,
        alias="storageTempRequirements",
        title="Product storage temperature requirements",
        description=(
            "The temperature requirements for storage of the biologically-derived "
            "product."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``BiologicallyDerivedProduct`` according specification,
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
            "productCategory",
            "productCode",
            "parent",
            "request",
            "identifier",
            "biologicalSourceEvent",
            "processingFacility",
            "division",
            "productStatus",
            "expirationDate",
            "collection",
            "storageTempRequirements",
            "property",
        ]


from . import backboneelement


class BiologicallyDerivedProductCollection(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    How this product was collected.
    """

    __resource_type__ = "BiologicallyDerivedProductCollection"

    collectedDateTime: fhirtypes.DateTimeType = Field(
        None,
        alias="collectedDateTime",
        title="Time of product collection",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e collected[x]
            "one_of_many": "collected",
            "one_of_many_required": False,
        },
    )
    collectedDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_collectedDateTime",
        title="Extension field for ``collectedDateTime``.",
    )

    collectedPeriod: fhirtypes.PeriodType = Field(
        None,
        alias="collectedPeriod",
        title="Time of product collection",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e collected[x]
            "one_of_many": "collected",
            "one_of_many_required": False,
        },
    )

    collector: fhirtypes.ReferenceType = Field(
        None,
        alias="collector",
        title="Individual performing collection",
        description="Healthcare professional who is performing the collection.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Practitioner", "PractitionerRole"],
        },
    )

    source: fhirtypes.ReferenceType = Field(
        None,
        alias="source",
        title=(
            "The patient who underwent the medical procedure to collect the product"
            " or the organization that facilitated the collection"
        ),
        description=(
            "The patient or entity, such as a hospital or vendor in the case of a "
            "processed/manipulated/manufactured product, providing the product."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Patient", "Organization"],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``BiologicallyDerivedProductCollection`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "collector",
            "source",
            "collectedDateTime",
            "collectedPeriod",
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
        one_of_many_fields = {"collected": ["collectedDateTime", "collectedPeriod"]}
        return one_of_many_fields


class BiologicallyDerivedProductProperty(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A property that is specific to this BiologicallyDerviedProduct instance.
    """

    __resource_type__ = "BiologicallyDerivedProductProperty"

    type: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="type",
        title="Code that specifies the property",
        description=(
            "Code that specifies the property. It should reference an established "
            "coding system."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    valueAttachment: fhirtypes.AttachmentType = Field(
        None,
        alias="valueAttachment",
        title="Property values",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )

    valueBoolean: bool = Field(
        None,
        alias="valueBoolean",
        title="Property values",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueBoolean", title="Extension field for ``valueBoolean``."
    )

    valueCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="valueCodeableConcept",
        title="Property values",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )

    valueInteger: fhirtypes.IntegerType = Field(
        None,
        alias="valueInteger",
        title="Property values",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )
    valueInteger__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueInteger", title="Extension field for ``valueInteger``."
    )

    valuePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="valuePeriod",
        title="Property values",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )

    valueQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="valueQuantity",
        title="Property values",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )

    valueRange: fhirtypes.RangeType = Field(
        None,
        alias="valueRange",
        title="Property values",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )

    valueRatio: fhirtypes.RatioType = Field(
        None,
        alias="valueRatio",
        title="Property values",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )

    valueString: fhirtypes.StringType = Field(
        None,
        alias="valueString",
        title="Property values",
        description=None,
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": True,
        },
    )
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueString", title="Extension field for ``valueString``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``BiologicallyDerivedProductProperty`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "type",
            "valueBoolean",
            "valueInteger",
            "valueCodeableConcept",
            "valuePeriod",
            "valueQuantity",
            "valueRange",
            "valueRatio",
            "valueString",
            "valueAttachment",
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
            "value": [
                "valueAttachment",
                "valueBoolean",
                "valueCodeableConcept",
                "valueInteger",
                "valuePeriod",
                "valueQuantity",
                "valueRange",
                "valueRatio",
                "valueString",
            ]
        }
        return one_of_many_fields
