from django.db.models import Q


def generate_query_argument_description(search_fields):
    header = "Supported filter parameters:\n"
    supported_list = ""
    for field in search_fields:
        supported_list += "* {0}\n".format(field)
    return header + supported_list


def filter_by_query_param(queryset, query, search_fields):
    """Filter queryset according to given parameters.

    Keyword arguments:
    queryset - queryset to be filtered
    query - search string
    search_fields - fields considered in filtering
    """
    if query:
        query_by = {
            "{0}__{1}".format(field, "icontains"): query for field in search_fields
        }
        query_objects = Q()
        for q in query_by:
            query_objects |= Q(**{q: query_by[q]})
        return queryset.filter(query_objects).distinct()
    return queryset
