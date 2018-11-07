from django import forms

from django.core.mail import EmailMessage

class ContatoForm(forms.Form):

    email = forms.EmailField()
    nome = forms.CharField()
    #assunto = forms.
    mensagem = forms.CharField()

    def is_valid(self):
        valido = super(ContatoForm, self).is_valid()
        if valido:
            self.enviar_email()
        return valido


    def enviar_email(self):
        print("Nome: "+self.cleaned_data["nome"])
        print("E-mail: "+self.cleaned_data["email"])
        print("Mensagem:")
        print(self.cleaned_data["mensagem"])
        #send_mail()

class LoginForm(forms.Form):
    login = forms.CharField()
    senha = forms.CharField()

    def is_valid(self):
        valido = super(LoginForm, self).is_valid()
        if valido:
            self.enviar_email()
        return valido

    def enviar_email(self):
        print("Login: "+self.cleaned_data["login"])
        print("Senha: "+self.cleaned_data["senha"])
        #send_mail()
