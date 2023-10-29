from django import forms

from conversations.models import ConversationsMessage

class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConversationsMessage
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            })
        }