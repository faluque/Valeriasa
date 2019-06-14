from django.shortcuts import render
from .models import usuarios, ctacte
from django.http.response import HttpResponseRedirect
from .forms import CustomUserChangeForm, CustomUserCreationForm, CuentaCorrienteForm
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import DeleteView, DetailView, View, CreateView, TemplateView, UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta

class HomeView(TemplateView):
    template_name='home.html'

    def get_context_data(self, **kwargs):
        ctx = super(HomeView, self).get_context_data(**kwargs)
        
        if self.request.user.is_authenticated():
            if self.request.user.tipoUsr=='I':
                ctx['es_cliente']=True

        return ctx

class UserMenuView(TemplateView):
    template_name='menu_usr.html'
    
    def get_context_data(self, **kwargs):
        con = super(UserMenuView, self).get_context_data(**kwargs)
        
        if self.request.user.is_authenticated():  
            con['usuarios']=usuarios.objects.filter(tipoUsr='I')
        
        return con

class UserRegistrationView(CreateView):
    form_class= CustomUserCreationForm
    template_name='user.html'

    def get_success_url(self):
        return reverse('home')

class UserUpdateView(UpdateView):
    form_class= CustomUserChangeForm
    template_name='user.html'
    success_url='/'
    model=usuarios

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(UserUpdateView, self).dispatch(request, *args, **kwargs)

class UserDeleteView(DeleteView):
    model= usuarios
    template_name='confirmacion.html'
    success_url= reverse_lazy('menu_usr')
class CtaCteMenuView(TemplateView):
    template_name='menu_ctacte.html'
    
    def get_context_data(self, **kwargs):
        ctd = super(CtaCteMenuView, self).get_context_data(**kwargs)
        
        if self.request.user.is_authenticated():  
            ctd['ctactes']=ctacte.objects.all()
        
        return ctd


class NewCuentaCorrienteView(CreateView):
        form_class = CuentaCorrienteForm
        template_name = 'cuenta_corriente.html'
        
        def form_valid(self, form):
            ctacte_obj= form.save(commit=False)
            ctacte_obj.saldo= ctacte_obj.importe
            ctacte_obj.save()
            return HttpResponseRedirect(reverse('home'))

        @method_decorator(login_required)
        def dispatch(self, request, *args, **kwargs):
            return super(NewCuentaCorrienteView, self).dispatch(request, *args,**kwargs)
 

class CtaCteUpdateView(UpdateView):
    form_class= CuentaCorrienteForm
    template_name='cuenta_corriente.html'
    success_url='/'
    model=ctacte

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(CtaCteUpdateView, self).dispatch(request, *args, **kwargs)

class CtaCteDetailsView(DetailView):
    model= ctacte
    template_name= 'detalle_ctacte.html'

class CtaCteDeleteView(DeleteView):
    model= ctacte
    template_name='confirmacion.html'
    success_url= reverse_lazy('menu_ctacte')

class ConsultaDeudasView(TemplateView):
    template_name='consulta_deudas.html'

    @method_decorator(login_required)
    def dispatch(self, request, *arg, **kwargs):
        return super(ConsultaDeudasView, self).dispatch(request, *arg, **kwargs)

    def get_context_data(self, **kwargs):
        cdt = super(ConsultaDeudasView, self).get_context_data(**kwargs)
        
        if self.request.user.is_authenticated():
            cdt['deudas']=ctacte.objects.filter(inquilino=self.request.user).filter(saldo__gt=0)
        return cdt

class ConsultaUltimosMovView(TemplateView):
    template_name='consulta_ultimos.html'

    @method_decorator(login_required)
    def dispatch(self, request, *arg, **kwargs):
        return super(ConsultaUltimosMovView, self).dispatch(request, *arg, **kwargs)

    def get_context_data(self, **kwargs):
        cot = super(ConsultaUltimosMovView, self).get_context_data(**kwargs)
        
        tresMeses= datetime.today()- timedelta(days=90)
        if self.request.user.is_authenticated():
            cot['ultimos']=ctacte.objects.filter(inquilino=self.request.user).filter(fecha__gte=tresMeses)
        return cot
