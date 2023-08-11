from rest_framework import permissions


class IsSuperUserIsAdminIsModeratorIsAuthor(permissions.BasePermission):
    """
    Разрешает анониму только безопасные запросы.
    Доступ к запросам PATCH и DELETE предоставляется только
    суперюзеру Джанго, админу Джанго, аутентифицированным пользователям
    с ролью admin или moderator, а также автору объекта.
    """

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
            and (request.user.is_superuser
                 or request.user.is_staff
                 or request.user.is_admin
                 or request.user.is_moderator
                 or request.user == obj.author))


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and (
            request.user.role == 'admin' or request.user.is_superuser)


class IsSuperUserOrIsAdminOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == 'Get':
            return True
        return (
            request.user.is_authenticated
            and (request.user.is_superuser or request.user.role == 'admin')
        )
    

class IsModerator(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'moderator'


class IsUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'user'
