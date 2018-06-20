from django import forms
class kyaUser(forms.Form):
    f_n=forms.CharField(label="first name",max_length=100)
    #m_n=forms.CharField(label="middle name",max_length=100,required=False)
    l_n=forms.CharField(label="last name",max_length=100)
    u_n=forms.CharField(label="user name",max_length=100)
    email=forms.EmailField(required=False)
    p1=forms.CharField(label="Password",max_length=100)
    p2=forms.CharField(label="Confirm Password",max_length=100)
