from django.contrib import admin
from django.forms import BaseInlineFormSet
from django.core.exceptions import ValidationError

from .models import Article, Scope, Tag


class InLineFormset(BaseInlineFormSet):
    def clean(self):
        main_tag_count = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                main_tag_count += 1
        if main_tag_count > 1:
            raise ValidationError('Только один основной тег')
        super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = InLineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass