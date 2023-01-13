from rest_framework import permissions


class IsOwnerOrStaff(permissions.BasePermission):

    def has_object_permission(self, request, view, obj): #isteği atan profil sahibi yada staff ise izin ver, burada her bir obj profile instance'ı temsil ediyor
        return bool(request.user.is_staff or (obj.user == request.user)) 