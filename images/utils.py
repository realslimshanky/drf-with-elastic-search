from typing import Any, Dict


def get_query_type_from_lookup_expr(lookup_expr: str) -> str:
    if lookup_expr == "exact":
        return "term"
    if ("__gte" in lookup_expr) or ("__lte" in lookup_expr):
        return "range"
    return "term"


def get_query_args_from_filter(filter_name: str, filter_value: Any) -> Dict[str, Any]:
    if "__gte" in filter_name:
        return {filter_name.strip("__gte"): {"gte": filter_value}}
    if "__lte" in filter_name:
        return {filter_name.strip("__lte"): {"lte": filter_value}}
    if "__min" in filter_name:
        return {filter_name.strip("__min"): {"gte": filter_value}}
    if "__max" in filter_name:
        return {filter_name.strip("__max"): {"lte": filter_value}}
    else:
        return {filter_name: filter_value}
