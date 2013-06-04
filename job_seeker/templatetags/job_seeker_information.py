from django import template
from main.utils import get_model_values, any_not_None


__author__ = 'ir4y'


register = template.Library()




@register.filter()
def section1_complete(user):
    return any_not_None([user.first_name, user.last_name] +
                        get_model_values(user.profile.personal_information, ('id', 'photo',)))


@register.filter()
def section2_complete(user):
    return any_not_None(get_model_values(user.profile.current_employment))


@register.filter()
def section3_complete(user):
    return any(map(lambda u: any_not_None(get_model_values(u)),
                   user.profile.previous_employments_set.all()))


@register.filter()
def section4_complete(user):
    return any(map(lambda u: any_not_None(get_model_values(u)),
                   user.profile.educations_set.all()))


@register.filter()
def section5_complete(user):
    return any(map(lambda u: any_not_None(get_model_values(u, ('id', 'is_for_interview', 'phone_number'))),
                   user.profile.referees_set.all()))

