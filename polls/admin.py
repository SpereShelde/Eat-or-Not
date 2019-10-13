from django.contrib import admin

from .models import Question, Choice, User, QuestionTuple


class ChoiceInline(admin.StackedInline):
    # admin.TabularInline
    model = Choice
    extra = 3

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('tuple', 'question_text')
    # fields = ['tuple', 'question_text']
    list_per_page = 20
    # ordering = ('-name',) #ordering设置默认排序字段，负号表示降序排序
    actions_on_top = True
    actions_on_bottom = True
    actions_selection_counter = True
    empty_value_display = ' -Empty- '
    fk_fields = ('tuple')
    # 过滤器功能及能过滤的字段
    list_filter = ('tuple', 'question_text')
    # 搜索功能及能实现搜索的字段
    search_fields = ('tuple', 'question_text')
    inlines = [ChoiceInline]

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('question', 'choice_text', 'votes')
    # fields = ['tuple', 'question_text']
    list_per_page = 20
    # ordering = ('-name',) #ordering设置默认排序字段，负号表示降序排序
    actions_on_top = True
    # actions_on_bottom = True
    actions_selection_counter = True
    empty_value_display = ' -Empty- '
    fk_fields = ('question',)
    # list_filter = ('question')
    # 搜索功能及能实现搜索的字段
    search_fields = ('question', 'choice_text')

class QuestionTupleAdmin(admin.ModelAdmin):
    # fieldsets = [
    #     ('Tuple', {'fields': ['tuple_name']}),
    #     ('Date', {'fields': ['pub_date']}),
    # ]
    # Question_inlines = [QuestionInline]
    #
    list_display = ('tuple_name', 'pub_date')
    # fields = ['tuple', 'question_text']
    list_per_page = 20
    # ordering = ('-name',) #ordering设置默认排序字段，负号表示降序排序
    actions_on_top = True
    # actions_on_bottom = True
    actions_selection_counter = True
    empty_value_display = ' -Empty- '
    list_filter = ('tuple_name', 'pub_date')
    # 搜索功能及能实现搜索的字段
    search_fields = ('tuple_name', 'pub_date')
    inlines = [QuestionInline]

class UserAdmin(admin.ModelAdmin):
    list_display = ('account', 'name')
    # fields = ['tuple', 'question_text']
    list_per_page = 20
    # ordering = ('-name',) #ordering设置默认排序字段，负号表示降序排序
    actions_on_top = True
    # actions_on_bottom = True
    actions_selection_counter = True
    empty_value_display = ' -Empty- '
    list_filter = ('account', 'name')
    # 搜索功能及能实现搜索的字段
    search_fields = ('account', 'name')

# admin.site.register(Choice)
admin.site.register(QuestionTuple, QuestionTupleAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)