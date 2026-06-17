"""User model for the Project Management CLI."""

class Person:
    """Base class for inheritance requirement."""
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email # Uses setter below
    
    def __repr__(self) -> str:
        return f"Person(name='{self.name}', email='{self.email}')"


class User(Person):
    """User inherits from Person. One-to-many: User -> Projects"""
    _id_counter = 1
    
    def __init__(self, name: str, email: str):
        super().__init__(name, email)
        self.id = User._id_counter
        User._id_counter += 1
        self.projects = []
    
    @property
    def email(self) -> str:
        return self._email
    
    @email.setter 
    def email(self, value: str):
        if "@" not in value or "." not in value:
            raise ValueError("Email must be valid format: user@domain.com")
        self._email = value
    
    def add_project(self, project):
        self.projects.append(project)
    
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "project_ids": [p.id for p in self.projects]
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        user = cls(data["name"], data["email"])
        user.id = data["id"]
        User._id_counter = max(User._id_counter, data["id"] + 1)
        return user
    
    def __str__(self) -> str:
        return f"User {self.id}: {self.name} <{self.email}>"