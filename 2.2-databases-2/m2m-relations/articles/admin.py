from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        if any(self.errors):
            return
        flags_count = 0

        for form in self.forms:
            if self.can_delete and self._should_delete_form(form):
                continue

            if form.cleaned_data.get("is_main", False):
                flags_count += 1

            if flags_count > 1:
                raise ValidationError('Не более одной главной категории')

        super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
