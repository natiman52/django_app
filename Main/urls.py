from django.urls import path
from .views import (
    home,AskQuestion,QuestionView,comment,LIke,DIslike,AskAnswer,add_view
)
from .Dviews import (
    DeleteAnswer,DeleteQuestion,deleteComment
)
from .Eview import (
    UpdateQuestion,UpdateAnswer

    )
app_name = 'main'

urlpatterns =[
    path('',home ,name='home'),
    path('Question/',AskQuestion,name='Question'),
    path('Question/<str:id>',QuestionView,name='List'),
    path('AskQuestion/<str:slug>',AskAnswer,name='AskAnswer'),
    path('comment/',comment,name='comment'),
    path('likes/',LIke,name='like'),
    path('dislike/',DIslike,name='dislike'),
    path('Delete-Question/<str:slug>',DeleteQuestion,name='delete_question'),
    path('Delete-Answer/<int:id>',DeleteAnswer,name='delete_answer'),
    path('Delete-Comment/<int:id>',deleteComment,name='delete_comment'),
    path('Edit-Question/<str:slug>',UpdateQuestion,name='update_question'),
    path('Edit-Answer/<int:id>',UpdateAnswer,name='update_answer'),
    path("add_view/<str:slug>",add_view,name="add_view")
]
