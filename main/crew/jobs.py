
from pydantic import BaseModel, Field

from main.helper import eval_str


class Right(BaseModel):
    """class for user rights"""
    name: str
    category: str
    value: bool

    def __str__(self) -> str:
        return self.name + '\n' + self.category + '\n' + self.value.__str__()

    def change_value(self, value: bool) -> bool:
        self.value = value
        return self.value

    def change_category(self, category: str):
        self.category = category
        return self.category


class Role(BaseModel):
    """class for user roles"""
    name: str
    rights: list[Right] = Field(default_factory=list)

    def __str__(self) -> str:
        return self.name + '\n' + self.show_rights()

    def show_rights(self) -> str:
        """show all rights of a role"""
        return self.rights.__str__()

    def add_right(self, right_name: str, category: str) -> list[Right] | ValueError:
        """add a right to a role if role not already in role"""
        if len(self.rights) > 0:
            for i in self.rights:
                if not eval_str(i['name'], right_name):
                    self.rights.append(Right(name=right_name, category=category, value=True))
                    return self.rights
                elif eval_str(i['name'], right_name):
                    return ValueError(f'Right {right_name} already exist')
                else:
                    return ValueError(f'Right {right_name} does not exist')
        else:
            self.rights.append(Right(name=right_name, category=category, value=True))
            return self.rights

    def remove_right(self, right_name) -> list[Right] | ValueError:
        """remove a right from a role"""
        for i in self.rights:
            if eval_str(i['name'], right_name):
                self.rights.remove(i)
                return self.rights
            else:
                ValueError(f'Right {right_name} does not in {self.name}')


class User(BaseModel):
    """class for user"""
    name: str
    password: str
    email: str
    discord_id: str
    roles: list[Role] = Field(default_factory=list)

    def __str__(self) -> str:
        return self.name + '\n' + self.show_roles()

    def show_roles(self) -> str:
        """show all roles of a user"""
        return self.roles.__str__()

    def add_role(self, role: str) -> list[Role] | ValueError:
        """add a role to a user if role not already in role"""
        for i in self.roles:
            if not eval_str(i['name'], role):
                self.roles.append(Role(name=role))
                return self.roles
            elif eval_str(i['name'], role):
                return ValueError(f'Role {role} already exist')
            else:
                ValueError(f'Role {role} does not exist')

    def remove_role(self, role: str) -> list[Role] | ValueError:
        """remove a role from a user"""
        for i in self.roles:
            if eval_str(i['name'], role):
                self.roles.remove(i)
                return self.roles
            else:
                return ValueError(f'Role {role} does not in {self.name}')







