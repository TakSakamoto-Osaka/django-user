from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied

class PaidUserView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    # raise_exception = False
    # login_url = reverse_lazy('login')
    
    template_name = "paid_user.html"

    def test_func(self):
        return self.request.user.is_paid_member == True
    
    def handle_no_permission(self):
        if self.request.user.is_authenticated == False:
            print('未ログイン')
            return redirect('login')
        else:
            print('非有料ユーザー')
            return redirect('top')
    