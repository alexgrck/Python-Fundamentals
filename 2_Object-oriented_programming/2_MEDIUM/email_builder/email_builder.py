from __future__ import annotations
from abc import ABC, abstractmethod


class Builder(ABC):
    @property
    @abstractmethod
    def email(self):
        pass

    @abstractmethod
    def update_from(self):
        pass

    @abstractmethod
    def update_to(self):
        pass

    @abstractmethod
    def update_title(self):
        pass

    @abstractmethod
    def update_content(self):
        pass

    def update_cc(self):
        pass

    def update_bcc(self):
        pass

    def update_html(self):
        pass


class EmailBuilder(Builder):
    def __init__(self):
        self._email = Email()

    @property
    def email(self) -> Email:
        return self._email

    def update_from(self, new_from):
        self._email.from_ = new_from
        return self

    def update_to(self, new_to):
        self._email.to_ = new_to
        return self

    def update_title(self, new_title):
        self._email.title = new_title
        return self

    def update_content(self, new_content):
        self._email.content = new_content
        return self

    def update_cc(self, new_cc, index=None):
        self._email.cc = new_cc
        return self

    def update_bcc(self, new_bcc, index=None):
        self._email.bcc = new_bcc
        return self

    def update_html(self, new_html):
        self._email.html = new_html
        return self


class Email:
    def __init__(
        self,
        from_="",
        to_="",
        title="",
        content="",
        cc: list = [],
        bcc: list = [],
        html="",
    ):
        self.from_ = from_
        self.to_ = to_
        self.title = title
        self.content = content
        self.cc = cc
        self.bcc = bcc
        self.html = html
