from __future__ import annotations

from abc import ABC, abstractmethod
from datetime import datetime


class BaseMethods(ABC):
    access_value = 0

    def __init__(self, name, surname, email, gender, birth_date: str = "DD-MM-YYYY"):
        self.name = name
        self.surname = surname
        self.email = email
        self.birth_date = birth_date
        self.gender = gender
        self.author = f"{self.name} {self.surname}"

    def __gt__(self, other: BaseMethods) -> bool:
        return self.access_value > other.access_value

    def __eq__(self, other: object) -> bool:
        return (
            isinstance(other, self.__class__)
            and self.name == other.name
            and self.surname == other.surname
        )

    def __hash__(self) -> int:
        return hash((self.name, self.surname))

    def update_email(self, new_email):
        self.email = new_email
        return self.email

    def create_post(self, title, content, author):
        return Post(title=title, content=content, author=author)

    @abstractmethod
    def modify_post(self, post: Post, title="", content=""):
        new_stuff = {}
        if content:
            new_stuff["content"] = content
        if title:
            new_stuff["title"] = title
        return post.modify_post(**new_stuff)

    def delete_post(self, post: Post):
        return Post.post_list.remove(post)


class Post:

    post_list = []

    def __init__(self, title="", content="", author=""):
        self.title = title
        self.content = content
        self.author = author
        self.creation_date = datetime.now()
        self.last_modification_author = self.author
        self.modification_date = self.creation_date
        self.post_list.append(self)

    def __gt__(self, other: Post) -> bool:
        return self.content > other.content

    def __ne__(self, other: Post) -> bool:
        return self.author != other.author

    def modify_post(self, title="", content="", author=None):
        if title:
            self.title = title
        if content:
            self.content = content
        self.last_modification_author = self.author if author is None else author
        self.modification_date = datetime.now()
        return self


class User(BaseMethods):

    access_value = 1

    def update_email(self, new_email):
        return super().update_email(new_email=new_email)

    def create_post(self, title, content):
        post = super().create_post(title=title, content=content, author=self.author)
        return post

    def modify_post(self, post: Post, title="", content=""):
        if post.author != self.author:
            raise TypeError("You may not edit post which is not your own post.")
        super().modify_post(post, title=title, content=content)
        post.modification_date = datetime.now()
        post.last_modification_author = self.author
        return post

    def delete_post(self, post: Post):
        if post.author != self.author:
            raise TypeError("You may not delete post which is not your own post.")
        return super().delete_post(post)


class Redactor(BaseMethods):

    access_value = 2

    def update_email(self, new_email):
        return super().update_email(new_email=new_email)

    def create_post(self, title, content):
        post = super().create_post(title=title, content=content, author=self.author)
        return post

    def modify_post(self, post: Post, title="", content=""):
        super().modify_post(post, content=content, title=title)
        post.modification_date = datetime.now()
        post.last_modification_author = self.author
        return post

    def delete_post(self, post: Post, owner):
        if not isinstance(owner, Admin):
            return super().delete_post(post)
        else:
            raise TypeError("You may not delete Admin's post.")


class Admin(BaseMethods):

    access_value = 3

    def edit_attribute(self, edited_user, attrs_dict: dict):
        for attr_name, value in attrs_dict.items():
            setattr(edited_user, attr_name, value)
        if "name" or "surname" in attrs_dict.keys():
            edited_user.author = f"{edited_user.name} {edited_user.surname}"
        return edited_user

    def create_post(self, title, content):
        post = super().create_post(title=title, content=content, author=self.author)
        return post

    def modify_post(self, post: Post, title="", content=""):
        super().modify_post(post, title=title, content=content)
        post.modification_date = datetime.now()
        post.last_modification_author = self.author
        return post

    def delete_post(self, post: Post):
        return super().delete_post(post)
