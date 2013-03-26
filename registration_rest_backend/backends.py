from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.sites.models import RequestSite
from django.contrib.sites.models import Site
from registration.backends.simple import SimpleBackend
from registration.models import RegistrationProfile
from registration import signals
from tasks import send_activation_email


class RestBackend(SimpleBackend):
    def register(self, request, **kwargs):
        """
        Create and immediately log in a new user.
        Send email activation message

        """
        username = kwargs.pop('username')
        email = kwargs.pop('email')
        password = kwargs.pop('password')
        new_user = User.objects.create_user(username, email, password, **kwargs)
        registration_profile = RegistrationProfile.objects.create_profile(new_user)
        if Site._meta.installed:
            site = Site.objects.get_current()
        else:
            site = RequestSite(request)
        send_activation_email.delay(registration_profile, site)

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
            activated.save()
            signals.user_activated.send(sender=self.__class__,
                                        user=activated,
                                        request=request)
        return activated
