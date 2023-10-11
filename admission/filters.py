from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet


class TenthMarkFilter(admin.SimpleListFilter):

    title = "10th Mark"

    parameter_name = "tenth_mark"

    def lookups(self, request: Any, model_admin: Any) -> list[tuple[Any, str]]:
        return [
            ('300', ">300"),
            ('350', ">350"),
            ('400', ">400"),
            ('450', ">450")
        ]

    def queryset(self, request: Any, queryset: QuerySet[Any]) -> QuerySet[Any] | None:
        if self.value() is None:
            return queryset
        return queryset.filter(tenth_mark__gte=int(self.value()))


class TwelvethMarkFilter(admin.SimpleListFilter):

    title = "12th Mark"

    parameter_name = "twelveth_mark"

    def lookups(self, request: Any, model_admin: Any) -> list[tuple[Any, str]]:
        return [
            ('300', ">300"),
            ('350', ">350"),
            ('400', ">400"),
            ('450', ">450"),
            ('500', ">500"),
            ('550', ">550"),
        ]

    def queryset(self, request: Any, queryset: QuerySet[Any]) -> QuerySet[Any] | None:
        if self.value() is None:
            return queryset
        return queryset.filter(twelveth_mark__gte=int(self.value()))
