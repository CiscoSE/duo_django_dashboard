from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.conf import settings

from duo_app import duo_auth


@login_required
@duo_auth.duo_auth_required
def duo_private(request):
    """
    View which requires a login and Duo authentication.
    """
    return HttpResponse(
        '<form action="http://127.0.0.1:8000/private"><input type="submit" value="Dashboard" /></form>'
        '<form action="http://127.0.0.1:8000/accounts/duo_logout"><input type="submit" value="Exit DB Configuration" /></form>'
        '<img src="/static/adminMongo_searchdocuments.png">'
        '<p>Dashboard Configuration'
    )


@login_required
def duo_private_manual(request):
    """
    View which requires a login, and manually checks for Duo authentication.
    """
    if not duo_auth.duo_authenticated(request):
        return HttpResponseRedirect(
            '%s?next=%s' % (settings.DUO_LOGIN_URL, request.path))
    return HttpResponse(
        '<form action="http://127.0.0.1:8000/private"><input type="submit" value="Dashboard" /></form>'
        '<form action="http://127.0.0.1:8000/accounts/duo_logout"><input type="submit" value="Exit DB Configuration" /></form>'
        '<img src="/static/adminMongo_searchdocuments.png">'
    )


@login_required
def private(request):
    """
    View which requires a login.
    """
    return HttpResponse(
        '<form action="http://127.0.0.1:8000/duo_private"><input type="submit" value="DB Configuration" /></form>'
        '<form action="http://127.0.0.1:8000/accounts/logout"><input type="submit" value="Logout" /></form>'
        '<img src="/static/ee-dashboard.png">'
    )


def public(request):
    """
    Public view.
    """
    return HttpResponse('Public content.')


def profile(request):
    """
    View for all Django profiles.
    """
    return HttpResponse('Profile view.')
