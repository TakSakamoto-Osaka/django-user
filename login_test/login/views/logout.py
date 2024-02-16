from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin


class LogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'top.html'
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context
     