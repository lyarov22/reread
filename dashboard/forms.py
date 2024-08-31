from django import forms
from core.models import CustomUser

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone', 'name', 'surname', 'birthdate', 'gender', 'avatar']
        widgets = {
            'birthdate': forms.DateInput(attrs={'type': 'date'}),
            'avatar': forms.ClearableFileInput(attrs={'multiple': False}),
        }

    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance')
        super().__init__(*args, **kwargs)
        
        # Добавляем классы и устанавливаем начальные значения для всех полей формы
        for field_name, field in self.fields.items():
            if instance and hasattr(instance, field_name):
                placeholder_value = getattr(instance, field_name, None)
                # Устанавливаем значение поля в форме, если оно есть
                field.widget.attrs.update({
                    'class': 'w-full py-4 px-6 rounded-xl',
                    'value': placeholder_value if placeholder_value is not None else '',
                })

