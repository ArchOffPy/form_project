from django import forms

class FeedbackForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=10, min_length=2, error_messages={
        'max_length': 'Слишком дофига символов',
        'min_length': 'Слишком мало символов',
        'required': 'Слушай, поле нужно заполнить',
    })
    surname = forms.CharField(label='Фамилия', max_length=10, min_length=2, error_messages={
        'max_length': 'Слишком дофига символов',
        'min_length': 'Слишком мало символов',
        'required': 'Слушай, поле нужно заполнить',
    })
    feedback = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 20}))
    rating = forms.IntegerField(label='Рейтиг', max_value=5, min_value=1, error_messages={
        'max_value': 'Слишком много. Нужно не более 5',
        'min_value': 'Слишком мало. Нужно не менее 1',
        'required': 'Нет, пустым оставить поле нельзя'
    })
