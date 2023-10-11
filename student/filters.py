from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.db.models import ExpressionWrapper, fields, Sum
from django.db.models import Q


class PaidStatus(admin.SimpleListFilter):

    title = "Paid Status"

    parameter_name = "paid"

    def lookups(self, request: Any, model_admin: Any) -> list[tuple[Any, str]]:
        return [
            ('paid', 'paid'),
            ('unpaid', 'unpaid')
        ]

    def queryset(self, request: Any, queryset: QuerySet[Any]) -> QuerySet[Any] | None:
        if self.value() is None:
            return queryset
        queryset = queryset.annotate(
            pending_fees=ExpressionWrapper(
                Sum('invoices__total_amount') - Sum('transactions__amount'),
                output_field=fields.DecimalField()
            )
        )
        if self.value() == "paid":
            return queryset.filter(Q(pending_fees=0) | Q(pending_fees=None))
        if self.value() == "unpaid":
            return queryset.filter(pending_fees__gt=0)
