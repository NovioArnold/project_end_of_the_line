from main.config.router import Router
from main.config.tracks import Mainline, Siding, Junctions, Yards, TrackSection, TrackTypes, Route

class TestRouter:
    test_router = Router(consist_id='test_router')
    def test_view_router(self):

        assert self.test_router.consist_id == 'test_router'
        assert self.test_router.route_name == 'none'
        assert self.test_router.track_section == []

    def test_get_route(self):
        assert self.test_router.get_route() == []

    def test_get_route_name(self):
        assert self.test_router.get_route_name() == 'none'

    def test_get_consist_id(self):
        assert self.test_router.get_consist_id() == 'test_router'

    def test_set_route(self):
        self.test_router.route_name = Route.none
        assert self.test_router.route_name == 'none'


    def test_add_track_section(self):
        self.test_router.track_section.append(Mainline.none)
        assert self.test_router.track_section == ['none']

    def test_remove_track_section(self):
        self.test_router.track_section.remove(Mainline.none)
        assert self.test_router.track_section == []


