from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label="What's your name",
        widget=forms.TextInput(attrs={"placeholder": "What's Your Name..."}),
    )

    email = forms.EmailField(
        label="Your Email",
        widget=forms.EmailInput(attrs={"placeholder": "Your Email..."}),
    )

    message = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "Type Your Message Here..."}),
    )


class NewsletterForm(forms.Form):
    email = forms.EmailField(
        label="Enter your email",
        widget=forms.EmailInput(attrs={"placeholder": "ENTER YOUR EMAIL"}),
    )
