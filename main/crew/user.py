from pydantic import BaseModel, Field
from jobs import conductor_rights
from main.helper import eval_bool


class User(BaseModel):
    """User model"""
    username: str = Field(default='user')
    password: str = Field(default='password')
    email: str = Field(default='email')
    allowed_roles: list[str] = Field(default_factory=list, name="allowed_roles")
    active_role: str = Field(default_factory=list, name="active_role")
    active_rights: dict[str, bool] = Field(default_factory=dict, name="active_rights")
    is_active: bool = Field(default=True, name="is_active")
    is_online: bool = Field(default=False, name="is_online")
    is_admin: bool = Field(default=False, name="is_admin")

    def __str__(self) -> str:
        return (f'user {self.username}\n '
                f'and has roles {self.active_role}\n '
                f'and is active {self.is_active}\n '
                f'and is online {self.is_online}\n'
                f'and is admin {self.is_admin}\n')

    def show_active_role(self) -> active_role:
        return self.active_role

    def show_allowed_roles(self) -> allowed_roles:
        return self.allowed_roles

    def set_active_role(self, role: str) -> str:
        if self.active_role == role:
            return f'active role is already {self.active_role}'
        elif role not in self.allowed_roles:
            return f'this user is not qualified for the role {role}'
        else:
            self.active_role = role
            return f'active role is now {self.active_role}'

    def add_allowed_role(self, role: str) -> str:
        if role in self.allowed_roles:
            return f'this user already has the role {role}'
        else:
            self.allowed_roles.append(role)
            return f'this user now has the role {role}'

    def remove_allowed_role(self, role: str) -> str:
        if role not in self.allowed_roles:
            return f'this user does not have the role {role}'
        else:
            self.allowed_roles.remove(role)
            return f'this user no longer has the role {role}'

    def set_active_rights(self, role: str) -> dict[active_rights]:
        match role:
            case 'conductor':
                self.active_rights = conductor_rights
                return self.active_rights



