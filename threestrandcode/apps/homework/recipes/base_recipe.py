import abc

from ..models import Assignment


class BaseRecipe(object):
    """This is the base class for recipes to extend off of.

    Each recipe should have a way to get missing pre requisites"""

    __metaclass__ = abc.ABCMeta

    @classmethod
    def get_name(cls):
        name = cls.__name__
        module = cls.__module__.split('.')[-1]
        return "%s.%s" % (module, name)

    @abc.abstractproperty
    def description(self):
        raise NotImplementedError()

    @classmethod
    def _check_user_completed(cls, user):
        try:
            return Assignment.objects.get(recipe__module=cls.get_name(), completed=True)
        except Assignment.DoesNotExist:
            return False

    @classmethod
    def _get_recursive_pre_reqs(cls):
        if hasattr(cls, "pre_reqs"):
            yield from cls.pre_reqs
            for k in cls.pre_reqs:
                yield from k._get_recursive_pre_reqs()

    @classmethod
    def get_missing_pre_reqs(cls, user):
        """Returns a list of missing pre reqs OR a message describing the problem"""
        if hasattr(cls, "pre_reqs"):
            pre_reqs = list(cls._get_recursive_pre_reqs())  # coerce to list to force generator to process
            missing_pre_reqs = list(filter(lambda x: not x._check_user_completed(user), pre_reqs))
        else:
            missing_pre_reqs = []
        return missing_pre_reqs

    @abc.abstractmethod
    def do_completed_check(self, user):
        raise NotImplementedError()
