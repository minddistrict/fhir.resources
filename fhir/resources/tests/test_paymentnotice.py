# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/PaymentNotice
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from pathlib import Path

from .. import paymentnotice
from .fixtures import ExternalValidatorModel, bytes_validator  # noqa: F401


def impl_paymentnotice_1(inst):
    assert inst.amount.currency == "USD"
    assert float(inst.amount.value) == float(12500.0)
    assert (
        inst.created == ExternalValidatorModel(valueDateTime="2014-08-16").valueDateTime
    )
    assert inst.id == "77654"
    assert (
        inst.identifier[0].system
        == ExternalValidatorModel(
            valueUri="http://benefitsinc.com/paymentnotice"
        ).valueUri
    )
    assert inst.identifier[0].value == "776543"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/v3-ActReason"
        ).valueUri
    )
    assert inst.payee.reference == "Organization/1"
    assert inst.payment.reference == "PaymentReconciliation/ER2500"
    assert inst.paymentDate == ExternalValidatorModel(valueDate="2014-08-15").valueDate
    assert inst.paymentStatus.coding[0].code == "paid"
    assert (
        inst.paymentStatus.coding[0].system
        == ExternalValidatorModel(
            valueUri="http://terminology.hl7.org/CodeSystem/paymentstatus"
        ).valueUri
    )
    assert (
        inst.recipient.identifier.system
        == ExternalValidatorModel(valueUri="http://regulators.gov").valueUri
    )
    assert inst.recipient.identifier.value == "AB123"
    assert inst.reporter.reference == "Organization/1"
    assert inst.request.reference == "http://benefitsinc.com/fhir/claim/12345"
    assert (
        inst.response.reference == "http://benefitsinc.com/fhir/claimresponse/CR12345"
    )
    assert inst.status == "active"
    assert inst.text.div == (
        '<div xmlns="http://www.w3.org/1999/xhtml">A human-readable'
        " rendering of the PaymentNotice</div>"
    )
    assert inst.text.status == "generated"


def test_paymentnotice_1(base_settings):
    """No. 1 tests collection for PaymentNotice.
    Test File: paymentnotice-example.json
    """
    filename = base_settings["unittest_data_dir"] / "paymentnotice-example.json"
    inst = paymentnotice.PaymentNotice.model_validate_json(Path(filename).read_bytes())
    assert "PaymentNotice" == inst.get_resource_type()

    impl_paymentnotice_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.model_dump()
    assert "PaymentNotice" == data["resourceType"]

    inst2 = paymentnotice.PaymentNotice(**data)
    impl_paymentnotice_1(inst2)
