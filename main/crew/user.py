from dataclasses import dataclass, field

from main.config.jobs import Rights
from main.config.users import EnumJobs
from main.config.variables import jobs

no_role: Rights = Rights(**(jobs[EnumJobs.no_role]))
conductor: Rights = Rights(**(jobs[EnumJobs.conductor]))
engineer: Rights = Rights(**(jobs[EnumJobs.engineer]))
dispatcher: Rights = Rights(**(jobs[EnumJobs.dispatcher]))
admin: Rights = Rights(**(jobs[EnumJobs.admin]))


@dataclass
class User:
    """User model"""

    username: str
    password: str
    email: str
    active_role: str = EnumJobs.no_role
    is_active: bool = False
    is_online: bool = False
    is_admin: bool = False
    allowed_roles: list[EnumJobs] = field(default_factory=list)
    active_rights: Rights = field(default_factory=Rights)

    def __str__(self) -> str:
        """returns a string representation of the user"""
        return (
            f"user {self.username}\n "
            f"and has roles {self.active_role}\n "
            f"and is active {self.is_active}\n "
            f"and is online {self.is_online}\n"
            f"and is admin {self.is_admin}\n"
        )

    def show_active_role(self) -> str:
        """returns the active role of the user"""
        return self.active_role

    def show_allowed_roles(self) -> list[EnumJobs]:
        """returns the allowed roles of the user"""
        return self.allowed_roles

    def set_active_role(self, role: str) -> str:
        """sets the active role of the user"""
        if role not in self.allowed_roles:
            return f"{role} is not allowed to this user"
        if role == self.active_role:
            return f"{role} is already active"
        self.active_role = role
        match role:
            case EnumJobs.no_role:
                self.active_rights = no_role
                return f"role is now {self.active_rights}"
            case EnumJobs.conductor:
                self.active_rights = conductor
                return f"role is now {self.active_rights}"
            case EnumJobs.engineer:
                self.active_rights = engineer
                return f"role is now {self.active_rights}"
            case EnumJobs.dispatcher:
                self.active_rights = dispatcher
                return f"role is now {self.active_rights}"
            case EnumJobs.admin:
                self.active_rights = admin
                return f"role is now {self.active_rights}"

    def clear_active_role(self):
        """clears the active role of the user"""
        self.active_role = EnumJobs.no_role
        self.active_rights = no_role
        return self.active_role, self.active_rights

    def add_allowed_role(self, role: EnumJobs) -> str:
        """adds a role to the allowed roles of the user"""
        self.allowed_roles.append(role)
        if role not in self.allowed_roles:
            self.allowed_roles.append(role)
            return f"this user has the role {role}"
        return f"this user already now has the role {role}"

    def remove_allowed_role(self, role: EnumJobs) -> str:
        """removes a role from the allowed roles of the user"""
        if role not in self.allowed_roles:
            return f"this user does not have the role {role}"
        if role == self.active_role:
            self.set_active_role(EnumJobs.no_role)
            self.allowed_roles.remove(role)

            return (
                f"this user no longer has the role {role} and is now {self.active_role}"
            )
        self.allowed_roles.remove(role)
        return f"this user no longer has the role {role}"
