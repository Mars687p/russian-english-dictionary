from __future__ import annotations

from tortoise.models import Model
from tortoise import fields

class Word(Model):
    id = fields.IntField(pk=True)
    english_word = fields.CharField(max_length=64, default='')
    russian_word = fields.CharField(max_length=64, default='')
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = 'words'
        ordering = ('created_at',)

    def __str__(self):
        return f'{self.english_word} - {self.russian_word}'