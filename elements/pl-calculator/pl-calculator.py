import random
from enum import Enum

import chevron
import lxml.html
import prairielearn as pl
from typing_extensions import assert_never

CALCULATOR_MUSTACHE_TEMPLATE_NAME = "pl-calculator.mustache"
CALCULATOR_NAME_DEFAULT = "pl-calculator"


def prepare(element_html: str, data: pl.QuestionData) -> None:
    element = lxml.html.fragment_fromstring(element_html)

    optional_attribs = ["calculator-name"]
    pl.check_attribs(element, required_attribs=[], optional_attribs=optional_attribs)
    calculator_name = pl.get_string_attrib(
        element, "calculator-name", CALCULATOR_NAME_DEFAULT
    )
    uuid = pl.get_uuid()
    if calculator_name in data["params"]:
        if calculator_name == CALCULATOR_NAME_DEFAULT:
            raise ValueError(
                "When using more than one calculator element you must specify a unique 'calculator-name' attribute for each of them."
            )
        else:
            raise ValueError(
                f"Multiple calculator elements are using calculator-name='{calculator_name}'. These must have unique names."
            )

    data["params"][calculator_name] = uuid


def render(element_html: str, data: pl.QuestionData) -> str:
    if data["panel"] != "question":
        return ""

    element = lxml.html.fragment_fromstring(element_html)

    required_attribs = ["calculator-name"]
    pl.check_attribs(element, required_attribs=required_attribs, optional_attribs=[])
    calculator_name = pl.get_string_attrib(element, "calculator-name")

    html_params = {
        "question": True,
        "uuid": data["params"][calculator_name],
    }
    with open(CALCULATOR_MUSTACHE_TEMPLATE_NAME, "r", encoding="utf-8") as f:
        template = f.read()
    return chevron.render(template, html_params).strip()
