from django import forms
from .models import Student

class StudentForm(forms.Form):
    

    name = forms.CharField(max_length =100,
        widget = forms.TextInput(       
            attrs = {                            
                'placeholder':'Enter name',
                
            }
        )
    )

    roll_no = forms.IntegerField(
        widget = forms.NumberInput(       
            attrs = {                            
                'placeholder':'Enter roll_no',
               
            }
        )
    )

    email = forms.EmailField(
        widget = forms.EmailInput(       
            attrs = {                            
                'placeholder':'Enter email',
               
            }
        )
    )
    profile_pic = forms.ImageField(
        label='Profile Picture',                     #label : for giving custom label
            widget = forms.ClearableFileInput(       #widget : is for type in HTML input tag
                attrs = {                            #attrs : is used for attributes like placeholder
                    'accept':'image/*',
                    'placeholder':'Insert Image',
                    'class':'input-image'
                }
            )
        )

    phone_no = forms.CharField(max_length =14,
        widget = forms.TextInput(       
            attrs = {                            
                'placeholder':'Enter phone_no',
               
            }
        )
    )
    course = forms.ChoiceField(
        choices=Student.COURSES,
      
        
    )
