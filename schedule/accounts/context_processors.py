from .models import SystemUser 

def menu_context(request):
    if request.user.is_authenticated:
        try:
            systemuser = SystemUser.objects.get(pk=request.user.id)
        except SystemUser.DoesNotExist:
            systemuser = None
    else:
        systemuser = None
    
    return {'logged_user': systemuser}
