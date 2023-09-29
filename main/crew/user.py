from main.config.users import ConfigUser, Jobs
from main.crew.jobs import (conductor_rights,
                  engineer_rights,
                  dispatcher_rights,
                  admin_rights,)
from main.helper import eval_bool
from dataclasses import dataclass, field
from typing import Optional

JOBS = Jobs
@dataclass
class User:
    """User model"""
    username: str
    password: str
    email: str
    active_role: str = JOBS.no_role
    is_active: bool = False
    is_online: bool = False
    is_admin: bool = False
    allowed_roles: list[Jobs] = field(default_factory=list)
    active_rights: dict[ConfigUser] = field(default_factory=dict)

    def __str__(self) -> str:
        return (f'user {self.username}\n '
                f'and has roles {self.active_role}\n '
                f'and is active {self.is_active}\n '
                f'and is online {self.is_online}\n'
                f'and is admin {self.is_admin}\n')

    @classmethod
    def show_active_role(cls) -> active_role:
        return cls.active_role

    @classmethod
    def show_allowed_roles(cls) -> allowed_roles:
        return cls.allowed_roles


    def set_active_role(self, role: Jobs) -> str:
        if role not in self.allowed_roles:
            return f'{role} is not allowed to this user'
        else:
            if role == self.active_role:
                return f'{role} is already active'
            else:
                self.active_role = role
                return f'{role} is now active'

    def add_allowed_role(self, role: Jobs) -> str:
        self.allowed_roles.append(role)
        if role not in self.allowed_roles:
            self.allowed_roles.append(role)
            return f'this user has the role {role}'
        else:
            return f'this user already now has the role {role}'

    @classmethod
    def remove_allowed_role(cls, role: Jobs) -> str:
        if role not in cls.allowed_roles:
            return f'this user does not have the role {role}'
        else:
            cls.allowed_roles.remove(role)
            return f'this user no longer has the role {role}'

    def set_active_rights(self, role: Jobs) -> dict[active_rights] | ValueError:
        match role:
            case JOBS.conductor:
                self.active_rights.update(conductor_rights.radio_rights)
                self.active_rights.update(conductor_rights.timetable_rights)
                self.active_rights.update(conductor_rights.switch_list_rights)
                self.active_rights.update(conductor_rights.consist_table_rights)
                self.active_rights.update(conductor_rights.item_manager_rights)
                self.active_rights.update(conductor_rights.flags_rights)
                self.active_rights.update(conductor_rights.load_unload_rights)
                return self.active_rights
            case JOBS.engineer:
                self.active_rights.update(engineer_rights.radio_rights)
                self.active_rights.update(engineer_rights.timetable_rights)
                self.active_rights.update(engineer_rights.switch_list_rights)
                self.active_rights.update(engineer_rights.consist_table_rights)
                self.active_rights.update(engineer_rights.item_manager_rights)
                self.active_rights.update(engineer_rights.flags_rights)
                self.active_rights.update(engineer_rights.load_unload_rights)
                return self.active_rights
            case 'dispatcher':
                self.active_rights = dispatcher_rights
                return self.active_rights
            case 'admin':
                self.active_rights = admin_rights
                return self.active_rights
            case _:
                return ValueError(f'{role} is not a valid role')




