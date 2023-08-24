# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime
from ...commons.types.observation_level import ObservationLevel


class UpdateSpanRequest(pydantic.BaseModel):
    span_id: str = pydantic.Field(alias="spanId")
    trace_id: typing.Optional[str] = pydantic.Field(alias="traceId")
    end_time: typing.Optional[dt.datetime] = pydantic.Field(alias="endTime")
    name: typing.Optional[str]
    metadata: typing.Optional[typing.Any]
    input: typing.Optional[typing.Any]
    output: typing.Optional[typing.Any]
    level: typing.Optional[ObservationLevel]
    version: typing.Optional[str]
    status_message: typing.Optional[str] = pydantic.Field(alias="statusMessage")

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}
