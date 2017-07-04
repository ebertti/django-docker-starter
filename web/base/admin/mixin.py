

class BaseAdminMixin():

    lookup_aberto = True

    def lookup_allowed(self, lookup, value):
        if self.lookup_aberto:
            return True
        return super().lookup_allowed(lookup, value)

    pass