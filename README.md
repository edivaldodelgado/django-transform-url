# django-transform-url
Code for taking a commom .html file template and change the inside references to django url references.


When you start a django-project and download a page template from internet, you have to change all src's and href's
in order to use the template mapping of django.

Here we aim to create a algorithm that you can set some parameters and change automatically those references.

Ex¹:

Commom Page Template:

<!-- Custom CSS -->
    <link href="css/helper.css" rel="stylesheet">
    
Django Templates:

<!-- Custom CSS -->
    <link href="{% static css/helper.css %}" rel="stylesheet">
    
    
Ex¹:

Commom Page Template:

<!-- Favicon icon -->
    <link rel="icon" type="image/png" sizes="16x16" href="images/favicon.png">
    
Django Templates:

<!-- Favicon icon -->
    <link rel="icon" type="image/png" sizes="16x16" href="{% media images/favicon.png %}">
    

