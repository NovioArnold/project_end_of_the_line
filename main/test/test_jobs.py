from enum import StrEnum

from main.config.jobs import Rights
from main.config.users import EnumJobs
from main.config.variables import jobs
from main.crew.user import User


class TestJobs:

    def test_no_roles(self):
        test_user = Rights(**jobs[EnumJobs.no_role])
        assert test_user.name == 'no_role'
        assert test_user.radio_rights['train_radio'] is False
        assert test_user.radio_rights['dispatcher_radio'] is False
        assert test_user.radio_rights['crew_lounge'] is True
        assert test_user.radio_rights['priority_speaker'] is False
        assert test_user.radio_rights['create_train_radio'] is False
        assert test_user.radio_rights['delete_train_radio'] is False
        assert test_user.timetable_rights['view_timetable'] is False
        assert test_user.timetable_rights['update_timetable'] is False
        assert test_user.timetable_rights['create_timetable'] is False
        assert test_user.timetable_rights['delete_timetable'] is False
        assert test_user.switch_list_rights['view_switch_list'] is False
        assert test_user.switch_list_rights['update_switch_list'] is False
        assert test_user.switch_list_rights['create_switch_list'] is False
        assert test_user.switch_list_rights['delete_switch_list'] is False
        assert test_user.consist_table_rights['view_consist_table'] is False
        assert test_user.consist_table_rights['update_consist_table'] is False
        assert test_user.consist_table_rights['create_consist_table'] is False
        assert test_user.consist_table_rights['delete_consist_table'] is False
        assert test_user.item_manager_rights['view_item'] is False
        assert test_user.item_manager_rights['update_item'] is False
        assert test_user.item_manager_rights['create_item'] is False
        assert test_user.item_manager_rights['delete_item'] is False
        assert test_user.load_unload_rights['load_car'] is False
        assert test_user.load_unload_rights['unload_car'] is False
        assert test_user.load_unload_rights['view_product'] is False
        assert test_user.flag_rights['set_derail_flag'] is False
        assert test_user.flag_rights['set_is_ready_flag'] is False
        assert test_user.flag_rights['set_is_out_of_service_flag'] is False
        assert test_user.flag_rights['set_is_assigned_to_consist_flag'] is False
        assert test_user.flag_rights['set_is_occupied_flag'] is False
        assert test_user.flag_rights['set_is_routed_flag'] is False

    def test_dispatcher(self):
        test_user = Rights(**jobs[EnumJobs.dispatcher])
        assert test_user.name == 'dispatcher'
        assert test_user.radio_rights['train_radio'] is False
        assert test_user.radio_rights['dispatcher_radio'] is True
        assert test_user.radio_rights['crew_lounge'] is True
        assert test_user.radio_rights['priority_speaker'] is True
        assert test_user.radio_rights['create_train_radio'] is True
        assert test_user.radio_rights['delete_train_radio'] is True

    def test_create_user(self):
        test_user = User('test_user', 'test_password', 'dispatcher')
        assert test_user.username == 'test_user'
        assert test_user.show_active_role() == 'no_role'
        test_user.add_allowed_role(EnumJobs.dispatcher)
        assert test_user.show_allowed_roles() == ['dispatcher']
        test_user.set_active_role('dispatcher')
        assert test_user.show_active_role() == 'dispatcher'
        test_user.remove_allowed_role(EnumJobs.dispatcher)
        test_user.clear_active_role()

        assert test_user.show_allowed_roles() == []

        assert test_user.active_rights.radio_rights['train_radio'] is False
        assert test_user.active_rights.radio_rights['dispatcher_radio'] is False


