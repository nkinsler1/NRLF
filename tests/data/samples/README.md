# Supplier sample data

This directory contains sample pointer data from our suppliers. Samples have
been sourced directly from suppliers or anonymised from live data.

To add a new sample to this folder, follow these steps:

- Remove any real PII from the DocumentReference data (NHS numbers, URLs, ids etc)
- Add the DocumentReference data to a .json file with a name describing the
  supplier and the pointer type, something like <ODSCode>_<PointerType>_<other-unique-info>.json
- Run the tests to verify that the pointer works with our model and validators
