from typing import List, Optional

from pydantic import ValidationError
from pydantic_core import ErrorDetails

from nrlf.core.response import Response
from nrlf.core.types import CodeableConcept
from nrlf.producer.fhir.r4 import model as producer_model
from nrlf.producer.fhir.r4.model import OperationOutcome, OperationOutcomeIssue


def diag_for_error(error: ErrorDetails) -> str:
    if error["loc"]:
        loc_string = ".".join(str(each) for each in error["loc"])
        return f"{loc_string}: {error['msg']}"
    else:
        return f"root: {error['msg']}"


def expression_for_error(error: ErrorDetails) -> Optional[str]:
    return str(".".join(str(each) for each in error["loc"]) if error["loc"] else "root")


class OperationOutcomeError(Exception):
    """
    Will instantly trigger an OperationOutcome error response when raised
    """

    def __init__(  # noqa: PLR0913
        self,
        severity: str,
        code: str,
        details: CodeableConcept,
        diagnostics: Optional[str] = None,
        expression: Optional[list[str]] = None,
        status_code: str = "400",
    ):
        self.operation_outcome = OperationOutcome(
            resourceType="OperationOutcome",
            issue=[
                OperationOutcomeIssue(
                    severity=severity,
                    code=code,
                    details=details,  # type: ignore
                    diagnostics=diagnostics,
                    expression=expression,
                )
            ],
        )
        self.status_code = status_code

    @property
    def response(self) -> Response:
        return Response(
            statusCode=self.status_code,
            body=self.operation_outcome.model_dump_json(exclude_none=True, indent=2),
        )


class ParseError(Exception):
    issues: List[OperationOutcomeIssue]

    def __init__(self, issues: List[OperationOutcomeIssue]):
        self.issues = issues

    @classmethod
    def from_validation_error(
        cls, exc: ValidationError, details: CodeableConcept, msg: str = ""
    ):
        issues = [
            producer_model.OperationOutcomeIssue(
                severity="error",
                code="invalid",
                details=details,  # type: ignore
                diagnostics=f"{msg} ({diag_for_error(error)})",
                expression=[expression_for_error(error)],  # type: ignore
            )
            for error in exc.errors()
        ]

        return cls(issues)

    @property
    def response(self):
        return Response(
            statusCode="400",
            body=producer_model.OperationOutcome(
                resourceType="OperationOutcome",
                issue=self.issues,
            ).model_dump_json(exclude_none=True, indent=2),
        )
