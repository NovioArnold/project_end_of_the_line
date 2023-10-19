"""This module contains the Crew class."""

from dataclasses import dataclass, field
from typing import Optional



@dataclass
class Crew:
    name_role: str
    rights: dict = field(default_factory=dict)

    def __str__(self) -> str:
        return self.name_role + '\n' + self.show_rights()

    def show_rights(self) -> str:
        return self.rights.__str__()

    def update_rights(self,
                      right_category: str,
                      right_name: str,
                      right_value: bool):
        match right_category:
            case 'radio':
                match right_name:
                    case 'train_radio':
                        x = self.rights['radio']['train_radio']
                        flag = eval_bool(x, right_value)
                        if flag is True:
                            x = right_value
                            return x
                        else:
                            return x
                    case 'dispatch_radio':
                        x = self.rights['radio']['dispatch_radio']
                        flag = eval_bool(x, right_value)
                        if flag is True:
                            x = right_value
                            return x
                        else:
                            return x
                    case 'prio_speaker':
                        x = self.rights['radio']['prio_speaker']
                        flag = eval_bool(x, right_value)
                        if flag is True:
                            x = right_value
                            return x
                        else:
                            return x
                    case 'crew_lounge':
                        x = self.rights['radio']['crew_lounge']
                        flag = eval_bool(x, right_value)
                        if flag is True:
                            x = right_value
                            return x
                        else:
                            return x
                    case 'create_train_radio':
                        x = self.rights['radio']['create_train_radio']
                        flag = eval_bool(x, right_value)
                        if flag is True:
                            x = right_value
                            return x
                        else:
                            return x

            case 'switch_list':
                match right_name:
                    case 'create_switch_list':
                        x = self.rights['switch_list']['create_switch_list']
                        flag = eval_bool(x, right_value)
                        if flag is True:
                            x = right_value
                            return x
                        else:
                            return x
                    case 'view_switch_list':
                        x = self.rights['switch_list']['view_switch_list']
                        flag = eval_bool(x, right_value)
                        if flag is True:
                            x = right_value
                            return x
                        else:
                            return x
                    case 'update_switch_list':
                        x = self.rights['switch_list']['update_switch_list']
                        flag = eval_bool(x, right_value)
                        if flag is True:
                            x = right_value
                            return x
                        else:
                            return x
                    case 'delete_switch_list':
                        x = self.rights['switch_list']['delete_switch_list']
                        flag = eval_bool(x, right_value)
                        if flag is True:
                            x = right_value
                            return x
                        else:
                            return x
            case 'consist_table':
                match right_name:
                    case 'create_consist_table':
                        x = self.rights['consist_table']['create_consist_table']
                        flag = eval_bool(x, right_value)
                        if flag is True:
                            x = right_value
                            return x
                        else:
                            return x

                    case 'view_consist_table':
                        x = self.rights['consist_table']['view_consist_table']
                        flag = eval_bool(x, right_value)
                        if flag is True:
                            x = right_value
                            return x
                        else:
                            return x

                    case 'update_consist_table':
                        x = self.rights['consist_table']['update_consist_table']
                        flag = eval_bool(x, right_value)
                        if flag is True:
                            x = right_value
                            return x
                        else:
                            return x

                    case 'delete_consist_table':
                        x = self.rights['consist_table']['delete_consist_table']
                        flag = eval_bool(x, right_value)
                        if flag is True:
                            x = right_value
                            return x
                        else:
                            return x

            case 'item_manager':
                match right_name:
                    case 'create_item':
                        x = self.rights['item_manager']['create_item']
                        flag = eval_bool(x, right_value)
                        if flag is True:
                            x = right_value
                            return x
                        else:
                            return x

                    case 'view_item':
                        x = self.rights['item_manager']['view_item']
                        flag = eval_bool(x, right_value)
                        if flag is True:
                            x = right_value
                            return x
                        else:
                            return x

                    case 'update_item':
                        x = self.rights['item_manager']['update_item']
                        flag = eval_bool(x, right_value)
                        if flag is True:
                            x = right_value
                            return x
                        else:
                            return x

                    case 'delete_item':
                        x = self.rights['item_manager']['delete_item']
                        flag = eval_bool(x, right_value)
                        if flag is True:
                            x = right_value
                            return x
                        else:
                            return x

                    case 'set_rail_flag':
                        x = self.rights['item_manager']['set_rail_flag']
                        flag = eval_bool(x, right_value)
                        if flag is True:
                            x = right_value
                            return x
                        else:
                            return x

                    case 'set_out_of_service_flag':
                        x = self.rights['item_manager']['set_out_of_service_flag']
                        flag = eval_bool(x, right_value)
                        if flag is True:
                            x = right_value
                            return x
                        else:
                            return x

            case 'load_unload':
                match right_name:
                    case 'load_car':
                        x = self.rights['load_unload']['load_car']
                        flag = eval_bool(x, right_value)
                        if flag is True:
                            x = right_value
                            return x
                        else:
                            return x
                    case 'unload_car':
                        x = self.rights['load_unload']['unload_car']
                        flag = eval_bool(x, right_value)
                        if flag is True:
                            x = right_value
                            return x
                        else:
                            return x






