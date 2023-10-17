from marshmallow.exceptions import ValidationError, MarshmallowError
from marshmallow import fields
import inspect


class DjangoModelID(fields.Raw):
    """
    This field is used to represent a Django Model Instance solely as it's PK

    :param queryset: Either a queryset instance or a model class. If a model class
        is specified, the queryset used will be model.objects.all()
    :param model:  For legacy reasons, we allow model to be specified as a kwarg,
        if this is specified, you cannot specify a queryset, and queryset will be
        model.objects.all()
    :param ignore_invalid: Setting this to true will deserialize this field to None in the case
        the coresponding model can't be found, rather than raising a validation error.
    """
    def __init__(self, queryset=None, model=None, ignore_invalid=False, deserialize_to_integer=False, **kwargs):
        self.ignore_invalid = ignore_invalid
        self.deserialize_to_integer = deserialize_to_integer
        if queryset is not None and model is not None:
            raise ValueError('Cannot specify both queryset and model')
        elif queryset is None and model is None:
            raise ValueError('Must specify either queryset or model')

        # the queryset arg can be either a Model class or a queryset instance
        # allows simpler syntax i.e. DjangoModelID(Unit) or DjangoModelID(Unit.objects.all())
        if inspect.isclass(queryset) and issubclass(queryset, models.Model):
            # queryset arg is a model class
            model = queryset

        if model is not None:
            self.queryset = model.objects.all()
        else:
            self.queryset = queryset
        super(DjangoModelID, self).__init__(**kwargs)

    def lookup(self, value):
        """Do the lookup on the queryset. If this raises a DoesNotExist, a validation error will be returned.
        Override this in a subclass to customize how the lookup is done."""
        return self.queryset.get(pk=value)

    def serialize_model(self, value):
        """Override this in a subclass to customize how we serialize the model"""
        if isinstance(value, int):
            return value
        if isinstance(value, dict):
            return value.get('id', None)
        return getattr(value, 'pk')


    def _deserialize(self, value, attrs, obj):
        if self.deserialize_to_integer and isinstance(value, int):
            return value

        if isinstance(value, self.queryset.model):
            return value

        try:
            return self.lookup(value)
        except self.queryset.model.DoesNotExist:
            if self.ignore_invalid:
                return None
            raise ValidationError('Invalid choice.')

    def _serialize(self, value, attrs, obj):
        if value is None:
            return None
        return self.serialize_model(value)
