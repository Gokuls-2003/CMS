from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from .import models


class ClassRoomFilter(admin.SimpleListFilter):

    title = "Class Room"

    parameter_name = "class_room"

    def lookups(self, request: Any, model_admin: Any) -> list[tuple[Any, str]]:
        data = []
        for class_room in models.Classroom.objects.all():
            data.append((class_room.name, class_room.name))
        return data

    def queryset(self, request: Any, queryset: QuerySet[Any]) -> QuerySet[Any] | None:
        if self.value() is None:
            return queryset
        return queryset.filter(class_room__name=self.value())


class DayFilter(admin.SimpleListFilter):

    title = "Days"

    parameter_name = "days"

    def lookups(self, request: Any, model_admin: Any) -> list[tuple[Any, str]]:
        return [
            ('Monday', 'Monday'),
            ('Tuesday', 'Tuesday'),
            ('Wednesday', 'Wednesday'),
            ('Thursday', 'Thursday'),
            ('Friday', 'Friday')
        ]

    def queryset(self, request: Any, queryset: QuerySet[Any]) -> QuerySet[Any] | None:
        if self.value() is None:
            return queryset
        return queryset.filter(day=self.value())
