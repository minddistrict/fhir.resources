# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/RegulatedAuthorization
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from pathlib import Path

from .. import regulatedauthorization
from .fixtures import ExternalValidatorModel, bytes_validator  # noqa: F401


def impl_regulatedauthorization_1(inst):
    assert inst.holder.display == "EquiliDrugCo Holdings Inc."
    assert inst.holder.reference == "Organization/EqlidrugCo"
    assert inst.id == "basic-drug-auth"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.regulator.display == "FDA"
    assert inst.regulator.reference == "Organization/FDA"
    assert inst.status.coding[0].code == "active"
    assert (
        inst.statusDate
        == ExternalValidatorModel(valueDateTime="2016-01-01").valueDateTime
    )
    assert inst.subject[0].reference == "MedicinalProductDefinition/equilidem"
    assert inst.text.status == "generated"
    assert inst.type.text == "Regulatory Drug Marketing Approval"


def test_regulatedauthorization_1(base_settings):
    """No. 1 tests collection for RegulatedAuthorization.
    Test File: regulatedauthorization-example-basic-drug-auth.json
    """
    filename = (
        base_settings["unittest_data_dir"]
        / "regulatedauthorization-example-basic-drug-auth.json"
    )
    inst = regulatedauthorization.RegulatedAuthorization.model_validate_json(
        Path(filename).read_bytes()
    )
    assert "RegulatedAuthorization" == inst.get_resource_type()

    impl_regulatedauthorization_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "RegulatedAuthorization" == data["resourceType"]

    inst2 = regulatedauthorization.RegulatedAuthorization(**data)
    impl_regulatedauthorization_1(inst2)


def impl_regulatedauthorization_2(inst):
    assert (
        inst.case.application[0].dateDateTime
        == ExternalValidatorModel(valueDateTime="2015-08-01").valueDateTime
    )
    assert (
        inst.case.application[0].identifier.system
        == ExternalValidatorModel(
            valueUri="http://ema.europa.eu/example/applicationidentifier-number"
        ).valueUri
    )
    assert inst.case.application[0].identifier.value == "IA38G"
    assert (
        inst.case.application[0].type.coding[0].code
        == "GroupTypeIAVariationNotification"
    )
    assert (
        inst.case.application[0].type.coding[0].system
        == ExternalValidatorModel(
            valueUri="http://ema.europa.eu/example/marketingAuthorizationApplicationType"
        ).valueUri
    )
    assert (
        inst.case.application[1].dateDateTime
        == ExternalValidatorModel(valueDateTime="2014-09-01").valueDateTime
    )
    assert (
        inst.case.application[1].identifier.system
        == ExternalValidatorModel(
            valueUri="http://ema.europa.eu/example/applicationidentifier-number"
        ).valueUri
    )
    assert inst.case.application[1].identifier.value == "IA38F"
    assert (
        inst.case.application[1].type.coding[0].code
        == "GroupTypeIAVariationNotification"
    )
    assert (
        inst.case.application[1].type.coding[0].system
        == ExternalValidatorModel(
            valueUri="http://ema.europa.eu/example/marketingAuthorizationApplicationType"
        ).valueUri
    )
    assert (
        inst.case.datePeriod.end
        == ExternalValidatorModel(valueDateTime="2015-08-21").valueDateTime
    )
    assert (
        inst.case.datePeriod.start
        == ExternalValidatorModel(valueDateTime="2014-09-02").valueDateTime
    )
    assert (
        inst.case.identifier.system
        == ExternalValidatorModel(
            valueUri="http://ema.europa.eu/example/procedureidentifier-number"
        ).valueUri
    )
    assert inst.case.identifier.value == "EMEA/H/C/009999/IA/0099/G"
    assert inst.case.type.coding[0].code == "VariationTypeIA"
    assert (
        inst.case.type.coding[0].system
        == ExternalValidatorModel(
            valueUri="http://ema.europa.eu/example/marketingAuthorizationProcedureType"
        ).valueUri
    )
    assert inst.holder.reference == "Organization/example"
    assert inst.id == "example"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel(
            valueUri="http://ema.europa.eu/example/marketingAuthorizationNumber"
        ).valueUri
    )
    assert inst.identifier[0].value == "EU/1/11/999/001"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.region[0].coding[0].code == "EU"
    assert (
        inst.region[0].coding[0].system
        == ExternalValidatorModel(
            valueUri="http://ema.europa.eu/example/country"
        ).valueUri
    )
    assert inst.regulator.reference == "Organization/example"
    assert inst.status.coding[0].code == "active"
    assert (
        inst.status.coding[0].system
        == ExternalValidatorModel(
            valueUri="http://ema.europa.eu/example/authorizationstatus"
        ).valueUri
    )
    assert (
        inst.statusDate
        == ExternalValidatorModel(valueDateTime="2015-01-14").valueDateTime
    )
    assert inst.text.status == "generated"
    assert (
        inst.validityPeriod.end
        == ExternalValidatorModel(valueDateTime="2020-05-20").valueDateTime
    )
    assert (
        inst.validityPeriod.start
        == ExternalValidatorModel(valueDateTime="2014-09-03").valueDateTime
    )


def test_regulatedauthorization_2(base_settings):
    """No. 2 tests collection for RegulatedAuthorization.
    Test File: regulatedauthorization-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "regulatedauthorization-example.json"
    )
    inst = regulatedauthorization.RegulatedAuthorization.model_validate_json(
        Path(filename).read_bytes()
    )
    assert "RegulatedAuthorization" == inst.get_resource_type()

    impl_regulatedauthorization_2(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "RegulatedAuthorization" == data["resourceType"]

    inst2 = regulatedauthorization.RegulatedAuthorization(**data)
    impl_regulatedauthorization_2(inst2)
