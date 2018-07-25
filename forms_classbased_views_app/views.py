
from django.utils.timezone import now
from django.views.generic import FormView,TemplateView
from .forms import ContactForm

from django.core.urlresolvers import reverse_lazy
#from django.core.urlresolvers import reverse_lazy

class AboutUsView(TemplateView):
    template_name = 'about_us.html'

def get_context_data(self, **kwargs):
    context = super(AboutUsView, self).get_context_data(**kwargs)
    if now().weekday() < 5 and 8 < now().hour < 18:
        context['open'] = True
    else:
        context['open'] = False
    return context

class ContactView(FormView):
    form_class = ContactForm
    success_url = reverse_lazy('contact')
    template_name = 'contact.html'

    def form_valid(self, form):
        contact_name = self.form.cleaned_data['contact_name']
        contact_email = self.form.cleaned_data['contact_email']
        form_content = self.form.cleaned_data['content']
        template = get_template('contact_template.txt')
        context = Context({
            'contact_name': contact_name,
            'contact_email': contact_email,
            'form_content': form_content
            })
        content = template.render(context)

        email = EmailMessage(
            'New contact form submission',
            content,
            'Your website ' + '',
            ['youremail@gmail.com'],
            headers = {'Reply-To': contact_email}
        )
        email.send()
	return super(ContactView, self).form_valid(form)