from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from registration.backends.simple import SimpleBackend
from registration.models import RegistrationProfile
from registration import signals


class RestBackend(SimpleBackend):
    def register(self, request, **kwargs):
        """
        Create and immediately log in a new user.

        """
        username, email, password = kwargs['username'], kwargs['email'], kwargs['password1']
        new_user = User.objects.create_user(username, email, password)
        new_user.user_type = kwargs['username']

        # authenticate() always has to be called before login(), and
        # will return the user we just created.
        new_user = authenticate(username=username, password=password)
        login(request, new_user)
        signals.user_registered.send(sender=self.__class__,
                                     user=new_user,
                                     request=request)
        return new_user

    def activate(self, request, activation_key):
        """
        Given an an activation key, look up and activate the user
        account corresponding to that key (if possible).

        After successful activation, the signal
        ``registration.signals.user_activated`` will be sent, with the
        newly activated ``User`` as the keyword argument ``user`` and
        the class of this backend as the sender.

        """
        activated = RegistrationProfile.objects.activate_user(activation_key)
        if activated:
            activated.is_email_active = True
            signals.user_activated.send(sender=self.__class__,
                                        user=activated,
                                        request=request)
        return activated
