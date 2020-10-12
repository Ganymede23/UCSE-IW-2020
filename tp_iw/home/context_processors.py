from usuario.models import Profile
def agregar_usuarios_no_seguidos(request):
    usuarios_no_seguidos=[]
    if request.user.is_authenticated:
        profile = Profile.objects.get(pk=request.user.id)
        usuarios =  Profile.objects.all().exclude(user=request.user)
        for usuario in usuarios:
            if not profile.following.filter(id=usuario.id).exists():
                usuarios_no_seguidos.append(usuario)
        return {
            'usuarios_no_seguidos': usuarios_no_seguidos,
        }
    return {
            'usuarios_no_seguidos': '',
        }