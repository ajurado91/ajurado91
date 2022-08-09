from cerberus import Validator


class SchemaValidator:
    def __init__(self, schema_expected, required_all):
        self.schema_expected = schema_expected
        self.required_all = required_all
        self.validator = Validator(schema_expected, required_all=self.required_all)

    def validate(self, response_dict):
        return self.validator.validate(response_dict)
