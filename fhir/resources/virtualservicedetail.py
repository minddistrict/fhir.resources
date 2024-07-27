# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/VirtualServiceDetail
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import datatype, fhirtypes


class VirtualServiceDetail(datatype.DataType):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Virtual Service Contact Details.
    """

    __resource_type__ = "VirtualServiceDetail"

    additionalInfo: typing.List[typing.Optional[fhirtypes.UrlType]] = Field(
        None,
        alias="additionalInfo",
        title="Address to see alternative connection details",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    additionalInfo__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(
        None, alias="_additionalInfo", title="Extension field for ``additionalInfo``."
    )

    addressContactPoint: fhirtypes.ContactPointType = Field(
        None,
        alias="addressContactPoint",
        title="Contact address/number",
        description=(
            "What address or number needs to be used for a user to connect to the "
            "virtual service to join. The channelType informs as to which datatype "
            "is appropriate to use (requires knowledge of the specific type)."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e address[x]
            "one_of_many": "address",
            "one_of_many_required": False,
        },
    )

    addressExtendedContactDetail: fhirtypes.ExtendedContactDetailType = Field(
        None,
        alias="addressExtendedContactDetail",
        title="Contact address/number",
        description=(
            "What address or number needs to be used for a user to connect to the "
            "virtual service to join. The channelType informs as to which datatype "
            "is appropriate to use (requires knowledge of the specific type)."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e address[x]
            "one_of_many": "address",
            "one_of_many_required": False,
        },
    )

    addressString: fhirtypes.StringType = Field(
        None,
        alias="addressString",
        title="Contact address/number",
        description=(
            "What address or number needs to be used for a user to connect to the "
            "virtual service to join. The channelType informs as to which datatype "
            "is appropriate to use (requires knowledge of the specific type)."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e address[x]
            "one_of_many": "address",
            "one_of_many_required": False,
        },
    )
    addressString__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_addressString", title="Extension field for ``addressString``."
    )

    addressUrl: fhirtypes.UrlType = Field(
        None,
        alias="addressUrl",
        title="Contact address/number",
        description=(
            "What address or number needs to be used for a user to connect to the "
            "virtual service to join. The channelType informs as to which datatype "
            "is appropriate to use (requires knowledge of the specific type)."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e address[x]
            "one_of_many": "address",
            "one_of_many_required": False,
        },
    )
    addressUrl__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_addressUrl", title="Extension field for ``addressUrl``."
    )

    channelType: fhirtypes.CodingType = Field(
        None,
        alias="channelType",
        title="Channel Type",
        description=(
            "The type of virtual service to connect to (i.e. Teams, Zoom, Specific "
            "VMR technology, WhatsApp)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    maxParticipants: fhirtypes.PositiveIntType = Field(
        None,
        alias="maxParticipants",
        title="Maximum number of participants supported by the virtual service",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    maxParticipants__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_maxParticipants", title="Extension field for ``maxParticipants``."
    )

    sessionKey: fhirtypes.StringType = Field(
        None,
        alias="sessionKey",
        title="Session Key required by the virtual service",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    sessionKey__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_sessionKey", title="Extension field for ``sessionKey``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``VirtualServiceDetail`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "channelType",
            "addressUrl",
            "addressString",
            "addressContactPoint",
            "addressExtendedContactDetail",
            "additionalInfo",
            "maxParticipants",
            "sessionKey",
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
            "address": [
                "addressContactPoint",
                "addressExtendedContactDetail",
                "addressString",
                "addressUrl",
            ]
        }
        return one_of_many_fields
