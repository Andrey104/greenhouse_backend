from django.db.models import Q
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404


def get_object_data(model, object_id, request, validate):
    obj = get_object_or_404(model, pk=object_id)
    validate(obj)
    data = request.data
    return obj, data


def validate_request(data, *args):
    errors = {}
    msg = 'This field is required'
    for item in args:
        if data.get(item) is None:
            errors[item] = msg

    if errors:
        raise ValidationError(errors)


def create_object(serializer, data, **kwargs):
    request = kwargs.pop('request', None)
    obj = serializer(data=data, context={'request': request})
    obj.is_valid(raise_exception=True)
    obj.save(**kwargs)
    return obj


def add_action(serializer, action_type, data, **kwargs):
    data['type'] = action_type
    return create_object(serializer, data, **kwargs)


def filter_by_status(request):
    q = Q()
    statuses = request.GET.getlist('status')
    if statuses is not None:
        for status in statuses:
            q |= Q(status=status)
    return q


def paginate(paginator, serializer, queryset, request):
    paginator = paginator()
    context = paginator.paginate_queryset(queryset, request)
    serializer = serializer(context, many=True, context={'request': request})
    return paginator.get_paginated_response(serializer.data)


def validate_date(date):
    for char in date:
        if not char.isdigit() and not char == '-':
            return False
    return True