import django_filters

# A filter that uses starts with as the default lookup expression

class StartsWithCharFilter(django_filters.CharFilter):

    def __init__(self, *args, **kwargs):
        super(StartsWithCharFilter, self).__init__(*args, **kwargs)
        self.lookup_expr = 'startswith'
