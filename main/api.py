__author__ = 'ir4y'


class ResourceTypesOverrideMixin(object):
    """
    This class override default type of resource item
    it use types_override dict in Meta section

    Example of usage:
    class RegistrationResource(ResourceTypesOverrideMixin, Resource):
        user_type = fields.CharField(attribute='user_type')
        company_name = fields.CharField(attribute='company_name')
        first_name = fields.CharField(attribute='first_name')
        last_name = fields.CharField(attribute='last_name')
        email_address = fields.CharField(attribute='email_address')
        phone_number = fields.CharField(attribute='phone_number')
        password = fields.CharField(attribute='password')
        re_password = fields.CharField(attribute='re_password')

        class Meta:
            types_override = {
                'user_type': 'hidden',
                'password': 'password',
                're_password': 'password',
                'email_address': 'email',
                'phone_number': 'phone',
            }
    """
    def build_schema(self):
        data = super(ResourceTypesOverrideMixin, self).build_schema()
        if hasattr(self._meta, 'types_override'):
            for field_name, field_data in data['fields'].iteritems():
                if field_name in self._meta.types_override:
                    field_data['type'] = self._meta.types_override[field_name]
        return data