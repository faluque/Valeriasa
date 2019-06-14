from django.shortcuts import render, redirect
from .models import usuarios, ctacte
from django.http.response import HttpResponseRedirect
from .forms import CustomUserChangeForm, CustomUserCreationForm, CuentaCorrienteForm
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import DeleteView, DetailView, View, CreateView, TemplateView, UpdateView, FormView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm, AdminPasswordChangeForm


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

    def form_valid(self, form):
            usr_obj= form.save(commit=False)
            if usr_obj.tipoUsr=='I':
                usr_obj.nro_inquilino= usr_obj.id
            usr_obj.save()
            return HttpResponseRedirect(reverse('home'))

    def get_success_url(self):
        return reverse('home')


class UserUpdateView(UpdateView):
    form_class= CustomUserChangeForm
    template_name='userUD.html'
    success_url='/'
    model=usuarios

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(UserUpdateView, self).dispatch(request, *args, **kwargs)



class SetPasswordView(FormView):

    form_class = AdminPasswordChangeForm
    template_name = 'change-password.html'
    success_url = 'home'

    def get_form_kwargs(self):
        kwargs = super(set, self).get_form_kwargs()
        kwargs['user_to_update'] = user
        return kwargs

    def form_valid(self, form):
        form.save()
        return super(SetPasswordView, self).form_valid(form)

class UserDeleteView(DeleteView):
    model= usuarios
    template_name='confirmacion.html'
    success_url= reverse_lazy('home')

class CtaCteMenuView(TemplateView):
    template_name='menu_ctacte.html'
    
    def get_context_data(self, **kwargs):
        ctd = super(CtaCteMenuView, self).get_context_data(**kwargs)
        
        if self.request.user.is_authenticated():  
            ctd['ctactes']=ctacte.objects.all().order_by('-fecha')
        
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
    template_name='confirmacion-ctacte.html'
    success_url= reverse_lazy('home')

class ConsultaDeudasView(TemplateView):
    template_name='consulta_deudas.html'

    @method_decorator(login_required)
    def dispatch(self, request, *arg, **kwargs):
        return super(ConsultaDeudasView, self).dispatch(request, *arg, **kwargs)

    def get_context_data(self, **kwargs):
        cdt = super(ConsultaDeudasView, self).get_context_data(**kwargs)
        
        if self.request.user.is_authenticated():
            cdt['deudas']=ctacte.objects.filter(nro_inquilino=self.request.user.nro_inquilino).exclude(saldo__exact="0.00").order_by('-fecha')
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
            cot['ultimos']=ctacte.objects.filter(nro_inquilino=self.request.user.nro_inquilino).filter(fecha__gte=tresMeses).order_by('-fecha')
        return cot
