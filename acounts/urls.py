urlpatterns = [
    # (...manter tudo o que já existe…)
    path(
        "account/<int:pk>/edit", views.AccountUpdateView.as_view(), name="account_edit"
    ),
]
