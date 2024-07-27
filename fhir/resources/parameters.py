# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Parameters
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import fhirtypes, resource


class Parameters(resource.Resource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Operation Request or Response.
    This resource is used to pass information into and back from an operation
    (whether invoked directly from REST or within a messaging environment).  It
    is not persisted or allowed to be referenced by other resources.
    """

    __resource_type__ = "Parameters"

    parameter: typing.List[fhirtypes.ParametersParameterType] = Field(
        None,
        alias="parameter",
        title="Operation Parameter",
        description="A parameter passed to or received from the operation.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Parameters`` according specification,
        with preserving original sequence order.
        """
        return ["id", "meta", "implicitRules", "language", "parameter"]


from . import backboneelement


class ParametersParameter(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Operation Parameter.
    A parameter passed to or received from the operation.
    """

    __resource_type__ = "ParametersParameter"

    name: fhirtypes.StringType = Field(
        None,
        alias="name",
        title="Name from the definition",
        description="The name of the parameter (reference to the operation definition).",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    part: typing.List[fhirtypes.ParametersParameterType] = Field(
        None,
        alias="part",
        title="Named part of a multi-part parameter",
        description="A named part of a multi-part parameter.",
        json_schema_extra={
            "element_property": True,
        },
    )

    resource: fhirtypes.ResourceType = Field(
        None,
        alias="resource",
        title="If parameter is a whole resource",
        description="Conveys the content if the parameter is a whole resource.",
        json_schema_extra={
            "element_property": True,
        },
    )

    valueAddress: fhirtypes.AddressType = Field(
        None,
        alias="valueAddress",
        title="If parameter is a data type",
        description="Conveys the content if the parameter is a data type.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueAge: fhirtypes.AgeType = Field(
        None,
        alias="valueAge",
        title="If parameter is a data type",
        description="Conveys the content if the parameter is a data type.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueAnnotation: fhirtypes.AnnotationType = Field(
        None,
        alias="valueAnnotation",
        title="If parameter is a data type",
        description="Conveys the content if the parameter is a data type.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueAttachment: fhirtypes.AttachmentType = Field(
        None,
        alias="valueAttachment",
        title="If parameter is a data type",
        description="Conveys the content if the parameter is a data type.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueAvailability: fhirtypes.AvailabilityType = Field(
        None,
        alias="valueAvailability",
        title="If parameter is a data type",
        description="Conveys the content if the parameter is a data type.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueBase64Binary: fhirtypes.Base64BinaryType = Field(
        None,
        alias="valueBase64Binary",
        title="If parameter is a data type",
        description="Conveys the content if the parameter is a data type.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )
    valueBase64Binary__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_valueBase64Binary",
        title="Extension field for ``valueBase64Binary``.",
    )

    valueBoolean: bool = Field(
        None,
        alias="valueBoolean",
        title="If parameter is a data type",
        description="Conveys the content if the parameter is a data type.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueBoolean", title="Extension field for ``valueBoolean``."
    )

    valueCanonical: fhirtypes.CanonicalType = Field(
        None,
        alias="valueCanonical",
        title="If parameter is a data type",
        description="Conveys the content if the parameter is a data type.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )
    valueCanonical__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueCanonical", title="Extension field for ``valueCanonical``."
    )

    valueCode: fhirtypes.CodeType = Field(
        None,
        alias="valueCode",
        title="If parameter is a data type",
        description="Conveys the content if the parameter is a data type.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )
    valueCode__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueCode", title="Extension field for ``valueCode``."
    )

    valueCodeableConcept: fhirtypes.CodeableConceptType = Field(
        None,
        alias="valueCodeableConcept",
        title="If parameter is a data type",
        description="Conveys the content if the parameter is a data type.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueCodeableReference: fhirtypes.CodeableReferenceType = Field(
        None,
        alias="valueCodeableReference",
        title="If parameter is a data type",
        description="Conveys the content if the parameter is a data type.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueCoding: fhirtypes.CodingType = Field(
        None,
        alias="valueCoding",
        title="If parameter is a data type",
        description="Conveys the content if the parameter is a data type.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueContactDetail: fhirtypes.ContactDetailType = Field(
        None,
        alias="valueContactDetail",
        title="If parameter is a data type",
        description="Conveys the content if the parameter is a data type.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueContactPoint: fhirtypes.ContactPointType = Field(
        None,
        alias="valueContactPoint",
        title="If parameter is a data type",
        description="Conveys the content if the parameter is a data type.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueCount: fhirtypes.CountType = Field(
        None,
        alias="valueCount",
        title="If parameter is a data type",
        description="Conveys the content if the parameter is a data type.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueDataRequirement: fhirtypes.DataRequirementType = Field(
        None,
        alias="valueDataRequirement",
        title="If parameter is a data type",
        description="Conveys the content if the parameter is a data type.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueDate: fhirtypes.DateType = Field(
        None,
        alias="valueDate",
        title="If parameter is a data type",
        description="Conveys the content if the parameter is a data type.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )
    valueDate__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueDate", title="Extension field for ``valueDate``."
    )

    valueDateTime: fhirtypes.DateTimeType = Field(
        None,
        alias="valueDateTime",
        title="If parameter is a data type",
        description="Conveys the content if the parameter is a data type.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )
    valueDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueDateTime", title="Extension field for ``valueDateTime``."
    )

    valueDecimal: fhirtypes.DecimalType = Field(
        None,
        alias="valueDecimal",
        title="If parameter is a data type",
        description="Conveys the content if the parameter is a data type.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )
    valueDecimal__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueDecimal", title="Extension field for ``valueDecimal``."
    )

    valueDistance: fhirtypes.DistanceType = Field(
        None,
        alias="valueDistance",
        title="If parameter is a data type",
        description="Conveys the content if the parameter is a data type.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueDosage: fhirtypes.DosageType = Field(
        None,
        alias="valueDosage",
        title="If parameter is a data type",
        description="Conveys the content if the parameter is a data type.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueDuration: fhirtypes.DurationType = Field(
        None,
        alias="valueDuration",
        title="If parameter is a data type",
        description="Conveys the content if the parameter is a data type.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueExpression: fhirtypes.ExpressionType = Field(
        None,
        alias="valueExpression",
        title="If parameter is a data type",
        description="Conveys the content if the parameter is a data type.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueExtendedContactDetail: fhirtypes.ExtendedContactDetailType = Field(
        None,
        alias="valueExtendedContactDetail",
        title="If parameter is a data type",
        description="Conveys the content if the parameter is a data type.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueHumanName: fhirtypes.HumanNameType = Field(
        None,
        alias="valueHumanName",
        title="If parameter is a data type",
        description="Conveys the content if the parameter is a data type.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueId: fhirtypes.IdType = Field(
        None,
        alias="valueId",
        title="If parameter is a data type",
        description="Conveys the content if the parameter is a data type.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )
    valueId__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueId", title="Extension field for ``valueId``."
    )

    valueIdentifier: fhirtypes.IdentifierType = Field(
        None,
        alias="valueIdentifier",
        title="If parameter is a data type",
        description="Conveys the content if the parameter is a data type.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueInstant: fhirtypes.InstantType = Field(
        None,
        alias="valueInstant",
        title="If parameter is a data type",
        description="Conveys the content if the parameter is a data type.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )
    valueInstant__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueInstant", title="Extension field for ``valueInstant``."
    )

    valueInteger: fhirtypes.IntegerType = Field(
        None,
        alias="valueInteger",
        title="If parameter is a data type",
        description="Conveys the content if the parameter is a data type.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )
    valueInteger__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueInteger", title="Extension field for ``valueInteger``."
    )

    valueInteger64: fhirtypes.Integer64Type = Field(
        None,
        alias="valueInteger64",
        title="If parameter is a data type",
        description="Conveys the content if the parameter is a data type.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )
    valueInteger64__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueInteger64", title="Extension field for ``valueInteger64``."
    )

    valueMarkdown: fhirtypes.MarkdownType = Field(
        None,
        alias="valueMarkdown",
        title="If parameter is a data type",
        description="Conveys the content if the parameter is a data type.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )
    valueMarkdown__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueMarkdown", title="Extension field for ``valueMarkdown``."
    )

    valueMeta: fhirtypes.MetaType = Field(
        None,
        alias="valueMeta",
        title="If parameter is a data type",
        description="Conveys the content if the parameter is a data type.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueMoney: fhirtypes.MoneyType = Field(
        None,
        alias="valueMoney",
        title="If parameter is a data type",
        description="Conveys the content if the parameter is a data type.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueOid: fhirtypes.OidType = Field(
        None,
        alias="valueOid",
        title="If parameter is a data type",
        description="Conveys the content if the parameter is a data type.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )
    valueOid__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueOid", title="Extension field for ``valueOid``."
    )

    valueParameterDefinition: fhirtypes.ParameterDefinitionType = Field(
        None,
        alias="valueParameterDefinition",
        title="If parameter is a data type",
        description="Conveys the content if the parameter is a data type.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valuePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="valuePeriod",
        title="If parameter is a data type",
        description="Conveys the content if the parameter is a data type.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valuePositiveInt: fhirtypes.PositiveIntType = Field(
        None,
        alias="valuePositiveInt",
        title="If parameter is a data type",
        description="Conveys the content if the parameter is a data type.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )
    valuePositiveInt__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_valuePositiveInt",
        title="Extension field for ``valuePositiveInt``.",
    )

    valueQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="valueQuantity",
        title="If parameter is a data type",
        description="Conveys the content if the parameter is a data type.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueRange: fhirtypes.RangeType = Field(
        None,
        alias="valueRange",
        title="If parameter is a data type",
        description="Conveys the content if the parameter is a data type.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueRatio: fhirtypes.RatioType = Field(
        None,
        alias="valueRatio",
        title="If parameter is a data type",
        description="Conveys the content if the parameter is a data type.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueRatioRange: fhirtypes.RatioRangeType = Field(
        None,
        alias="valueRatioRange",
        title="If parameter is a data type",
        description="Conveys the content if the parameter is a data type.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueReference: fhirtypes.ReferenceType = Field(
        None,
        alias="valueReference",
        title="If parameter is a data type",
        description="Conveys the content if the parameter is a data type.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueRelatedArtifact: fhirtypes.RelatedArtifactType = Field(
        None,
        alias="valueRelatedArtifact",
        title="If parameter is a data type",
        description="Conveys the content if the parameter is a data type.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueSampledData: fhirtypes.SampledDataType = Field(
        None,
        alias="valueSampledData",
        title="If parameter is a data type",
        description="Conveys the content if the parameter is a data type.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueSignature: fhirtypes.SignatureType = Field(
        None,
        alias="valueSignature",
        title="If parameter is a data type",
        description="Conveys the content if the parameter is a data type.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueString: fhirtypes.StringType = Field(
        None,
        alias="valueString",
        title="If parameter is a data type",
        description="Conveys the content if the parameter is a data type.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueString", title="Extension field for ``valueString``."
    )

    valueTime: fhirtypes.TimeType = Field(
        None,
        alias="valueTime",
        title="If parameter is a data type",
        description="Conveys the content if the parameter is a data type.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )
    valueTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueTime", title="Extension field for ``valueTime``."
    )

    valueTiming: fhirtypes.TimingType = Field(
        None,
        alias="valueTiming",
        title="If parameter is a data type",
        description="Conveys the content if the parameter is a data type.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueTriggerDefinition: fhirtypes.TriggerDefinitionType = Field(
        None,
        alias="valueTriggerDefinition",
        title="If parameter is a data type",
        description="Conveys the content if the parameter is a data type.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueUnsignedInt: fhirtypes.UnsignedIntType = Field(
        None,
        alias="valueUnsignedInt",
        title="If parameter is a data type",
        description="Conveys the content if the parameter is a data type.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )
    valueUnsignedInt__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_valueUnsignedInt",
        title="Extension field for ``valueUnsignedInt``.",
    )

    valueUri: fhirtypes.UriType = Field(
        None,
        alias="valueUri",
        title="If parameter is a data type",
        description="Conveys the content if the parameter is a data type.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )
    valueUri__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueUri", title="Extension field for ``valueUri``."
    )

    valueUrl: fhirtypes.UrlType = Field(
        None,
        alias="valueUrl",
        title="If parameter is a data type",
        description="Conveys the content if the parameter is a data type.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )
    valueUrl__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueUrl", title="Extension field for ``valueUrl``."
    )

    valueUsageContext: fhirtypes.UsageContextType = Field(
        None,
        alias="valueUsageContext",
        title="If parameter is a data type",
        description="Conveys the content if the parameter is a data type.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )

    valueUuid: fhirtypes.UuidType = Field(
        None,
        alias="valueUuid",
        title="If parameter is a data type",
        description="Conveys the content if the parameter is a data type.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e value[x]
            "one_of_many": "value",
            "one_of_many_required": False,
        },
    )
    valueUuid__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_valueUuid", title="Extension field for ``valueUuid``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ParametersParameter`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "name",
            "valueBase64Binary",
            "valueBoolean",
            "valueCanonical",
            "valueCode",
            "valueDate",
            "valueDateTime",
            "valueDecimal",
            "valueId",
            "valueInstant",
            "valueInteger",
            "valueInteger64",
            "valueMarkdown",
            "valueOid",
            "valuePositiveInt",
            "valueString",
            "valueTime",
            "valueUnsignedInt",
            "valueUri",
            "valueUrl",
            "valueUuid",
            "valueAddress",
            "valueAge",
            "valueAnnotation",
            "valueAttachment",
            "valueCodeableConcept",
            "valueCodeableReference",
            "valueCoding",
            "valueContactPoint",
            "valueCount",
            "valueDistance",
            "valueDuration",
            "valueHumanName",
            "valueIdentifier",
            "valueMoney",
            "valuePeriod",
            "valueQuantity",
            "valueRange",
            "valueRatio",
            "valueRatioRange",
            "valueReference",
            "valueSampledData",
            "valueSignature",
            "valueTiming",
            "valueContactDetail",
            "valueDataRequirement",
            "valueExpression",
            "valueParameterDefinition",
            "valueRelatedArtifact",
            "valueTriggerDefinition",
            "valueUsageContext",
            "valueAvailability",
            "valueExtendedContactDetail",
            "valueDosage",
            "valueMeta",
            "resource",
            "part",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("name", "name__ext")]
        return required_fields

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
                "valueAddress",
                "valueAge",
                "valueAnnotation",
                "valueAttachment",
                "valueAvailability",
                "valueBase64Binary",
                "valueBoolean",
                "valueCanonical",
                "valueCode",
                "valueCodeableConcept",
                "valueCodeableReference",
                "valueCoding",
                "valueContactDetail",
                "valueContactPoint",
                "valueCount",
                "valueDataRequirement",
                "valueDate",
                "valueDateTime",
                "valueDecimal",
                "valueDistance",
                "valueDosage",
                "valueDuration",
                "valueExpression",
                "valueExtendedContactDetail",
                "valueHumanName",
                "valueId",
                "valueIdentifier",
                "valueInstant",
                "valueInteger",
                "valueInteger64",
                "valueMarkdown",
                "valueMeta",
                "valueMoney",
                "valueOid",
                "valueParameterDefinition",
                "valuePeriod",
                "valuePositiveInt",
                "valueQuantity",
                "valueRange",
                "valueRatio",
                "valueRatioRange",
                "valueReference",
                "valueRelatedArtifact",
                "valueSampledData",
                "valueSignature",
                "valueString",
                "valueTime",
                "valueTiming",
                "valueTriggerDefinition",
                "valueUnsignedInt",
                "valueUri",
                "valueUrl",
                "valueUsageContext",
                "valueUuid",
            ]
        }
        return one_of_many_fields
