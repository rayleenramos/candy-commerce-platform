import os

content = """{% extends "base.html" %}

{% block title %}Create an Account - Keanu's Candy{% endblock %}

{% block content %}
<div class="min-h-[80vh] flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8">
    <div class="max-w-md w-full space-y-8 bg-white p-10 rounded-2xl shadow-lg card-hover">
        <div>
            <h2 class="mt-6 text-center text-3xl font-extrabold text-dark">Create your account</h2>
            <p class="mt-2 text-center text-sm text-gray-600">
                Already have an account? <a href="{% url 'login' %}" class="font-medium text-primary hover:text-red-500 transition-colors">Sign in</a>
            </p>
        </div>
        <form class="mt-8 space-y-6" action="{% url 'register' %}" method="post">
            {% csrf_token %}
            {% if form.errors %}
            <div class="bg-red-50 border-l-4 border-red-500 p-4 mb-4 rounded-md">
                <p class="text-red-700 text-sm font-medium">Please correct the errors below.</p>
                {{ form.non_field_errors }}
            </div>
            {% endif %}

            <div class="space-y-4">
                {% for field in form %}
                <div>
                    <label for="{{ field.id_for_label }}" class="block text-sm font-medium text-gray-700 mb-1">{{ field.label }}</label>
                    <input 
                        type="{{ field.field.widget.input_type }}" 
                        name="{{ field.name }}" 
                        id="{{ field.id_for_label }}" 
                        class="input-field text-center" 
                        {{ field.field.required|yesno:'required,' }}
                    >
                    {% if field.errors %}
                    <p class="mt-1 text-xs text-red-500">{{ field.errors.0 }}</p>
                    {% endif %}
                    {% if field.help_text %}
                    <p class="mt-1 text-xs text-gray-500">{{ field.help_text }}</p>
                    {% endif %}
                </div>
                {% endfor %}
            </div>

            <div>
                <button type="submit" class="group relative w-full flex justify-center py-3 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-primary hover:bg-red-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary transition-all shadow-md hover:shadow-lg active:scale-95">
                    Create Account
                </button>
            </div>
        </form>
    </div>
</div>
{% endblock %}
"""

path = "/Users/cesar/SE_proj/finalproject-candy_crushers/accounts/templates/accounts/register.html"

with open(path, "w") as f:
    f.write(content)

print(f"Successfully wrote robust content to {path}")
