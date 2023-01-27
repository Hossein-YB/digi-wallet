from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _


class Transaction(models.Model):
    TRANSACTION_CHOOSES = (
        (1, "Charge"),
        (2, "purchase"),
        (1, "Transfer"),
    )

    user = models.ForeignKey(get_user_model(), related_name="transaction", on_delete=models.RESTRICT,
                             verbose_name=_("user"))
    transaction_type = models.PositiveSmallIntegerField(choices=TRANSACTION_CHOOSES, verbose_name=_("Transaction type"))
    amount = models.BigIntegerField(_("amount"))
    datetime_created = models.DateTimeField(auto_now_add=True, verbose_name=_("date time created"))

    def __str__(self):
        return f"user {self.user}: do {self.transaction_type} {self.amount}"

    class Meta:
        verbose_name = _("Transaction")
        verbose_name_plural = _("Transactions")


class UserBalance(models.Model):
    user = models.ForeignKey(get_user_model(), related_name="balance_user", on_delete=models.RESTRICT,
                             verbose_name=_("user"))
    balance = models.BigIntegerField(verbose_name=_("balance"))
    datetime_created = models.DateTimeField(auto_now_add=True, verbose_name=_("date time created"))
    datetime_modified = models.DateTimeField(auto_now=True, verbose_name=_("date time modified"))

    def __str__(self):
        return f"user {self.user}: have balance {self.balance}"

    class Meta:
        verbose_name = _("user balance")
        verbose_name_plural = _("user balances")
